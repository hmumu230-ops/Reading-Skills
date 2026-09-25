# book-distill · 小A式万字解读 Skill

把「小A学财经」蒸馏书籍的方法做成可复用 skill：用结构式阅读把一本书提炼成 3~7 个核心观点，产出**蒸馏笔记 + 分集大纲 + 万字口语讲稿**。

## 用法

在 Devin CLI 会话中（技能目录在 `.devin/skills/` 下即自动注册）：

```
/book-distill 《思考，快与慢》            # 只有书名：凭知识蒸馏，会标注存疑点
/book-distill ./books/hei-tian-e.txt     # 给原文/笔记文件：读原文蒸馏，保真最高
```

投喂电子书文件（推荐）：

```
python3 tools/extract_book.py ~/Downloads/某本书.epub   # epub 直接解（纯标准库）
python3 tools/extract_book.py 某本书.pdf               # pdf 需系统有 pdftotext 或 PyMuPDF
# 生成 books/《书名》.txt → 然后 /book-distill books/《书名》.txt
```

## 产出

```
output/《书名》/
├── 00-蒸馏笔记.md   # 核心论点+论证链+金句，看笔记=几分钟回忆起全书
├── 01-大纲.md       # 分集大纲（问题式/反常识标题），确认后才写稿
├── 02~NN-*.md       # 逐集讲稿，每集 1500~3000 字
└── 99-完整版.md     # 合并稿，末尾带「终极清单」记忆锚点
```

## 核心思路

不是把书读薄，而是**讲透不讲全**：问题先行 → 抓骨架 → 观点/论证/案例三层分离 → 三重闸门筛选（承重墙/能复述/可迁移）→ 重建论证链 → 补读作者生平/版本差异 → 按听众行动路径重组 → 本土化映射 → 费曼式口语输出。方法论还吸收了同类 skill 的精华（三重验证/四档置信度/误读陷阱等，见 `蒸馏提炼类skill调研清单.md`）。

方法论提炼自真实讲稿样本（`research/`，本地研究目录，**含第三方字幕内容，不随仓库发布**）：YouTube 频道 `@ALittleFinance` 的《聪明的投资者》60分钟万字解读全稿、《滚雪球》33集连播中文逐字稿（开场公式/上集回顾/大结局清单均从逐字稿逆向）。字幕为自动生成，仅供方法研究。

## 文件

- `.devin/skills/book-distill/SKILL.md` — skill 本体（单文件，可整目录拷走复用）
- `.devin/skills/book-distill/examples/` — 分集大纲样例
- `.devin/plan.md` — 开发计划与决策记录
- `tools/extract_book.py` — 电子书→纯文本提取器
- `output/《认知觉醒》/` — 端到端演示产物（蒸馏笔记+大纲+7集讲稿+完整版，约万字）
- `蒸馏提炼类skill调研清单.md` — 同类蒸馏 skill 调研与精华吸收记录
- `research/` — 逐字稿样本（已 gitignore，仅限本地）
