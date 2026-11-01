# 严肃占卜 · Divination — launch film

**60.0 s · 1920×1080 · 30 fps · H.264 High CRF 16 · AAC 256 kb/s 48 kHz · −14.0 LUFS integrated (true peak −1.1 dBTP EN, −1.5 dBTP ZH) · 120 BPM (bar = 2 s)**
Two cuts from one comp: [`deliver/divination-promo-en.mp4`](deliver/divination-promo-en.mp4) · [`deliver/divination-promo-zh.mp4`](deliver/divination-promo-zh.mp4)

**The message:** most AI fortune-telling tells you what you want to hear; this one sits the masters' exam, and publishes the grade, including the part where it still loses.
The Skill has no UI, so the film shows what is real about it: a real cast, a real sealed exam case, and the README's own numbers.

**The carry element** is the brand mark's cinnabar dot (`#B8361E`), the only cinnabar thing in the film. It blinks on the table, glows through a cash coin's square hole, becomes the typing caret (a red reading mark, 圈点), the terminal cursor, the pen that strikes out what other AI fortune-telling does (朱批), the hop that turns each moving line, the circle a grader draws round a full mark, the bullet, the full stop after 71.1%, the field the camera dives through, and the logo's dot again. Every cut hands it to the next scene.

## Storyboard

| t (s) | bars | scene | carry |
|---|---|---|---|
| 0–6 | 0–3 | **3D open.** The dot blinks three times on a dark table (0.25 / 1.0 / 1.75). On bar 1 three bronze 乾隆通寶 cash coins fall into frame, tumble and wobble flat like real coins: two 字 up, one 背 up, 2+2+3 = 7, 少阳, the first line of the real cast. The middle coin lands over the dot; the camera dives into its square hole. | dot → coin hole → full-frame cinnabar |
| 6–12 | 3–6 | Thesis. "Most AI fortune-tellers / tell you what you want to hear." The dot runs back along both lines and strikes them out. "This one sits the masters' exam." | field closes onto the caret; caret strikes; glides to the prompt |
| 12–16 | 6–8 | **The real cast** in a terminal: `python3 skill/tools/cast_iching.py "这次的 offer 该不该接"`, output verbatim; push in on the six lines. | terminal cursor |
| 16–20 | 8–10 | The six ━ glyphs lift out of the terminal into a large hexagram; the dot hops onto each moving line (上、五、二) on eighth notes and turns it: 中孚 → 复. | ring of each moving line |
| 20–26 | 10–13 | Most AI vs Divination, the README's table: the cast, the chart, every line. One row per bar; the dot strikes out the left side. | pen per row |
| 26–38 | 13–19 | **The exam.** Rain falls over sealed case LY-103 (test set, `test_gold.jsonl` sha256 `de6cbfd2…86a7d6`): Wang Huying's 测天气例一, "问当晚雨会不会停". The Skill's blind reading is typed (bar 15); the master's original is unsealed (bar 16); the judges' scores land on beats (bar 17), the rain stops, and the dot draws the grader's circle round 6/6. | caret of the blind reading → the circle |
| 38–42 | 19–21 | Eleven methods on eighth notes (六爻纳甲 … 西洋占星), then "1,400+ rules from the masters' own books" with five masters' names. | bullet |
| 42–48 | 21–24 | 96 rounds · 5,419 AI seats · 7.66B tokens · 1,361 cases (one per beat); then 71.1%, 41 sealed cases, κ = 0.827. | bullet → full stop after 71.1% |
| 48–52 | 24–26 | **The honest result.** "It hasn't beaten the masters yet." 4.06 vs 5.35 (low-contamination holdout). "We published it anyway." | caret → the dot between the scores |
| 52–54 | 26–27 | "The masters' manual, for every AI." The dot swells to fill the frame. | caret → field |
| 54–56.5 | 27–28.25 | **3D end.** From inside the dot the camera pulls back; the paper tile with 卜 cut through it swings in around its own dot and lands pixel-matched on the vector lockup. | 3D dot → vector dot |
| 56.5–60 | 28.25–30 | The repo's own horizontal reverse lockup; 严肃占卜 and DIVINATION wipe in from their outlines (never retyped in a font); URL and tag; fade. | logo dot |

## Copy (EN | ZH)

| key | EN | 中文 |
|---|---|---|
| thesis | Most AI fortune-tellers / tell you what you want to hear. | 大多数 AI 算命 / 只捡你爱听的说 |
| | This one sits the masters' exam. | 这一个，拿大师原断当考卷 |
| cast | A real cast. Three coins, six throws. — Randomness from Python's secrets module. The raw result, shown in full. | 真起卦：三钱六掷 — 随机只用 secrets 密码学随机，原始结果完整给你看 |
| hexagram | Moving lines turn. The hexagram changes. — Read by the book: the rule, the chapter, or the master's case it rests on. | 动爻一变，本卦化出变卦 — 每条断语都有出处：规则章节，或大师成例编号 |
| vs | Most AI / Divination; The cast: The model imagines one → Cryptographically random. A real cast. The chart: Pillars quoted from memory → Deterministic calendar, true solar time. Every line: Stock phrases and comfort → Cites its rule or case, or says it's a guess | 常见 AI 算命 / 严肃占卜；卦从哪来：模型自己「想」一个 → secrets 密码学随机，真起卦；盘从哪来：凭印象报干支 → 确定性历法，真太阳时校正；断语依据：口诀拼贴、心灵鸡汤 → 每条标出处，对不上的标「推测」 |
| exam | Then we made it sit the masters' exam. — 1,361 real cases. The master's reading and the outcome, sealed away. | 然后，让它考大师的卷 — 1,361 个历史案例，大师原断与真实结局一律封存 |
| | Answer sealed · Divination · blind reading · Wang Huying · original reading · Direction / Assertions / Outcome | 答案封存 · 严肃占卜 · 盲断 · 王虎应 · 原断 · 方向 / 断语 / 应验 |
| grade | Graded against the master: 6 out of 6. — The rain stopped that evening. The concert went on. | 对照大师原断：6 分满分 — 当晚雨停，音乐会如期举行 |
| methods | Liuyao · Da Liu Ren · Meihua · I Ching · Bazi · Zi Wei Dou Shu · Qimen Dunjia · Character reading · Dream reading · Tarot · Astrology | 六爻纳甲 · 大六壬 · 梅花易数 · 周易 · 八字 · 紫微斗数 · 奇门遁甲 · 测字 · 梦占 · 塔罗 · 西洋占星 |
| rules | 1,400+ rules from the masters' own books. — Xu Lewu · Wang Huying · Duan Jianye · Xu Quanren · Cai Minghong | 1,400 多条断法，出自大师原著 — 徐乐吾 · 王虎应 · 段建业 · 许铨仁 · 蔡明宏 |
| numbers | 96 rounds of blind tests · 5,419 AI seats · 7.66B tokens · 1,361 real cases, outcomes known | 96 轮盲测迭代 · 5,419 个 AI 席位 · 76.6 亿 token · 1,361 个结局已知的历史案例 |
| | 71.1% agreement with the masters, 41 sealed cases — Two judges, 92.7% in agreement · κ = 0.827 | 71.1% 41 例封存考题，与大师原断一致 — 双评审一致率 92.7% · κ = 0.827 |
| honest | It hasn't beaten the masters yet. 4.06 Divination / 5.35 The masters — Low-contamination holdout, out of 6. We published it anyway. | 它还没赢过大师 4.06 严肃占卜 / 5.35 大师 — 低污染留出集，满分 6 分。这个结果，我们照实写进了报告 |
| finale | The masters' manual, for every AI. | 把大师的手册，交给每一个 AI |
| tag | Free. Open source. A cultural tradition, not a science. | 免费开源 · 占卜是文化传统，不是科学预测 |

## What is real

- **The cast** (`session/cast.txt`): one real run of `skill/tools/cast_iching.py` at Divination@`5c70ae21`, 2026-11-02 03:40 CST, stdout verbatim: 中孚 之 复, moving lines 2, 5, 6. The 3D coins' landing (2+2+3 = 7) is that cast's first line.
- **The exam case**: LY-103 from the 41-case sealed test set, opened once in Round 18 (`benchmark/runs/round18/test-seal-log.md`). Question and background from `inputs/LY-103.json`; the Skill's blind reading is `predictions/LY-103.json`'s `summary`, verbatim; Wang Huying's words are the gold `statement_excerpt`, cut with "……" only; the scores 2/2/2 = 6/6 are `judging/judgeA-scores.jsonl`; the outcome is the book's own account ("果然应验", no weather record). The seal hash is `test_gold.jsonl`'s sha256, recorded in the KB-snapshot manifests since Round 10.
- **Every number** is the README's: 1,400+ rules, 96 rounds, 5,419 seats, 76.6 亿 tokens, 1,361 cases, 71.1% on 41 sealed cases, κ 0.827, 92.7%, and the Phase 2 low-contamination 4.06 vs 5.35 (`benchmark/phase2/FINAL-REPORT-v2.md`).
- **Brand**: the repo's own `assets/brand/lockup-horizontal-reverse.svg` (the 3D tile is extruded from the same 卜 path and dot); ink `#1B1712`, paper `#ECE5D3`, cinnabar `#B8361E`.
- Data stays verbatim in both cuts: the terminal, hexagram names and the exam texts are Chinese in the EN cut too (`lint_copy.py` flags them; that is deliberate).

## How it was made

`film/comp.html` is the whole film as one seekable timeline (`__seek(t)` is a pure function of t; `__events()` feeds the sound). `film/o3d.html` holds the two three.js r170 shots, rendered offline by `r3d_seq.py` with a 3-sample linear-light shutter. `render_film.py` renders the comp frame by frame with adaptive motion blur. `music.py` is an original numpy score (D minor, pentatonic melody layer, bells on the coins, moving lines, the grader's circle and the lockup, a rain bed over the sealed case); `sound.py` places earshot SFX (@`925ebe5`) peak-aligned on the comp's events; `encode.sh` does a two-pass loudnorm. Fonts: Noto Serif SC + Source Serif 4 for copy, Noto Sans Mono CJK SC for the terminal.

## Rebuild

```sh
cd promo/film && sh reproduce.sh          # both cuts → deliver/divination-promo-{en,zh}.rebuild.mp4
LANGS=zh sh reproduce.sh                  # one cut
python3 -m http.server 8777 --directory film   # then comp.html?lang=zh&t=35.6&hud for any moment
```
Versions and seeds are pinned (`requirements.txt`, `fonts.sha256`, rng 7 / 11 / 3); a different Chromium build may move edge pixels, never content or timing.
