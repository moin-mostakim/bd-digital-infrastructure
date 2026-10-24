#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/.vercel/output"
BUILD_ID="$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || date +%s)"
rm -rf "$ROOT/.vercel/output"
mkdir -p "$OUT/static"
sed "s/__DECK_BUILD_ID__/${BUILD_ID}/g" "$ROOT/index.html" > "$OUT/static/index.html"
cp -R "$ROOT/vendor" "$OUT/static/vendor"
if [ -d "$ROOT/audio" ]; then
  cp -R "$ROOT/audio" "$OUT/static/audio"
fi
cat > "$OUT/config.json" <<EOF
{
  "version": 3,
  "routes": [
    { "handle": "filesystem" },
    {
      "src": "/index.html",
      "headers": {
        "Cache-Control": "no-cache, no-store, must-revalidate"
      }
    },
    {
      "src": "/",
      "headers": {
        "Cache-Control": "no-cache, no-store, must-revalidate"
      }
    },
    { "src": "/(.*)", "status": 404, "dest": "/404.html" }
  ]
}
EOF
echo "Prepared $OUT (build ${BUILD_ID})"
