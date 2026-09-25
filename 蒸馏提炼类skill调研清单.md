# 蒸馏/提炼类 Skill 调研清单

> 调研日期：2026-09-24 · 目的：为 `book-distill`（小A式万字解读）寻找同类/互补的 GitHub skill
> 热度为该仓库总 star（skills 合集的 star 归属整个仓库，非单个 skill）

## 一、书籍蒸馏 / 拆书（与 book-distill 同赛道）

| Skill | 仓库 | 热度 | 核心做法 | 可借鉴点 |
|---|---|---|---|---|
| cangjie-skill | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | ⭐10.5k | **元 skill**：书/视频/播客 → 一组可执行的原子 skills。RIA-TV++ 流水线：Adler 整书理解 → 5 个提取器并行 → 三重验证 → RIA++ 构造 → Zettelkasten 互链 → 压力测试 | 三重验证闸门、PIPELINE_STATE 断点续跑、rejected/ 淘汰审计 |
| ljg-book | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | ⭐7.4k | 双轴重建全书：source-blind 读者能复述书的实际内容 + 主线如何相连；保留多线发展 | 「外行能复述」验收标准，比"讲透"更可检验 |
| high-fidelity-book-distillation | [X-FRI/skills](https://github.com/X-FRI/skills/blob/main/skills/high-fidelity-book-distillation/SKILL.md) | ⭐2 | 把书重建成"问题-主张-理由-证据-概念-注意事项-应用"系统；references 分层按需加载 | 版权边界最严（禁编造页码/引用/数据）、金融/医疗领域规则文件 |
| book-distiller | [daizhouchen/book-distiller](https://github.com/daizhouchen/book-distiller) | ⭐10 | 蒸馏成中文典雅风单文件 HTML。七基因组合模型（人物/叙事/论证/模型/史料/美学/体验） | **事实系统化四步法**（穷尽提取→维度分类→模式识别→跨维度交织）、误读陷阱+作者盲点、信源 ABCD 分级 |
| book-reader | [hijiangtao/book-reader-skill](https://github.com/hijiangtao/book-reader-skill) | ⭐10 | PDF/EPUB/MOBI/TXT → extract_book.py 解析 JSON → 分批提炼知识点 → 阶段性摘要 → Markdown 笔记 | 带实体提取脚本；按书长度分档批处理策略（<30/30-100/100-300/>300页） |
| distill-book | [maragudk/fabrik](https://github.com/maragudk/fabrik/blob/main/skills/distill-book/SKILL.md) | ⭐26 | 按章拆分 → 每章一个 subagent 独立蒸馏 → 主上下文只读概述再综合 | 工程精华：**永不把原章文本拉进主上下文**，可扩展任意长 |
| book-to-skill | [alirezarezvani/claude-skills](https://www.skillsdirectory.com/skills/alirezarezvani-book-to-skill-claude-skills) | — | 书 → agent skill：常驻 SKILL.md(<4k token) + 按需章节文件 + 术语表 + 决策 cheatsheet | token 预算分层的知识库设计 |
| book-distill | [melodic-software](https://www.skillsdirectory.com/skills/melodic-software-book-distill) | — | 技术书(PDF/EPUB) → 按概念（非章节）组织的 skill reference 文件，多会话流水线 | 「按概念命名不按章节」的文件组织 |
| book-summary | [ferroxlabs/book-summary](https://claudskills.com/skills/book-summary/) | — | 分析型摘要：中心论点+3-5关键观点+金句+方法论评估+与其他书的关联 | 「评估作者论证方法」这一步你的 skill 没有 |

## 二、文章/长文精读与提炼（对应"提炼文章核心及思路"）

| Skill | 仓库 | 热度 | 核心做法 |
|---|---|---|---|
| dsh-deepread | [xiehuan123/dsh-deepread](https://github.com/xiehuan123/dsh-deepread) | ⭐56 | 精读文章或书，5 模式：quick / deep / map 知识地图 / feynman 费曼 / book。**证据纪律最严**：四档置信度（作者原意/原文事实/合理推断/无法确认）、"原文未提供证据"明写、案例≠普遍证据、相关≠因果。可导出 md/FreeMind/HTML |
| deep-reading-analyst | [ginobefun/deep-reading-analyst-skill](https://github.com/ginobefun/deep-reading-analyst-skill) | ⭐350 | 10+ 思维框架分深度用：SCQA/5W2H(15min) → 批判性思维/反向思考(30min) → 心智模型/第一性原理/系统思维/六顶帽子(60min) → 多源对比(120min) |
| insight-extractor | [yfge/video-skills-suite](https://github.com/yfge/video-skills-suite) | ⭐1 | 长文本（转写稿/研报/文章）→ 核心论点+金句（留原话+时间戳）+争议点+行动项；下游接 article-forge 成文，video-pipeline 一键全链路 |
| extractwisdom | [mj-deving/pai-skills](https://skillsmp.com/zh/creators/mj-deving/pai-skills/skills-contentanalysis-extractwisdom) | — | fabric `extract_wisdom` 的 skill 版：不套固定栏目，检测内容里实际存在的智慧域再定制板块 |
| essence-distiller | [live-neon/skills](https://github.com/live-neon/skills/blob/main/pbd/essence-distiller/SKILL.md) | — | 找"改写后仍然存活的承重墙观点"，不做摘要做原理 |
| agent-skill-summarizer | [jiangxidong/agent-skill-summarizer](https://github.com/jiangxidong/agent-skill-summarizer) | — | 文章/播客/转写稿 → 中英双语 Obsidian 笔记；PACER 知识分类法（Procedural/Analogous/Conceptual/Evidence/Reference），每类配消化模板 |
| research-summarizer | [alirezarezvani/claude-skills](https://www.skills.sh/alirezarezvani/claude-skills/research-summarizer) | — | 论文→IMRAD、网文→claim-evidence-implication、报告→executive summary，按源类型换结构；/summarize /compare /cite 三命令 |
| research-extract | [katyella/research-extract](https://github.com/katyella/research-extract/blob/main/SKILL.md) | — | YouTube/播客/博客/PDF → 分块 → **并行 agent 团队**各领一块提取 → Show Notes + Cheat Sheet HTML |
| expert-interview-notes | [sunyuzheng/expert-interview-notes](https://github.com/sunyuzheng/expert-interview-notes) | — | 专家访谈/播客转写 → 克制的内部笔记：保留判断、假设、张力、未决问题，**故意不写成行动清单** |
| 爆款笔记拆解 | [atian-create/single-note-breakdown-skill](https://github.com/atian-create/single-note-breakdown-skill) | — | 单条小红书/抖音 → 为什么被点/被看完/被收藏 + 可学结构 vs 不可复制资源分离 |

## 三、ljg-skills 单品（⭐7.4k 仓库内与提炼强相关的）

> 仓库：<https://github.com/lijigang/ljg-skills> · `bunx skills add lijigang/ljg-skills#md --skill <名>` 单装（md 分支是 Markdown 格式）

| Skill | 一句话 |
|---|---|
| ljg-qa | 信息提问机：把文章/书的核心观点抽成 Q-A 链，A 固定四段（结论/形式化/步骤/边界）|
| ljg-plain | 白话引擎：任何内容改写到聪明十二岁小孩能懂 —— **和小A口语讲稿最像** |
| ljg-learn | 概念解剖：八方向切一个概念（历史/辩证/现象/语言/形式/存在/美感/元反思）压成一句顿悟 |
| ljg-read | 伴读：英文三层翻译（信达雅）+ 结构标注 + 深度提问 + 跨领域旁逸 |
| ljg-paper | 论文阅读：面向无背景读者，从角色与动作讲清研究问题/贡献/证据边界 |
| ljg-writes | 写作引擎：把一个观点写成可理解、可迁移、经得住反例的中文文章 |
| ljg-structure | 母题结构风洞：表层问题 → 反复母题 → 可迁移结构 + ASCII 图 |
| ljg-think | 追本之箭：一个观点纵向钻到不可再分的本质 |
| ljg-rank | 降秩引擎：给一个领域找出不可再少的独立生成器 |
| ljg-is | 理解引擎：「是什么」接「怎样运作」→ 认知修正 + 可执行判断 |
| ljg-present | Unix 演讲设计：保真排版/授权讲稿提炼，五类版式，单文件离线 HTML |
| ljg-card | 内容铸卡：文本 → 长图/全文卡/漫画/白板 PNG |

## 四、音视频/转写稿 → 摘要

| Skill | 仓库 | 说明 |
|---|---|---|
| audio-tldr | [AugustusW/audio-tldr-skill](https://github.com/AugustusW/audio-tldr-skill) | YouTube/播客/本地音视频 → whisper 本地转写（哈希缓存）→ 3-7 条要点 |
| lai-summarize | [lattifai/lattifai-skills](https://github.com/lattifai/lattifai-skills/blob/main/skills/lai-summarize/SKILL.md) | 转写稿 → TL;DR+章节时间戳+金句；prepare.py 造 prompt → agent 写 → validate.py 验 |
| youtube-summarizer | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/youtube-summarizer) | YT 字幕 → STAR+R-I-S-E 框架详细摘要 |
| last30days | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Reddit/X/YouTube/HN 近 30 天讨论 → 综合摘要 |
| distill-knowledge | [dimdasci/distill-knowledge](https://github.com/dimdasci/distill-knowledge) | 会议录像 → 说话人标注转写 + 分主题文档 |

## 五、蒸馏产物的沉淀去向（知识库类）

| Skill | 仓库 | 说明 |
|---|---|---|
| llm-wiki | [akillness/oh-my-skills](https://github.com/akillness/oh-my-skills/blob/main/.agent-skills/llm-wiki/SKILL.md) | Karpathy gist 的 skill 化：原始源不动，LLM 维护 wiki 层 + index.md + log.md + lint |
| kmd | [yasik/kmd](https://github.com/yasik/kmd) | markdown 知识库 ingest/lint 双 skill，Obsidian 一等公民 |
| obsidian-skills | [tpitsunov/obsidian-skills](https://github.com/tpitsunov/obsidian-skills) | /atomize 长文拆 Zettel、/fleeting  inbox 处理、/tag 打标；AI_Outbox 隔离区模式 |
| distiller | [Chi-hong22/distiller](https://github.com/Chi-hong22/distiller) | AI 对话 → 场景化知识笔记（项目收尾/bug复盘/重构/学习/通用） |
| make-note | [birbirbrian/make-note-skills](https://github.com/birbirbrian/make-note-skills) | 对话 → Obsidian 笔记（callout+wiki 链接） |

## 六、蒸馏下游：成稿/讲稿/发布

| Skill | 仓库 | 说明 |
|---|---|---|
| se7en-talkline | [yiliqi78/se7en-skills](https://github.com/yiliqi78/se7en-skills/blob/main/skills/se7en-talkline/SKILL.md) | 演讲剧本生成器：屏幕（减法精华）/口述（加法主体）双通道拆分 → Markdown 剧本 + slide-manifest.yaml |
| pptalker | [YoungXu06/pptalker-skill](https://github.com/YoungXu06/pptalker-skill) | PPT/PDF/HTML → 逐页讲稿（确认后渲染）→ AI 配音+字幕视频 |
| ppt-tts-script | [ninehills/skills](https://skillsmp.com/es/creators/ninehills/skills/ppt-tts-script) | PPT → 拟人化逐字稿（md+json），回写演讲者备注 |
| wechat-skill | [843645440/wechat-skill](https://github.com/843645440/wechat-skill) | 公众号全链路：命题写作→原生信息模块→4套主题排版→不掉格式 HTML→草稿箱 |
| wechat-mp-writer | [fengqiliu/PM-Skills](https://skillsmp.com/zh/creators/fengqiliu/pm-skills/skills-wechat-mp-writer-skill) | 公众号写作：热点选题+去AI味+配图+发布草稿箱 |
| article-forge | [yfge/video-skills-suite](https://github.com/yfge/video-skills-suite) | 观点摘要+素材 → 可发布文章（博客/知乎/公众号），内置 anti-ai.md 检查表 |

## 七、索引站（继续挖的地方）

- [skills.sh](https://www.skills.sh) — vercel-labs 官方目录，按安装量排名；`npx skills add <repo> --skill <名>`
- [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) — 1000+，官方团队出品为主
- [KairoxJarvis/awesome-agent-skills](https://github.com/KairoxJarvis/awesome-agent-skills) — 偏知识工作/非技术岗
- [ningzimu/awesome-skills](https://github.com/ningzimu/awesome-skills) ⭐27 — 精简人工精选
- [junminhong/awesome-agent-skills](https://github.com/junminhong/awesome-agent-skills) — 含设计模式章节
- [skillsdirectory.com](https://www.skillsdirectory.com) / [claudskills.com](https://claudskills.com) / [skillsmp.com](https://skillsmp.com) — 目录站，Grade 评级
- [anthropics/skills](https://github.com/anthropics/skills) — 官方：docx/pdf/pptx/xlsx 文档处理 + skill 写作规范
- [obra/superpowers](https://github.com/obra/superpowers) — `writing-skills`：用 TDD 思路写 skill（压力场景测试）

## 八、和 book-distill 的差异化定位

你的 skill 独特处（别人都没有的）：**讲给别人听**——分集+钩子标题+口语讲稿+万字篇幅，是内容生产不是学习笔记。

可直接吸收的技巧（按 ROI 排序）：

1. **ljg-qa 的 Q-A 链**：你已有"观点改写成听众会问的问题"，ljg 的 A 四段式（结论/形式化/步骤/边界）可让每集讲稿更抗问
2. **dsh-deepread 四档置信度**：升级你的「存疑清单」——作者原意/原文事实/合理推断/无法确认
3. **book-distiller 误读陷阱+作者盲点**：加一集"这本书常被怎么误读"天然是爆款钩子
4. **fabrik 章节并行 subagent**：整本 epub 不再一页页读
5. **cangjie 三重验证闸门**：核心观点入选前先过"有证据/能复述/可迁移"
6. **insight-extractor 争议点单列**：金句留原话、分歧双方各自理由——讲稿里的张力来源
7. **high-fidelity 的版权纪律**：禁编造页码/引用/数据，和你的存疑清单互补
8. **se7en-talkline 屏幕/口述分离**：若以后讲稿要配视频/PPT，这套双通道可直接用
