#!/usr/bin/env bash
# Build a clean Cloudflare Worker assets folder (no .git/android/Python).
set -euo pipefail
cd "$(dirname "$0")"
rm -rf public
mkdir -p public/.well-known
for f in index.html manifest.json sw.js \
  orca-integrations.js orca-sentry.js orca-sw-register.js \
  icon-192.png icon-512.png orca-mascot.png orca-icon.png orcamint-thumb.png \
  keiko-minted.jpg lightchain-ai-1.jpg; do
  [ -f "$f" ] && cp "$f" public/
done
[ -f .well-known/assetlinks.json ] && cp .well-known/assetlinks.json public/.well-known/
echo "public/ ready for wrangler ($(find public -type f | wc -l) files)"
