#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_book.py — 把电子书提取成纯文本，供 /book-distill 模式A 使用

用法:
    python3 tools/extract_book.py <book.epub|book.txt|book.md|book.pdf>

产出: books/<书名>.txt（含章界标记 [CH xx] 和开头元信息）

依赖: 仅 python3 标准库。pdf 需系统装有 pdftotext 或 PyMuPDF(fitz)，
否则打印手动转换指引后退出。
"""
import html.parser
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "books"

NS = {
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
    "ct": "urn:oasis:names:tc:opendocument:xmlns:container",
}

BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "br",
              "tr", "section", "article", "chapter", "blockquote"}


class TextExtractor(html.parser.HTMLParser):
    """剥标签保段落。块级标签转换行，其余丢弃。"""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0  # script/style 深度

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        raw = "".join(self.parts)
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in raw.split("\n")]
        return "\n".join(ln for ln in lines if ln)


def xhtml_to_text(data: bytes) -> str:
    p = TextExtractor()
    p.feed(data.decode("utf-8", errors="replace"))
    return p.text()


def first_heading(xhtml: bytes) -> str:
    m = re.search(rb"<h[1-3][^>]*>(.*?)</h[1-3]>", xhtml, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", "", m.group(1).decode("utf-8", errors="replace"))
    return t.strip()[:60]


def extract_epub(path: Path) -> tuple[str, list[tuple[str, str]]]:
    """返回 (书名, [(章标题, 正文)])。按 OPF spine 顺序。"""
    zf = zipfile.ZipFile(path)
    # container.xml -> opf 路径
    container = ET.fromstring(zf.read("META-INF/container.xml"))
    opf_rel = container.find(".//ct:rootfile", NS).get("full-path")
    opf_dir = str(Path(opf_rel).parent)
    if opf_dir == ".":
        opf_dir = ""
    opf = ET.fromstring(zf.read(opf_rel))

    meta = opf.find("opf:metadata", NS)
    title_el = meta.find("dc:title", NS) if meta is not None else None
    title = (title_el.text or "").strip() if title_el is not None else ""
    title = title or path.stem

    manifest = {it.get("id"): it.get("href")
                for it in opf.findall("opf:manifest/opf:item", NS)}
    spine_ids = [ir.get("idref")
                 for ir in opf.findall("opf:spine/opf:itemref", NS)]

    chapters = []
    for idx, idref in enumerate(spine_ids, 1):
        href = manifest.get(idref)
        if not href:
            continue
        full = f"{opf_dir}/{href}" if opf_dir else href
        full = full.replace("\\", "/").lstrip("/")
        try:
            data = zf.read(full)
        except KeyError:
            continue  # 有些 href 带 url 编码或锚点，容错跳过
        txt = xhtml_to_text(data)
        if len(txt) < 30:
            continue  # 跳过封面/版权页等空壳
        heading = first_heading(data) or Path(href).stem
        chapters.append((heading, txt))
    return title, chapters


def extract_pdf(path: Path) -> tuple[str, list[tuple[str, str]]]:
    if shutil.which("pdftotext"):
        out = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True, text=True, check=True).stdout
        return path.stem, [("全文", out)]
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(str(path))
        pages = [(f"p{i+1}", pg.get_text()) for i, pg in enumerate(doc)]
        merged = "\n\n".join(t for _, t in pages)
        return path.stem, [("全文", merged)]
    except ImportError:
        pass
    sys.exit(
        "PDF 提取需要 pdftotext(poppler) 或 PyMuPDF，均未找到。\n"
        "任选其一后重试：\n"
        "  pip install pymupdf\n"
        "  或安装 poppler 提供 pdftotext\n"
        "  或手动把 PDF 转成 txt 放到 books/ 目录。")


def normalize_text(path: Path) -> tuple[str, list[tuple[str, str]]]:
    return path.stem, [("全文", path.read_text(encoding="utf-8", errors="replace"))]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    if not src.exists():
        sys.exit(f"文件不存在: {src}")

    ext = src.suffix.lower()
    if ext == ".epub":
        title, chapters = extract_epub(src)
    elif ext == ".pdf":
        title, chapters = extract_pdf(src)
    elif ext in (".txt", ".md"):
        title, chapters = normalize_text(src)
    else:
        sys.exit(f"不支持的格式 {ext}（支持 .epub/.txt/.md/.pdf）")

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{title}.txt"
    total = 0
    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"《{title}》 来源: {src.name} 章节数: {len(chapters)}\n\n")
        for i, (head, body) in enumerate(chapters, 1):
            f.write(f"\n\n[CH {i:02d}] {head}\n\n{body}\n")
            total += len(body)

    print(f"OK  {out_path}")
    print(f"    章节 {len(chapters)} | 正文约 {total} 字")
    print(f"    下一步: /book-distill {out_path}")


if __name__ == "__main__":
    main()
