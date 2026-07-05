#!/usr/bin/env bash
# Copy static site into www/ for Capacitor Android builds.
set -euo pipefail
cd "$(dirname "$0")"
rm -rf www
mkdir -p www
for f in index.html manifest.json capacitor.config.json \
  orca-integrations.js orca-sentry.js orca-sw-register.js sw.js \
  icon-192.png icon-512.png orca-mascot.png orca-icon.png \
  keiko-minted.jpg lightchain-ai-1.jpg OrcaMint.apk; do
  [ -f "$f" ] && cp "$f" www/
done
echo "www/ ready for Capacitor ($(ls www | wc -l) files)"