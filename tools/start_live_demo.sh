#!/bin/bash
# Carbon Atlas — start the real Flask + MySQL app for a classroom live demo.
# Usage:  DB_PASSWORD='your-password' ./start_live_demo.sh
# It binds 0.0.0.0 so another device on the same network can open it.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP="$ROOT/01_WebApp_Code"
PORT="${PORT:-5001}"
: "${DB_PASSWORD:?export DB_PASSWORD='your MySQL password' first}"

if ! nc -z 127.0.0.1 3306 >/dev/null 2>&1; then
  echo "WARNING: nothing is listening on MySQL port 3306 — start MySQL first."
fi

# stop a previous instance on the same port (safe for demo only)
lsof -ti tcp:"$PORT" | xargs kill -9 2>/dev/null || true

cd "$APP"
echo "Starting Flask on 0.0.0.0:${PORT} ..."
HOST=0.0.0.0 PORT="$PORT" nohup /opt/anaconda3/bin/python3 app.py \
  > /tmp/carbon_atlas_live.log 2>&1 &
SERVER_PID=$!

for i in $(seq 1 30); do
  if curl -fsS "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1; then break; fi
  sleep 0.3
done

if ! curl -fsS "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1; then
  echo "ERROR: Flask did not start. See /tmp/carbon_atlas_live.log"
  exit 1
fi

IP="$(ipconfig getifaddr en0 2>/dev/null || true)"
IP2="$(ipconfig getifaddr en1 2>/dev/null || true)"
echo
echo "Flask is up (PID $SERVER_PID)."
echo "  Local:      http://127.0.0.1:${PORT}/"
[ -n "$IP" ]  && echo "  LAN (Wi-Fi): http://${IP}:${PORT}/"
[ -n "$IP2" ] && echo "  LAN (other): http://${IP2}:${PORT}/"
echo
echo "Next:"
echo "  1) phone with 4G: open the LAN URL (or run ./start_tunnel.sh for a public URL)"
echo "  2) classroom Windows: open the same URL in Edge/Chrome"
echo "  3) prevent sleep:  caffeinate -dimsu"
echo "  4) logs:           tail -f /tmp/carbon_atlas_live.log"
echo
echo "Stop with: lsof -ti tcp:${PORT} | xargs kill"
