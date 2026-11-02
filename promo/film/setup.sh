#!/bin/sh
# One-time setup (safe to re-run): Python deps + Chromium, three.js r170, earshot @ 925ebe5, fonts, and the brand files.
# No font binary is committed: Noto Serif SC / Noto Sans Mono CJK SC come from notofonts/noto-cjk, Source Serif 4 from
# adobe-fonts/source-serif; the coin glyphs are subset from Noto Serif SC Regular. fonts.sha256 pins the exact files used.
set -e
cd "$(dirname "$0")"
pip install -q -r requirements.txt
python3 -m playwright install --with-deps chromium || python3 -m playwright install chromium
[ -d film/node_modules/three ] || npm install --silent --no-save --prefix film three@0.170.0
mkdir -p film/fonts film/brand
cp ../../assets/brand/lockup-horizontal-reverse.svg ../../assets/brand/mark.svg film/brand/
N=https://github.com/notofonts/noto-cjk/raw/main
S=https://github.com/adobe-fonts/source-serif/raw/release/TTF
for w in Regular SemiBold Bold; do [ -f film/fonts/NotoSerifSC-$w.otf ] || curl -fsSL -o film/fonts/NotoSerifSC-$w.otf $N/Serif/SubsetOTF/SC/NotoSerifSC-$w.otf; done
for w in Regular Bold; do [ -f film/fonts/NotoSansMonoCJKsc-$w.otf ] || curl -fsSL -o film/fonts/NotoSansMonoCJKsc-$w.otf $N/Sans/Mono/NotoSansMonoCJKsc-$w.otf; done
for w in Regular Semibold Bold; do [ -f film/fonts/SourceSerif4-$w.ttf ] || curl -fsSL -o film/fonts/SourceSerif4-$w.ttf $S/SourceSerif4-$w.ttf; done
[ -f film/fonts/coin.otf ] || pyftsubset film/fonts/NotoSerifSC-Regular.otf --text="乾隆通寶" --output-file=film/fonts/coin.otf
sha256sum -c fonts.sha256 || echo "warning: a font differs from the one the film was rendered with (metrics may shift)"
if [ ! -d repos/earshot ]; then
  git clone -q https://github.com/Leonxlnx/earshot repos/earshot
  git -C repos/earshot checkout -q 925ebe56a1b755e5d354ab642bb8f344440cfa9c
fi
pip install -q --no-deps -e repos/earshot
echo "setup ok: python3 -m http.server 8777 --directory film, then open http://localhost:8777/comp.html?lang=en&t=0"
