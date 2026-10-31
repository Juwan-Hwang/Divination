import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
anon='P3-678389ac'
for name in ['packet1.json','packet2.json','packet3.json','packet4.json','packetA.json','packetB.json']:
    p=base/'runs/round88/judging'/name
    data=json.load(open(p))
    print(name, type(data), len(data) if hasattr(data,'__len__') else '')
    # search recursively for anon and editor_note
    s=json.dumps(data, ensure_ascii=False)
    print('  anon present?', anon in s, 'editor_note count', s.count('editor_note'))
    if anon in s:
        # find items
        items=data if isinstance(data,list) else data.get('cases',data)
        if isinstance(items, dict): items=list(items.values())
        for it in items:
            if isinstance(it,dict) and anon in json.dumps(it,ensure_ascii=False):
                print('  item:', json.dumps(it, ensure_ascii=False)[:1200])
    if 'editor_note' in s:
        items=data if isinstance(data,list) else data.get('cases',data)
        if isinstance(items, dict): items=list(items.values())
        if isinstance(items,list):
            for it in items:
                if isinstance(it,dict) and 'editor_note' in it:
                    print('  editor_note item keys:', list(it.keys()), 'anon?', it.get('anon_id') or it.get('id'), 'note:', str(it.get('editor_note'))[:200])
