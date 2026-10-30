#!/usr/bin/env python3
"""R39 §4.1 输入卫生剥离构建脚本（数据角）。

自 inputs-dev11 全量复制生成 inputs-dev12，仅对 INPUT-HYGIENE-SCAN.md
强命中 15 卡的 20 个命名字段作原文文本级替换（旧值在文件内恰出现 1 次
才许替换），其余字节逐字不变。弱命中 25 卡一律不动。
本脚本不写 BUILD-MANIFEST.md（由数据角另行落盘）与 STRIP-LOG.md。
"""
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]  # benchmark/phase3/
SRC = ROOT / "inputs-dev11"
DST = ROOT / "inputs-dev12"

URL_PLACEHOLDER = "（链接略，标题含断语已剥离）"

# (card_id, field_path, form, old, new)
STRIPS = [
    ("AS-304", "provenance.book", "F1",
     "其X（推特）账号原文，后经 Timesnownews 报道引录 https://www.timesnownews.com/viral/what-happened-to-the-astrologer-who-predicted-kamala-harris-would-win-the-us-elections-become-the-first-brahmin-woman-president-with-306-seats-article-115083422",
     "其X（推特）账号原文，后经 Timesnownews 报道引录（链接略，标题含断语已剥离）"),
    ("AS-304", "provenance.url", "F1",
     "https://www.timesnownews.com/viral/what-happened-to-the-astrologer-who-predicted-kamala-harris-would-win-the-us-elections-become-the-first-brahmin-woman-president-with-306-seats-article-115083422",
     URL_PLACEHOLDER),
    ("AS-306", "provenance.book", "F1",
     "其YouTube视频（2024-06-02）；PRWeb 2024-11通稿 https://www.prweb.com/releases/trump-will-be-crowned---indian-origin-us-based-astrologer-predicted-this-in-june-2024-302299787.html",
     "其YouTube视频（2024-06-02）；PRWeb 2024-11通稿（链接略，标题含断语已剥离）"),
    ("WP-002", "provenance.url", "F1",
     "https://twt-assets.washtimes.com/news/2008/may/20/its-in-the-stars-for-obama-4575-5/",
     URL_PLACEHOLDER),
    ("WP-003", "provenance.work", "F1",
     "Astrology News Service, 'Panel of Astrologers Predicts Obama Victory', May 2012 (New Orleans)",
     "Astrology News Service, news report, May 2012 (New Orleans)"),
    ("WP-003", "provenance.url", "F1",
     "https://astrologynewsservice.com/news/panel-of-astrologers-predicts-obama-victory/",
     URL_PLACEHOLDER),
    ("WP-006", "provenance.work", "F1",
     "Jessica Adams, 'How Astrology Predicts a Brexit', jessicaadams.com, 22 February 2016 (referencing her 5 July 2015 'GOODBYE EU' post)",
     "Jessica Adams, blog post, jessicaadams.com, 22 February 2016 (referencing her 5 July 2015 post)"),
    ("WP-006", "provenance.url", "F1",
     "https://stg.jessicaadams.com/2016/02/22/how-astrology-predicts-a-brexit/",
     URL_PLACEHOLDER),
    ("WP-007", "provenance.url", "F1",
     "https://thetab.com/us/2016/08/26/new-york-psychic-predicted-trump-winning-election-50290",
     URL_PLACEHOLDER),
    ("WP-008", "provenance.work", "F1",
     "ANI via Business Standard, 'LS polls: Odds in PM Modi's favour, say clairvoyants', 30 March 2019",
     "ANI via Business Standard, news report, 30 March 2019"),
    ("WP-008", "provenance.url", "F1",
     "https://www.business-standard.com/amp/article/news-ani/ls-polls-odds-in-pm-modi-s-favour-say-clairvoyants-119033000747_1.html",
     URL_PLACEHOLDER),
    ("WP-009", "provenance.url", "F1",
     "https://sportzwiki.com/cricket/icc-cricket-world-cup-2019-team-india-wont-win-the-tournament-says-famous-astrologer-greenstone-lobo/",
     URL_PLACEHOLDER),
    ("WP-012", "provenance.url", "F1",
     "https://www.israelhayom.com/2020/11/02/the-us-will-fall-apart-mystics-weigh-in-on-2020-presidential-election/",
     URL_PLACEHOLDER),
    ("WP-013", "provenance.page", "F2",
     "Roundup items 7 (Labour Wins the 2024 UK Election)",
     "Roundup items 7"),
    ("BZ-301", "context.setting", "F3",
     "2011年，李居明公开预言民国111年（2022年）国民党走向灭亡阶段；当时国民党正值马英九执政、无明显存亡危机",
     "2011年，李居明就民国111年（2022年）国民党未来走向作出公开预言；当时国民党正值马英九执政、无明显存亡危机"),
    ("ZY-003", "context.setting", "F3",
     "穆姜（魯宣公夫人）與叔孫僑如謀亂事敗，被遷於東宮軟禁；始往而筮之，問能否速出。占史斷「必速出」，穆姜自斷相反——本例金標以穆姜自斷為準，史官之斷同錄於 predictions 第二條供對照",
     "穆姜（魯宣公夫人）與叔孫僑如謀亂事敗，被遷於東宮軟禁；始往而筮之，問能否速出。"),
    ("LY-506", "context.setting", "F3",
     "初占母病，斷語轉指初生子有災；八月子驚風後再占子病",
     "初占母病，其後再占子病"),
    ("BZ-016", "context.setting", "F4",
     "清雍正帝第四子弘历，生于王府，断时（任氏注书时）其后来为帝之事于命例语境中作为已知贵造引用——注意：此例为事后引用型成例，盲测时只能给四柱与时代背景，不得给身份",
     "清雍正帝第四子弘历，生于王府，任氏注书时引此命造为例"),
    ("AS-015", "context.asked_at", "F5",
     "Not stated in the text (the death Lilly timed from the figure fell on 8 October following)",
     "Not stated in the text"),
    ("AS-015", "context.attachments.note", "F5",
     "Positions partly garbled in the 1647 OCR; the husband's significator being wholly unafflicted and the timing of the wife's death are the two points Lilly states unambiguously.",
     "Positions partly garbled in the 1647 OCR; the husband's significator being wholly unafflicted is one of the points Lilly states unambiguously."),
]


def get_path(obj, path):
    cur = obj
    for key in path.split("."):
        cur = cur[key]
    return cur


def main():
    if DST.exists():
        print(f"ABORT: {DST} already exists", file=sys.stderr)
        return 1
    src_jsons = sorted(SRC.glob("*.json"))
    assert len(src_jsons) == 487, f"src json count {len(src_jsons)} != 487"

    # Pre-flight: every old value must equal the parsed field value in dev11.
    for cid, path, _form, old, _new in STRIPS:
        data = json.loads((SRC / f"{cid}.json").read_text(encoding="utf-8"))
        actual = get_path(data, path)
        assert actual == old, f"{cid} {path}: parsed value != declared old\n  parsed: {actual!r}\n  old:    {old!r}"
    print(f"pre-flight OK: {len(STRIPS)} fields match parsed dev11 values")

    # Full copy (cards byte-for-byte; manifest handled separately by author).
    DST.mkdir(parents=True)
    for p in sorted(SRC.iterdir()):
        if p.suffix == ".json":
            shutil.copyfile(p, DST / p.name)
    print(f"copied {len(list(DST.glob('*.json')))} json cards")

    # Text-level replacement: old raw string must occur exactly once per file
    # occurrence step (AS-304 book/url share the URL substring: book first,
    # which removes the standalone url field's copy is NOT affected because
    # the url field is a separate JSON string containing the same URL text;
    # after book replacement the URL still occurs exactly once (in url field).
    by_card = {}
    for cid, path, form, old, new in STRIPS:
        by_card.setdefault(cid, []).append((path, form, old, new))
    for cid, items in by_card.items():
        fpath = DST / f"{cid}.json"
        text = fpath.read_text(encoding="utf-8")
        for path, form, old, new in items:
            n = text.count(old)
            assert n == 1, f"{cid} {path}: old occurs {n} times (need 1)"
            text = text.replace(old, new, 1)
        fpath.write_text(text, encoding="utf-8")
        # Post-check: parsed new values equal declared news.
        data = json.loads(text)
        for path, form, old, new in items:
            assert get_path(data, path) == new, f"{cid} {path}: parsed new mismatch"
        print(f"stripped {cid}: {len(items)} field(s)")
    print(f"DONE: {len(by_card)} cards, {len(STRIPS)} fields")
    return 0


if __name__ == "__main__":
    sys.exit(main())
