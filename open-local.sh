#!/usr/bin/env bash
# Offline-friendly local preview (no Vercel required)
cd "$(dirname "$0")"
cp -f ../Bangladesh_Digital_Infrastructure.html index.html 2>/dev/null || true
if command -v python3 >/dev/null; then
  echo "Open http://127.0.0.1:8765 in your browser"
  python3 -m http.server 8765
else
  open index.html
fi
