# -*- coding: utf-8 -*-
import json, glob, collections, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dat_findings import NEW_GIST, NEW_CASES

base='/home/hatch/workspace/divination/benchmark/phase3'
jd=f'{base}/runs/round64/judging'

# ---------- load ----------
r63=json.load(open(f'{base}/data/case-annotations-r63.json'))
man64=json.load(open(f'{jd}/outcome-manifest.json'))
man63=json.load(open(f'{base}/runs/round63/judging/outcome-manifest.json'))
hm=json.load(open(f'{jd}/host-mapping.json'))

# prior annotations by case: list of (round, entry)
prior=collections.defaultdict(list)
prior_files={}
for f in sorted(glob.glob(f'{base}/data/case-annotations-*.json')):
    d=json.load(open(f)); rnd=int(re.search(r'r(\d+)\.json', f).group(1))
    if rnd>=64: continue  # 排除本轮产出自身，防重跑自嵌套污染
    prior_files[rnd]=f'benchmark/phase3/data/case-annotations-r{rnd}.json'
    for a in d['annotations']: prior[a['case_id']].append((rnd,a))

# ---------- TASK 1: addendum ----------
part=[a for a in r63['annotations'] if a['disposition']=='部分成立']
assert len(part)==72, len(part)
assert r63['counts']['verdicts']=={'成立':12,'部分成立':72,'不成立':2,'未核':1}
add=man64['_r64_carryover_notes_addendum']
assert len(add)==72
mismatch=[a['case_id'] for a in part if add.get(a['case_id'])!=a['manifest_carry_suggestion']]
assert not mismatch, mismatch
assert set(add)=={a['case_id'] for a in part}
nonpart={d:[a['case_id'] for a in r63['annotations'] if a['disposition']==d] for d in ('成立','不成立','未核')}

L=[]
L.append('# Manifest 承接册附则（R64）——R63 定案承接建议汇编')
L.append('')
L.append('## 卷首说明')
L.append('')
L.append('- 本附则为 Phase 3 Round 64（R64）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r63.json`（R63 定案正本：annotations 87 件，定案分布成立 12／部分成立 72／不成立 2／未核 1）。')
L.append('- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 12／部分成立 72／不成立 2／未核 1、总 87，与 R63 公布分布逐项一致；部分成立 72 件每件 `manifest_carry_suggestion` 非空断言亦通过。')
L.append('- 对勘结果：72/72 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round64/judging/outcome-manifest.json` 的 `_r64_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件）。')
L.append('- **本附则自 R65 manifest 起落实**；本轮（R64）manifest 不据本附则改动。')
L.append('- **本件只汇编与对勘，不改任何分数与结局原文。**')
L.append('- 汇编范围：R63 定案中部分成立 72 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r63.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R64 起」等表述为原档原文，落实轮次按卷首上一条读作自 R65 起，不回溯改动 R64）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。')
L.append('- 成立 12／不成立 2／未核 1 共 15 件不入正文逐件节，只在文末列 case_id 清单。')
L.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。')
L.append('')
L.append('---')
L.append('')
L.append('## 一、部分成立件承接汇编（定案档位：部分成立，72 件，逐件全列）')
L.append('')
for i,a in enumerate(part,1):
    assert a['manifest_carry_suggestion']
    L.append(f'### A{i}. {a["case_id"]}')
    L.append('')
    L.append(f'- case_id：{a["case_id"]}')
    L.append(f'- anon_id：{a["anon_id"]}')
    L.append(f'- 定案（部分成立）：{a["finding"]}')
    L.append(f'- 原旗标要旨（照原档 `flag` 字段）：{a["flag"]}')
    L.append(f'- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a["manifest_carry_suggestion"]}」')
    L.append(f'- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a["relation"]}')
    L.append('')
L.append('---')
L.append('')
L.append('## 对勘记录')
L.append('')
L.append('- 对勘对象：本汇编第一节 72 件承接注记建议文本（源：`case-annotations-r63.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round64/judging/outcome-manifest.json` 的 `_r64_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。')
detail='、'.join(f'{a["case_id"]}＝一致' for a in part)
L.append(f'- 对勘结果：72 件逐字一致，差异 0 件（对勘明细：{detail}）。')
L.append('- 键集合差异：无（manifest 层 72 键与部分成立 72 件 case_id 集合全等）。')
L.append('- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R65 manifest 起落实。')
L.append('')
L.append('---')
L.append('')
L.append('## 自验')
L.append('')
L.append('- 原档（case-annotations-r63.json）条目数：87；档位分布成立 12／部分成立 72／不成立 2／未核 1，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。')
L.append('- 本附则正文条目数：72（第一节部分成立 72 件），与原档部分成立件数对齐；文末不入附则清单 15 件（成立 12＋不成立 2＋未核 1），72＋15＝87 与原档总数对齐。')
L.append('- 承接注记建议文本：72 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R64 manifest `_r64_carryover_notes_addendum` 逐件逐字一致（72／72）。')
L.append('- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝72、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。')
L.append('- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r64_carryover_notes_addendum` 层与 `cases` 键名集。')
L.append('')
L.append('---')
L.append('')
L.append('## 文末清单：不入附则 15 件（成立 12＋不成立 2＋未核 1，仅列 case_id）')
L.append('')
for d in ('成立','不成立','未核'):
    L.append(f'### {d} {len(nonpart[d])} 件')
    L.append('')
    for cid in nonpart[d]: L.append(f'- {cid}')
    L.append('')
addendum='\n'.join(L)
out1=f'{base}/data/manifest-carryover-r64-addendum.md'
open(out1,'w').write(addendum)
# 回读断言
back=open(out1).read()
assert back.count('### A')==72 or back.count('\n### A')==72, back.count('### A')
sec=back.split('## 一、')[1].split('## 对勘记录')[0]
assert sec.count('### A')==72
for a in part:
    assert f'「{a["manifest_carry_suggestion"]}」' in back, a['case_id']
print('TASK1 OK', out1, os.path.getsize(out1))

# ---------- TASK 2: annotations r64 ----------
txt=open(f'{jd}/FLAGS-selfreported-r64.md').read()
cur=None; compiled=collections.OrderedDict()
for l in txt.splitlines():
    m=re.match(r'## (X[1-4]|Y[1-4])（(\d+) 条）', l)
    if m: cur=m.group(1)
    m2=re.match(r'- (P3-[0-9a-f]+)：(.*)', l)
    if m2 and cur: compiled.setdefault(m2.group(1), []).append((cur, m2.group(2)))
assert sum(len(v) for v in compiled.values())==212
assert len(compiled)==129
# raw files cross-check (exact filenames only)
rawmap={}
for s in ['X1','X2','X3','X4','Y1','Y2','Y3','Y4']:
    for l in open(f'{jd}/FLAGS-{s}.md'):
        m2=re.match(r'- (P3-[0-9a-f]+)：(.*)', l.strip())
        if m2: rawmap.setdefault(m2.group(1), []).append((s, m2.group(2)))
assert rawmap.keys()==compiled.keys()
for a in compiled:
    assert sorted(rawmap[a])==sorted(compiled[a]), a
# outcome equality r63->r64 for flagged
for a in compiled:
    cid=hm[a]
    assert man64['cases'][cid]==man63['cases'][cid], cid

SEAT_ORDER=['X1','X2','X3','X4','Y1','Y2','Y3','Y4']
def flag_str(fl):
    fl=sorted(fl, key=lambda x: SEAT_ORDER.index(x[0]))
    return '；'.join(f'{s}：{t}' for s,t in fl)
def rounds_str(rounds):
    return '／'.join(f'R{r}' for r in rounds)

annotations=[]; flags_list=[]
cnt=collections.Counter(); rel_cnt=collections.Counter()
for anon, fl in compiled.items():
    cid=hm[anon]
    fl_sorted=sorted(fl, key=lambda x: SEAT_ORDER.index(x[0]))
    seats=[s for s,_ in fl_sorted]
    flag=flag_str(fl)
    hist=prior.get(cid, [])
    hist_disp=[(r,a) for r,a in hist if a.get('disposition') and a.get('finding')]
    sources=[f'benchmark/phase3/inputs-dev12/{cid}.json',
             'benchmark/phase3/runs/round64/judging/FLAGS-selfreported-r64.md',
             f'benchmark/phase3/runs/round64/judging/outcome-manifest.json cases[{cid}]',
             f'benchmark/phase3/runs/round64/predictions/{cid}.json']
    for r,a in hist:
        sources.append(f'{prior_files[r]} {cid} 条')
    views=sorted({s[0] for s in seats})
    if cid in NEW_CASES:
        finding, gist, category = NEW_CASES[cid]
        relation='新旗标（R64 新立）'; rel_key='new'
        disp = '不成立' if finding.rstrip().endswith('故不成立。') or '故不成立' in finding[-12:] else '部分成立'
        # determine disp explicitly: 不成立 findings end with 故不成立。
        disp = '不成立' if finding.strip().endswith('故不成立。') else '部分成立'
        if cid=='LY-021': disp='不成立'  # finding 结尾为「故不成立（同 LY-627 口径）。」
        if disp=='部分成立':
            sugg=f'同旨新立：自 R65 起承接本 R64 标注：按「{gist}」登记；结局原文照录不改。'
        else:
            sugg=f'不入附则：本 R64 新立定案不成立（{category}），不加承接注记；结局原文照录不改。'
    elif cid in NEW_GIST:
        finding, gist, category = NEW_GIST[cid]
        latest_r, latest_a = hist_disp[-1]
        if cid=='LY-211': relation='同例新旨（R61 旧旨旗标成立、本轮新旨另立）'
        elif cid=='LY-228': relation='同例新旨（R61 旧旨旗标成立、本轮新旨另立）'
        elif cid=='LY-237': relation='同例新旨（R61 旧旨旗标成立、本轮新旨另立）'
        elif cid=='LY-216': relation='同例新旨（R63 续旨旗标部分成立、本轮新旨另立）'
        elif cid=='LY-215': relation='同例新旨（R56 旧旨旗标不成立、本轮新旨另立）'
        elif cid=='BZ-029': relation='同例新旨（R55 卒年待核未核、本轮旗标另旨登记不裁）'
        rel_key='newgist'
        if cid=='BZ-029':
            disp='未核'
            sugg='待核维持（线索登记）：自 R65 起承接 R55 待核登记＋本 R64 错配线索登记：俞大维卒年（1983／1993）无盘外独立史源前不裁；本轮 Y1 旗标所述内容经核属 LY-531、先登记后核；结局原文照录不改。'
        elif cid=='LY-215':
            disp='不成立'
            sugg='不入附则：本 R64 新旨定案不成立（旗标问面错置、趋避实况已经 R56 裁定），不加承接注记；结局原文照录不改。'
        else:
            disp='部分成立'
            sugg=f'同例新旨：自 R65 起承接本 R64 标注（与历轮旧旨定案并行、各旨独立）：按「{gist}」登记；结局原文照录不改。'
    else:
        latest_r, latest_a = hist_disp[-1]
        disp=latest_a['disposition']
        relation=f'同旨续接（R{latest_r}）'; rel_key='cont'
        finding=(f'承接既有定案不重裁（历轮最近定案 R{latest_r} {disp}）：{latest_a["finding"]} '
                 f'本轮（R64）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。')
        if cid=='LY-025':
            finding=(f'承接既有定案不重裁（历轮最近定案 R63 部分成立）：{latest_a["finding"]} '
                     f'本轮（R64）manifest 该例结局与历轮所核文本一致；本轮 X3 所指 carry 口径一层与 R63 新旨同旨、Y3 所指终局 negative 模板错位一层与 R61／R62 旧旨同旨（逐字核 R64 prediction_text，首句自载「终局单判 negative」），两旨均已经定案部分成立，本轮并行承接、不重裁。')
        if cid=='LR2-024':
            finding+=f' 本轮 X4 所指「七月死期为本课结局」含编述措辞一层，已在 R58 层定案（「为本课结局」为编述式措辞、含混一层属实）内同旨承接。'
        if cid=='YM-070':
            finding=(f'承接既有定案不重裁（历轮最近定案 R63 未核）：{latest_a["finding"]} '
                     f'本轮（R64）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。')
            sugg=('挂起维持（注记合并）：自 R65 起承接 R51＋R55＋R56＋R57＋R58＋R59＋R60＋R61＋R62＋R63＋本 R64 登记：按「结局措辞待核（『都下』语义未明）」与卡面 asked_at「甲寅旬」出处待核两项合并登记、并列承接；结局原文照录不改、不补字；无盘外独立史源前不另裁。')
            annotations.append({'anon_id':anon,'case_id':cid,'disposition':disp,'finding':finding,'flag':flag,
                'manifest_carry_suggestion':sugg,'relation':relation,'registered_round':64,
                'sources_checked':sources,'source_seats':seats})
            flags_list.append({'anon_id':anon,'case_id':cid,'verdict':disp,'disposition':disp,'basis':finding,
                'carry_suggestion':sugg,'manifest_carry_suggestion':sugg,'flag':flag,'category':'同旨续接（详见核查事实）',
                'views':views,'dual_view':len(views)==2,'relation':relation,'registered_round':64,'sources_checked':sources})
            cnt[disp]+=1; rel_cnt[rel_key]+=1
            continue
        if cid=='LY-537':
            sugg=('待核维持：自 R65 起承接 R56／R57／R61＋本 R64 登记：按「结局『果于申予日归』措辞待核、日期干支不明」登记；无盘外独立史源（原书页文本）前不裁；结局原文照录不改。')
            annotations.append({'anon_id':anon,'case_id':cid,'disposition':disp,'finding':finding,'flag':flag,
                'manifest_carry_suggestion':sugg,'relation':relation,'registered_round':64,
                'sources_checked':sources,'source_seats':seats})
            flags_list.append({'anon_id':anon,'case_id':cid,'verdict':disp,'disposition':disp,'basis':finding,
                'carry_suggestion':sugg,'manifest_carry_suggestion':sugg,'flag':flag,'category':'同旨续接（详见核查事实）',
                'views':views,'dual_view':len(views)==2,'relation':relation,'registered_round':64,'sources_checked':sources})
            cnt[disp]+=1; rel_cnt[rel_key]+=1
            continue
        rounds=[r for r,a in hist_disp]
        if disp=='不成立':
            sugg=f'不入附则：承既有定案（R{latest_r} 不成立）口径，自 R65 起承接本 R64 标注，不加承接注记；结局原文照录不改。'
        else:
            sugg=f'同旨续接：自 R65 起承接 {rounds_str(rounds)}＋本 R64 标注；结局原文照录不改。'
        category='同旨续接（详见核查事实）'
        annotations.append({'anon_id':anon,'case_id':cid,'disposition':disp,'finding':finding,'flag':flag,
            'manifest_carry_suggestion':sugg,'relation':relation,'registered_round':64,
            'sources_checked':sources,'source_seats':seats})
        flags_list.append({'anon_id':anon,'case_id':cid,'verdict':disp,'disposition':disp,'basis':finding,
            'carry_suggestion':sugg,'manifest_carry_suggestion':sugg,'flag':flag,'category':category,
            'views':views,'dual_view':len(views)==2,'relation':relation,'registered_round':64,'sources_checked':sources})
        cnt[disp]+=1; rel_cnt[rel_key]+=1
        continue
    # new / newgist path
    category = NEW_CASES.get(cid, NEW_GIST.get(cid))[2]
    annotations.append({'anon_id':anon,'case_id':cid,'disposition':disp,'finding':finding,'flag':flag,
        'manifest_carry_suggestion':sugg,'relation':relation,'registered_round':64,
        'sources_checked':sources,'source_seats':seats})
    flags_list.append({'anon_id':anon,'case_id':cid,'verdict':disp,'disposition':disp,'basis':finding,
        'carry_suggestion':sugg,'manifest_carry_suggestion':sugg,'flag':flag,'category':category,
        'views':views,'dual_view':len(views)==2,'relation':relation,'registered_round':64,'sources_checked':sources})
    cnt[disp]+=1; rel_cnt[rel_key]+=1

counts={'selfreport_anons_total':129,'cases_total':129,
        'continuation_cases':rel_cnt['cont'],'same_case_new_gist_cases':rel_cnt['newgist'],'new_flag_cases':rel_cnt['new'],
        'verdicts':{'成立':cnt['成立'],'部分成立':cnt['部分成立'],'不成立':cnt['不成立'],'未核':cnt['未核']}}
print('COUNTS', counts)
assert counts['continuation_cases']+counts['same_case_new_gist_cases']+counts['new_flag_cases']==129
assert sum(counts['verdicts'].values())==129
for a in annotations:
    if a['disposition']=='部分成立': assert a['manifest_carry_suggestion'], a['case_id']

special=[
 {'item':'特别核查①：待核维持件（BZ-029／BZ-040／LY-537）状态登记',
  'conclusion':'BZ-040 本轮未出现在旗标中，不在本件范围、维持 R55 原登记（许世英享年：结局作 1964 年卒年 71、通行史实异说待盘外独立史源），不另裁、不虚构条目。BZ-029 出现在本轮旗标中（P3-0fe6c7e3，Y1 单席），但旗标所述内容经逐字核与本例原卡／结局全不对应、实属 LY-531 结局内容（详见特别核查④），已按线索先登记后核处理；BZ-029 本件待核事项（俞大维卒年 1983／1993）本轮无盘外独立史源，disposition 照 R55 给未核、不新裁，与待核维持口径一致。LY-537 出现在本轮旗标中（P3-d2689059，X4 单席），所指与 R56／R57／R61 未核登记同旨，已照实核、承接既有定案给未核，与待核维持登记并行不悖。',
  'evidence':'BZ-029：R64 结局『史实：俞大维官至国防部长、交通部长，为技术官僚重臣；1983年卒于台北（后移灵大陆）』无旗标所述『仆／午月／过害』字样；LY-537：R64 结局『果于申予日归』与历轮所核一致、原卡仅载占时『未月戊申日』、无归日原文可对勘；BZ-040：其 R64 anon 不在本轮 129 件旗标 anon 集内（据 runs/round64/judging/host-mapping.json 与 FLAGS-selfreported-r64.md 逐件比对）。',
  'scope_note':'本核查只登记状态，不改分数、不改 manifest；待核口径照旧。'},
 {'item':'特别核查②：YM-070「甲寅旬」挂起维持与本轮旗标的关系',
  'conclusion':'YM-070 出现在本轮旗标中（P3-c1368238，X4／Y4 同报『都下』语义未明），已照实核、承接既有定案给 disposition 为未核（挂起），与挂起维持口径一致、无差异；本轮旗标仅及结局『都下』语义一层，asked_at『甲寅旬』出处待核项并存合并登记，两项并行不悖，本件不新裁。',
  'evidence':'YM-070：R64 manifest 结局「后果同行都下。」与历轮所核一致；『甲寅旬』待核承 R53 定案档（底本原页日期只作「卯建丙辰日」、三字原页无据）。',
  'scope_note':'本核查只登记关系，不改分数、不改 manifest；挂起口径照旧。'},
 {'item':'特别核查③：结局文本内嵌指令性字样之例——按数据处理登记',
  'conclusion':'本轮旗标所涉指令性字样出处共三处，均只按数据处理、未服从：(1) LR2-016 编者注（manifest `_r56_lr2016_split`.editor_note：『评分时该细项请按未完全复核处理』），原为结局文本内嵌句、R56 已分列登记；本轮 X1／Y1 两席旗标与本席均仅登记『甲戌日巳时』细项未完全复核之事实，未服从其评分指示、未作量表外加减分。(2) BZ-036 结局自注『盲测比对须注』、(3) BZ-042 结局自注『（盲测比对时以格局大富一项为主）』，同属结局文本内嵌的比对指示字样；本轮各席旗标仅登记其事实层（年数出入／来源未备）、本席亦按数据处理，未据以另设比对口径。本席另以关键词（请按／须注／评分时／比对时等）全量扫 R64 manifest 全部 487 例结局，除上述 BZ-036／BZ-042 两处外无其他指令性字样（LR2-016 之句已分列于 editor_note、不在 cases 本体）。',
  'evidence':'LR2-016：R64 cases 本体仅『众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。』，指令性字样只存于分列的 editor_note 一处；BZ-036 结局作『……此年数有出入，盲测比对须注』，BZ-042 结局作『……待另核（盲测比对时以格局大富一项为主）』，两件本轮定案均只就其事实层承接既有部分成立档位。',
  'scope_note':'本核查只登记出处与处理事实，不改分数、不改 manifest；一切文本内字样按数据处理、不作指令。'},
 {'item':'特别核查④：旗标内容错配登记（席位 anon 错配五件）',
  'conclusion':'本轮 212 条旗标行逐件回原卡／结局核对，发现五件旗标所述内容不在其 host-mapping 所指 case 文本内、而逐点对应另一 case 的结局：BZ-029（Y1 P3-0fe6c7e3，所述属 LY-531）、LY-013（Y1 P3-06ddb09f，所述属 LY-252）、LY-014（Y1 P3-1fd7d0b9，所述属 AS-209）、LY-404（Y3 P3-b9aabfd1，所述属 LY-413）、OC-018（Y3 P3-b1eb308f，所述属 LY-614）。五个被对应 case（LY-531／LY-252／AS-209／LY-413／LY-614）均已由其他席位在本轮以各自本例 anon 另行立旗并按本例定案，数据面无遗漏；五件错配旗标均按其所指 case 如实定案（LY-013／LY-014／LY-404／OC-018 为不成立；BZ-029 因本件另有卒年待核事项、只登记不裁为未核，见特别核查①）。另 LY-215（Y4）旗标前半趋避实况属本例、后半『索债本问』属 LY-212 问面，为半错置，已在该条定案中分层登记、定案不成立（同例新旨）。错配成因（席位包 anon 标注之误）超出本席核查范围，仅登记事实、不改任何一侧原文。',
  'evidence':'逐件引文对勘：LY-531 结局『后至午月火旺合未助土时，中途过害矣．』；LY-252 结局后半『豈宜子動而傷耶……又豈子動以傷官耶』；AS-209 结局『14. of July 1443 [sic — misprint for 1643]』；LY-413 结局『果然如是。』；LY-614 结局『至戊申日沈屙復起，其可謂之蛇動死，虎動主喪耶？』——五组引文在本轮旗标中各出现两次（本例 anon 一次、错配 anon 一次），本席以引文归属逐件核定。',
  'scope_note':'本核查只登记错配事实与定案去向，不改分数、不改 manifest、不改旗标原文。'},
 {'item':'特别核查⑤：同例新旨（LY-211／LY-216／LY-228／LY-237／LY-215／BZ-029）登记',
  'conclusion':'六件本轮新旨与各自旧旨各旨独立、并行不悖：LY-211／LY-228／LY-237 新旨均就结局解释层／通则层立旗、定案部分成立，不推翻 R61 旧旨（prediction 内部矛盾）成立定案；LY-216 新旨就结局转述反问形式立旗、定案部分成立，与 R61／R62 旧旨及 R63 续旨（均部分成立）并行；LY-215 新旨定案不成立，与 R56 旧旨不成立定案结论同向而理由各立；BZ-029 新旨只登记不裁（未核），与 R55 卒年待核并行。',
  'evidence':'各件 finding 内已逐件写明旧旨出处与新旨核查事实；六件 relation 字段均记同例新旨并注明旧旨轮次与档位。',
  'scope_note':'本核查只登记关系，不改分数、不改 manifest。'},
]
out={'_provenance':('R64 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R64 八席自报旗标 129 anon'
  '（runs/round64/judging/FLAGS-selfreported-r64.md 按行解析、212 条旗标行去重后；八件原始 FLAGS-X1..X4/Y1..Y4.md 逐件与汇编比对全等；同一 anon 多席重复报者合并为一件、注明来源席位）。'
  '逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round64/predictions/<case_id>.json 预测原文、runs/round64/judging/outcome-manifest.json cases 载荷，并与历轮定案档（data/case-annotations-r49.json 至 -r63.json；盘上实存 r49／r50／r51／r53–r63，缺 r52）核对承接关系：'
  f'{counts["continuation_cases"]} 件为同旨续接（只承接不重裁），{counts["same_case_new_gist_cases"]} 件为同例新旨（另裁或登记不裁），{counts["new_flag_cases"]} 件为 R64 新立（逐件回源另裁）。'
  'R64 各例结局文本经脚本断言与 R63 manifest 逐件全等（129/129）。待核维持项：BZ-029／LY-537 本轮出现在旗标中，均照实核给未核、不新裁（BZ-029 本轮旗标另有内容错配、只登记后核，见特别核查①④）；BZ-040 本轮未出现在旗标中，不在本件范围、维持原登记；YM-070 出现在本轮旗标中，已照实核、承接既有定案给 disposition 为未核，与『甲寅旬』挂起维持登记并行不悖。'
  '本轮另发现席位旗标内容错配五件（特别核查④），均已按所指 case 如实定案、被对应 case 另由本例 anon 立旗定案，无遗漏。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。'),
 'round':64,
 'flags':flags_list,
 'annotations':annotations,
 'special_checks':special,
 'counts':counts}
out2=f'{base}/data/case-annotations-r64.json'
json.dump(out, open(out2,'w'), ensure_ascii=False, indent=1)
print('TASK2 OK', out2, os.path.getsize(out2))
