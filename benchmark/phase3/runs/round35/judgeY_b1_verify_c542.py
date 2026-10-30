import json, pathlib
base = pathlib.Path(__file__).parent
packet = json.loads((base/"judging"/"packet1.json").read_text(encoding="utf-8"))
mapping = json.loads((base/"judging"/"host-mapping.json").read_text(encoding="utf-8"))
# packet structure inspection
print("packet type:", type(packet).__name__)
if isinstance(packet, dict):
    print("packet keys:", list(packet.keys())[:20])
    # try find list
    for k,v in packet.items():
        print(k, type(v).__name__, len(v) if hasattr(v,'__len__') else '')
elif isinstance(packet, list):
    print("packet len:", len(packet))
    print("first item keys:", list(packet[0].keys()) if packet else None)
    print(json.dumps(packet[0], ensure_ascii=False)[:2000])
print("mapping type:", type(mapping).__name__)
if isinstance(mapping, dict):
    print("mapping len:", len(mapping))
    items=list(mapping.items())[:3]
    for k,v in items:
        print(repr(k), "->", repr(v)[:500])
