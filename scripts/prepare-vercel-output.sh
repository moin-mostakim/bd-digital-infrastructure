#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/.vercel/output"
rm -rf "$ROOT/.vercel/output"
mkdir -p "$OUT/static"
cp "$ROOT/index.html" "$OUT/static/index.html"
cp -R "$ROOT/vendor" "$OUT/static/vendor"
cat > "$OUT/config.json" <<'EOF'
{
  "version": 3,
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "status": 404, "dest": "/404.html" }
  ]
}
EOF
echo "Prepared $OUT (index.html + vendor/ + filesystem routes)"
