# LICENSES — 许可边界独立账（2026-10-29 建账）

本账为将来论文发表与商业闭源预留：所有资产按许可类别分开登记。与 MANIFEST.md（资产总清单）的许可栏互为印证；条目级许可（数据集逐例）以 masters-dataset 各条 license_status / redistributable 字段为准。

## 1. 我们原创的（可自由用于论文与闭源商业）
- 知识库正文：docs/KNOWLEDGE-BASE.md（原 README）、chinese-yijing.md、chinese-liuyao-meihua.md、chinese-bazi-ziwei.md、western-tarot.md、western-astro-numerology-runes.md、lifekline-method.md、calibration.md、MANIFEST.md
- 占卜 skill：~/workspace/custom-skills/divination/SKILL.md
- 工具脚本：divination/tools/cast_iching.py、draw_tarot.py、draw_runes.py 及自建机器可读数据集（hexagrams-64 / tarot-78 / runes-24 / ganzhi-jieqi JSON，程序生成与校验）
- 基准与评测：masters-dataset 的 SCHEMA.md / schema.json / DATASHEET.md / splits 设计、benchmark/PROTOCOL.md、benchmark/evaluation/evaluate.py、benchmark/iterations.md 与各轮 runs/ 证据包
- 数据集的整理结构（字段设计、去重/划分/编码劳动）本身为原创；但条目内容（大师断语节录等）的权利状态逐条见第 5 节与各条字段，不因整理而改变。

## 2. 公版原典（PD / PD-US，可引用原文；发布时按各条出处著录）
- 《周易》经文+文言、《增删卜易》、《渊海子平》、《梅花易数》（托名存疑，内容公版）— 维基文库本，sources/chinese/
- 《三命通会》原作 — 公版（其现代转录见第 3 节）
- Waite《Pictorial Key to the Tarot》1911（Sacred-Texts 本）；de Laurence 1918 影印本（Gutenberg #43548，PD-US，版本对照用）
- Legge 译《I Ching》1882（PD）
- 《诗体埃达》Bellows 译（Gutenberg #73533，PD-US）、符文诗（英文维基文库，PD）
- 托勒密《Tetrabiblos》Ashmand 译（Gutenberg #70850，PD-US）
- Lilly《Introduction to Astrology》1852（Internet Archive，PD）；《Christian Astrology》1647（西方数据集 auxiliary 所存文本，PD）

## 3. CC 类
- 《三命通会》GitHub 转录本（mikkokotila/Sanming-Tongshui，四库本镜像）：原作 PD / 转录整理 CC BY-SA 4.0 — 再分发该转录文本须署名并同许可共享。
- 学术 OA 论文 5 篇：Religions 2024 ×2、Religions 2014（均 CC BY）、Adler 朱熹占卜章节（大学主页公开发布）、Dao 2024 Shaughnessy 书评（OA）— 引用遵各刊许可。

## 4. MIT / BSD 类开源代码（可依法使用，保留版权与许可声明）
- 6tail/lunar-python（MIT，tools/repos/lunar-python）— 八字/历算主库
- SylarLong/iztro（MIT，tools/repos/iztro）— 紫微排盘
- metabismuth/tarot-json（MIT）、godcong/yi（MIT）— 数据集
- yuangu/sxtwl_cpp（BSD-3-Clause）— 寿星天文历
- lifekline 两仓（Harry-commit / curionox）：**无 LICENSE 文件**——仅作方法研究与谱系核查参照，不复制其代码进原创资产（见 lifekline-method.md）。
- tarot-api 的 card_data.json：未声明许可，内容源出 Waite 公版牌义——只作研究参照，商用前须替换为自建 tarot-78 数据。

## 5. AGPL / 商业双许可（⚠️ 闭源商用红线）
- **aloistr/swisseph（Swiss Ephemeris，AGPL / 商业双许可 CHF 700）** 与 **astrorigin/pyswisseph（AGPL-3.0）**：在本项目中**只作研究参照与数据校验**（星历金标准对标）。
- **若做闭源商业产品：不得直接嵌入，须购买 Astrodienst 商业许可，或替换为其他实现（如自研历算或 MIT/BSD 许可的星历库）。** 论文研究使用不受此限（按 AGPL 与学术惯例引用）。

## 6. 现代版权材料的节录（数据集内，逐条可查）
- masters-dataset/modern-masters/ 全部条目：现代作品只存元数据 + 短节录 + 出处指针；逐条 license_status 与 redistributable 已在条目内标注（现代版权一律保守标 false，仅徐乐吾两例因著作权过期标 true）。现阶段内部使用全量；将来公开发布版按 redistributable 过滤导出。
- masters-dataset/chinese-natal/ 中韦千里（卒 1988）、倪海厦（卒 2012）材料：版权存续，条目标 redistributable=false，同上口径。
- Cheiro《Book of Numbers》（Internet Archive DLI 本）：许可存疑从严——仅作数字命理史料参照，不作再分发与商用素材。
- Celebrity50_zh.json（MirrorAI-Lab/BaZi-Persona）：该仓无 LICENSE 文件——仅作内部辅助验证参照，不再分发。
