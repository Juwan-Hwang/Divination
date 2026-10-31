import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round66/predictions"
os.makedirs(OUT, exist_ok=True)

preds = {
"BZ-303": {
  "case_id": "BZ-303",
  "prediction_text": (
    "方向：先撑后转，至2024年由旺转衰，楼市负面收束。近段2016-2021年仍在下元八运期内，艮土当令，地产得土运之气，香港楼价高位总体向上、不主崩盘；"
    "2022-2023年八运退气，升势收窄、高位反复、成交转弱。主转折在2024年进入九运：艮土退位、离火当令，楼市失去地运主托，出现明显下行调整（峰值已过、价格中枢下移），"
    "香港经济亦随地产退潮而放缓，相对利火属的科技、网络、文化娱乐一类行业（此为倾向表述）。应期（年档，先定年）：转折窗口2023-2024年，主坐标2024年；"
    "依据为三元九运以2004-2023年为八运、2024-2043年为九运的运界。置信分层：转运与楼市转弱方向为中置信，具体跌幅不报（无坐向与盘面数据）。"
  ),
  "basis": (
    "tradition: fengshui; systems_used: [三元九运地运, 流年干支五行]\n"
    "输入残损：卡面仅载对象（香港整体运势与房地产市场）、问时2016年、问题期限至2024年与当时楼价上行背景；无香港或建筑坐向、无玄空飞星盘、无具体楼价/经济数值，冻结快照亦无风水专章（仅 chinese-bazi-ziwei.md 附节作定位、且载明本库不出风水断语），故只能按地运运程层作断、不能落坐向级断语，置信据此下调，不臆补盘面。\n"
    "推断路径：本题应验跨度定为年档（地运以二十年一运计，问题本身跨2016-2024年）。八运（2004-2023）艮属土、土主地产建筑，当令期内地产为地运所托，故近段断高位向上；运末退气则升势收窄；2024年交九运离火，土气退位为翻转触发，远段（以2024年为段界）转下行。近段与远段各有其运星依据，非由近段外推。承受对象与应验对象同一：均为香港楼市/香港整体经济。\n"
    "R61-REV1 应期复推-初推：以三元九运运界推，主坐标2024年（八运终、九运始）。\n"
    "R61-REV1 应期复推-复推：以当令旺星退气/入运复推，八白艮土星退气、九紫离火星当令同在2024年，坐标与初推一致。\n"
    "R61-REV1 应期复推-处置：二路同点，保留年档单点主坐标2024年，窗口2023-2024年，未取中之路不并陈为第二主坐标。\n"
    "R61-REV1 断项粒度核：楼市2024年转下行断项，细节类型=状态类别，支撑指针2条（运界切换、旺星退气/当令交替）指向同一落点，按原粒度保留；火属行业相对转旺断项，支撑指针仅1条（离火当令），已降为倾向表述；跌幅数量无指针，已删去不报。"
  ),
  "confidence": 0.42,
  "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
},
"BZ-304": {
  "case_id": "BZ-304",
  "prediction_text": (
    "方向：2020庚子年内不结束（负面）；近段急升、夏缓、冬再起。近段2020年3-4月，庚子年金水相生、水主流行传播，新加坡病例继续上升、管制趋向升级至接近全面阻断的等级，全球扩散同步扩大；"
    "主缓解坐标在2020年6月前后（午月），新加坡本地传播转缓、管制可分段放松，但不是终结。远段2020年11-12月亥子水旺，全球再现一波高峰、边境与出行仍受限，疫情跨年拖入2021年才逐步受控，庚子年内不主清零收官。"
    "应期（年/月档，先年后月）：以2020年为年窗，分段主坐标为4月升级、6月转缓、11-12月再起（末项已放宽为相邻两月窗）；依据为庚子流年金水与巳午火月、亥子水月的旺衰交替。置信分层：年内不终结为中置信，月份坐标为低至中置信。"
  ),
  "basis": (
    "tradition: fengshui; systems_used: [流年干支五行(庚子年金水), 月令旺衰与冲合]\n"
    "输入残损：卡面仅载对象（新加坡及全球新冠疫情）、问时2020-03-12、当时新加坡病例上升且尚未实施阻断措施；无起局盘面、无新加坡方位/坐向数据、无病例数值，冻结快照亦无风水专章（仅 chinese-bazi-ziwei.md 附节作定位），故只能按流年与月令层作断，置信据此下调，不臆补盘面。\n"
    "推断路径：本题应验跨度定为年档（问庚子年走势），年内分段以月档落坐标。庚金为肺金、水主流动传播，金生水则疫气在2020年得流年生扶、年内不断。近段（3-4月）金水余势加春季扩散，断上升与管制趋升；远段触发为亥子月水旺再临与子年支伏临，故冬月再起、跨年不终，非由近段外推。承受对象与应验对象同一：均为新加坡本地疫情（全球面只作同步扩散与冬波背景）。\n"
    "R61-REV1 应期复推-初推：以五行旺衰推，午月火旺克金耗水得6月转缓，亥子月水旺得11-12月再起。\n"
    "R61-REV1 应期复推-复推：以干支冲合换机制复推，年支子逢午月子午冲主6月转折点，亥子会水主冬月水势复盛，坐标与初推一致。\n"
    "R61-REV1 应期复推-处置：二路同点，6月保留单月主坐标；冬波一路只支持月窗不支持单月，主坐标已降一档粒度为11-12月相邻两月窗，未并陈第二单点。\n"
    "R61-REV1 断项粒度核：6月转缓断项，细节类型=状态类别，支撑指针2条（火旺克金耗水、子午冲转折）指向同一落点，按原粒度保留；新加坡管制升级程度断项，支撑指针仅1条（庚子金水流年），已降为倾向表述（趋向升级至接近全面阻断）；具体病例数量无指针，已删去不报。"
  ),
  "confidence": 0.40,
  "trigger": {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
},
}

written = []
for cid, obj in preds.items():
    p = os.path.join(OUT, cid + ".json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    written.append(cid)

# assertions: read back only own outputs
assert set(written) == {"BZ-303", "BZ-304"}, written
total = 0
for cid in written:
    p = os.path.join(OUT, cid + ".json")
    data = json.load(open(p, encoding="utf-8"))
    assert set(data.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}, data.keys()
    assert data["case_id"] == cid
    assert isinstance(data["confidence"], (int, float)) and 0 <= data["confidence"] <= 1
    t = data["trigger"]
    assert set(t.keys()) == {"changed_main", "reserve_used", "disputed", "reason"}
    assert all(isinstance(t[k], bool) for k in ("changed_main", "reserve_used", "disputed"))
    assert isinstance(t["reason"], str)
    # basis must contain exactly one tradition/systems_used first-line marker group
    first = data["basis"].splitlines()[0]
    assert first.startswith("tradition: fengshui; systems_used:"), first
    assert data["basis"].count("systems_used") == 1, cid
    total += os.path.getsize(p)
print("written:", len(written), written)
print("total_bytes:", total)
