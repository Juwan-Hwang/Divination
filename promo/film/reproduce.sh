#!/bin/sh
# Rebuild both cuts of the 严肃占卜 · Divination launch film from committed inputs.
#   sh reproduce.sh            → deliver/divination-promo-{en,zh}.rebuild.mp4
#   LANGS=zh sh reproduce.sh   → one cut
# 3D frames (film/frames/{open,end}) are rendered from film/o3d.html (~15 min on SwiftShader). The cast shown is the
# committed real run (session/cast.txt); casting again gives a different hexagram, so it is not re-run here.
# Audio is seeded (score rng 7, SFX jitter 11, room 3); existing frames are skipped (resumable).
set -e
cd "$(dirname "$0")"
sh setup.sh
(python3 -m http.server 8777 --directory film >/tmp/divination-film-http.log 2>&1 &)
sleep 1
cp session/cast.txt film/data/cast.txt
[ "$(ls film/frames/open 2>/dev/null | wc -l)" -ge 180 ] || python3 r3d_seq.py open 6.0 film/frames/open --page o3d.html --sub 3
[ "$(ls film/frames/end 2>/dev/null | wc -l)" -ge 75 ] || python3 r3d_seq.py end 2.5 film/frames/end --page o3d.html --sub 3 --handoff comp.html
for L in ${LANGS:-en zh}; do
  python3 scripts/dump_events.py --comp "comp.html?lang=$L" --out "audio/events_$L.json"
  python3 music.py --events "audio/events_$L.json" --out "audio/$L"
  python3 sound.py --events "audio/events_$L.json" --music "audio/$L/music.wav" --out "audio/mix_$L.wav"
  while [ "$(ls film/out/frames_$L 2>/dev/null | grep -c jpg$)" -lt 1800 ]; do
    python3 render_film.py --comp "comp.html?lang=$L" --out "film/out/frames_$L" --workers 3 --max-seconds 1100
  done
  ./encode.sh "film/out/frames_$L" "audio/mix_$L.wav" "deliver/divination-promo-$L.rebuild.mp4"
done
