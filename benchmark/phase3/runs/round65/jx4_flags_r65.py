# -*- coding: utf-8 -*-
import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round65")
view = json.loads((base/"jx4_view_r65.json").read_text(encoding="utf-8"))
by_anon = {o["anon_id"]: o["outcome_record"] for o in view}
flags = [
 ("P3-c532f2f9","结局后段为卦理解释层混入（应期与财爻机制自解），非纯结局事实","應寅年者﹐寅年而實空。應午年發者﹐世爻而值年月﹐功名反覆而不久者﹐六沖之卦也。宦囊消索者﹐子水財爻絕於日也﹔"),
 ("P3-cc4ac5bf","结局尾句为回溯性自注（以事后申日补释三刑），属解释层混入","此乃少一字﹐得後來之申日補之﹐豈可謂少一字不成三刑耶"),
 ("P3-d067898c","结局后半为应期机制自解层，死期事实之外另附卦理解释","应戌月者世入墓之月也，亥日者，克冲之日也"),
 ("P3-e78fab97","结局后半混入断法通则（爻位定地通例），个案结局仅首句","又有以初爻爲內地﹐以五爻六爻爲邊缺。"),
 ("P3-eca434d4","结局后半为卦理推演解释层（世爻空亡、火局克世等），非结局事实本身","世爻正值岁旬空亡，又被年月日会成火局克世，且世爻绝于岁建，败于月建，衰于日建，故当终也。"),
 ("P3-f0086657","结局内含编者自注：年份 1443 系 1643 误印，属回溯性编注混入结局文本","about the 14. of July 1443 [sic — misprint for 1643] in Warwick-shire"),
 ("P3-fae8caaa","结局尾句为应验解释层（应合克世之释），卒年事实之外另附自解","乃應戌土逢合之年而克世也。"),
 ("P3-ff800f97","结局尾句为应期解释层（实破之日自解），且本例两占合载、死亡归属未明字","夫應於卯日者﹐乃實破之日也。"),
]
lines = ["# FLAGS-X4 — R65 评审席位 X4 旗标登记（只登记不改分）",""]
for anon, gist, quote in flags:
    outcome = by_anon[anon]
    assert quote in outcome, (anon, "QUOTE NOT VERBATIM IN OWN OUTCOME")
    lines.append(f"## {anon}")
    lines.append(f"- 旗标要旨：{gist}")
    lines.append(f"- 结局原文逐字摘录：「{quote}」")
    lines.append("")
(base/"judging/FLAGS-X4.md").write_text("\n".join(lines), encoding="utf-8")
print("flags verified & written:", len(flags))
