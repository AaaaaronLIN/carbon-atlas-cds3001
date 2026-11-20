#!/bin/bash
# Start a free Cloudflare quick tunnel to the local Carbon Atlas app.
# Run start_live_demo.sh first. Ctrl+C stops the tunnel.
set -euo pipefail
cd /tmp

ARCH="$(uname -m)"
case "$ARCH" in
  arm64) ASSET="cloudflared-darwin-arm64.tgz" ;;
  x86_64) ASSET="cloudflared-darwin-amd64.tgz" ;;
  *) echo "Unsupported arch: $ARCH"; exit 1 ;;
esac

if [ ! -x /tmp/cloudflared ]; then
  echo "Downloading cloudflared ($ASSET) ..."
  curl -L --max-time 180 -o /tmp/cloudflared.tgz \
    "https://github.com/cloudflare/cloudflared/releases/latest/download/${ASSET}"
  tar -xzf /tmp/cloudflared.tgz -C /tmp
  chmod +x /tmp/cloudflared
fi

echo "Opening a public HTTPS URL for http://127.0.0.1:5001 ..."
echo "Copy the https://....trycloudflare.com line into the classroom browser."
exec /tmp/cloudflared tunnel --url http://127.0.0.1:5001 --no-autoupdate
