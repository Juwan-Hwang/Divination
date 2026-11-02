<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/lockup-horizontal-reverse.svg">
    <img src="assets/brand/lockup-horizontal.svg" alt="严肃占卜 · Divination" width="440">
  </picture>
</p>

<p align="center"><b>An AI divination Skill that sits the masters' own readings as its exam.</b><br>It won't tell you what you want to hear. It reads your question the way the masters' handbooks say to.</p>

<p align="center">
  <a href="#install-in-thirty-seconds">Install</a> ·
  <a href="#how-it-differs-from-other-ai-fortune-telling">Why it's different</a> ·
  <a href="#report-card">Report card</a> ·
  <a href="#what-it-can-read">What it can read</a> ·
  <a href="#limits">Limits</a>
</p>

<p align="center"><a href="README.md">简体中文</a> · English</p>

https://github.com/user-attachments/assets/f5a72afe-0343-4400-baae-1348c88003be

---

Most AI fortune-telling recites a few stock verses, then tells you whatever sounds nice.

Divination (严肃占卜, "serious divination") doesn't. We read dozens of masters' original books cover to cover — Liuyao, Da Liu Ren, BaZi, Zi Wei Dou Shu, Qi Men Dun Jia, character divination, dream divination; Xu Lewu, Wang Huying, Duan Jianye, Xu Quanren, Cai Minghong, and more — distilled **over 1,400 reading rules**, and packaged them as a Skill an AI can execute directly. Then we tested it on real cases the masters once read, with known outcomes and the answers sealed, until its readings matched theirs.

## Install in thirty seconds

**Claude Code**

```bash
git clone https://github.com/Juwan-Hwang/Divination.git
cp -r Divination/skill ~/.claude/skills/divination
```

Start a new session and just ask, for example:

> Cast a hexagram for me: should I take this offer?

**Claude.ai / other agents that support Skills**: zip the `skill/` folder and upload it, or have the agent read `skill/SKILL.md`.

Casting and card drawing use only the Python standard library, so there is nothing to install:

```bash
python3 skill/tools/cast_iching.py "Should I take this offer"   # three-coin I Ching cast
python3 skill/tools/draw_tarot.py 3                             # three-card tarot spread
```

The calendar libraries that BaZi, Zi Wei and astrology charts need (lunar-python, iztro, pyswisseph) are optional external dependencies; the Skill tells you when it needs one.

## How it differs from other AI fortune-telling

| | Typical AI fortune-telling | Divination |
|---|---|---|
| Where the cast comes from | The model "imagines" one | `secrets` cryptographic randomness: a real cast, raw result shown in full |
| Where the chart comes from | Stems and branches from memory | Deterministic calendar maths: the year turns at Lichun, months at solar terms, true solar time corrected |
| What a reading rests on | Spliced verses and pep talk | Every statement cites its source — a rule's chapter or a master's case ID; anything without one is marked "conjecture" |
| Rival schools | Pushed back on you: "Which school would you like?" | The reader decides from the situation and says in one line which method it used |
| Conclusion | Vague, or guaranteed to please | Direction + conditions + timing; when methods conflict, it lays out the split and says which it chose |
| Proof it's any good | None | Blind tests on sealed cases, rules frozen before the exam, negative results published as-is |

Every full reading has the same five parts: **raw result → method used → item-by-item reading (each with its basis) → leaning (direction, conditions, timing) → archive line**. No cast, no hexagram talk; no chart, no chart talk.

## Report card

How it was trained:

- **96 rounds** of blind-test iteration, **5,419** AI seats, **7.66 billion** tokens
- **1,361** historical cases with a master's original reading and a real outcome as exam questions
- Setter, answerer, grader, reviser and moderator are **five separate roles**; grading uses two graders plus an arbiter
- Rules are frozen before the exam and never changed after it; exam cases are sealed with SHA-256, and nobody sees the answers before the seal is opened

**How often it agrees with the masters** (v1, 41 sealed test cases, first opening):

| Metric | Result |
|---|---|
| Per-case agreement score | **71.1%** |
| Passed (≥ 4/6) | 27 / 41 |
| Agreement between the two graders | 92.7% (κ = 0.827) |
| Gap to the calibration set's last-three-round mean | 2.9 percentage points, no sign of overfitting |

We also tried something harder: not "does it sound like the masters" but "who is more accurate", scoring masters and Skill together against what really happened. The verdict: **it hasn't beaten the masters yet.** On clean samples the masters are right almost every time, and the Skill still trails clearly (Phase 2 holdout, low-contamination subset: 4.06 vs 5.35 out of 6). That result is in the report exactly as it came out; we didn't change the scoring to close the gap.

Full protocol, every round's data and the negative results: [`benchmark/PROTOCOL.md`](benchmark/PROTOCOL.md) · [`benchmark/iterations.md`](benchmark/iterations.md) · [`benchmark/phase2/FINAL-REPORT-v2.md`](benchmark/phase2/FINAL-REPORT-v2.md) (in Chinese)

## What it can read

Just say clearly what you want to ask. The Skill picks the method itself, and can cross-check several:

| You want to ask | First choice | Cross-check |
|---|---|---|
| Will a specific thing work out, and when | Liuyao (Najia) | Da Liu Ren (adds detail: who, which direction, how it unfolds) |
| A decision you have to make right now | Meihua Yishu (Plum Blossom) | I Ching |
| No specific matter, you want a direction | I Ching text reading | Tarot |
| Life pattern and luck cycles | BaZi | Zi Wei Dou Shu |
| When to act and in which direction | Qi Men Dun Jia | — |
| Relationships, state of mind, circumstances | Tarot | I Ching |
| A character or a dream at hand | Character divination, dream divination | Liuyao, Meihua |
| Birth chart and transits | Western astrology | BaZi (cross-system comparison) |

It only asks for facts (what the matter is, birth time and place) and never hands you a multiple choice between schools. It won't cast twice on the same matter, following the I Ching's hexagram Meng: "The first cast informs; asking again and again is importunate, and the importunate are not informed."

## Limits

Divination here is a cultural tradition and a framework for thinking through decisions, not a scientific forecasting tool. Recorded cases in the classics carry survivorship bias; passing the blind test shows its readings agree with the masters', not that they predict.

- Medical, legal, investment and personal-safety questions: reference only, always alongside real professional judgement
- It won't read a third party's private affairs for you, and won't talk about "changing your fate" or "breaking a curse"
- Modern constructions such as the attributed *Meihua Yishu* or Waite's card meanings are used as normal, but their provenance is labelled honestly rather than dressed up as ancient texts

## What's in the repo

| Path | Contents |
|---|---|
| [`skill/`](skill/) | **The installable Skill package** (SKILL.md + 14 knowledge-base files + casting and drawing tools) — this is the canonical version |
| [`benchmark/`](benchmark/) | Blind-test protocol, exam cases, every round's grading and evidence |
| [`masters-dataset/`](masters-dataset/) | Masters' case dataset (querent, context at the time, the master's original reading, the outcome) |
| [`docs/KNOWLEDGE-BASE.md`](docs/KNOWLEDGE-BASE.md) | Research knowledge base: principles, procedures and contents |
| [`MANIFEST.md`](MANIFEST.md) · [`LICENSES.md`](LICENSES.md) | Source list and licensing boundaries for all materials |

Most of the repo, including the Skill's knowledge base, is written in Chinese.

## License

Original content in this repo is released under [CC BY-NC-SA 4.0](LICENSE): free to use, with attribution, non-commercial, share-alike. Quoted classics, open-source libraries and datasets keep their own licenses, listed in [`LICENSES.md`](LICENSES.md).

<p align="center"><sub>A master's time is expensive; this Skill is free. It won't replace the masters, but it turns their handbooks into something any AI can follow.</sub></p>
