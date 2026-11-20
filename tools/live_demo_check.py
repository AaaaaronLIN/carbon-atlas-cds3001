#!/usr/bin/env python3
"""Pre-flight check for the classroom live demo.

Usage:
  python3 live_demo_check.py http://127.0.0.1:5001
  python3 live_demo_check.py https://xxxx.trycloudflare.com
"""
import json
import sys
import urllib.request

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5001").rstrip("/")

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=15) as r:
        return r.status, json.loads(r.read().decode())

checks = []
try:
    with urllib.request.urlopen(BASE + "/", timeout=15) as r:
        checks.append(("page /", r.status == 200, f"HTTP {r.status}"))
    st, health = get("/api/health")
    checks.append(("API health", st == 200 and health.get("rows") == 655200,
                   f"rows={health.get('rows')} last_day={health.get('last_day')}"))
    st, ytd = get("/api/country_ytd?year=2025")
    checks.append(("2025 world total", st == 200 and abs(float(ytd.get("world_total", 0)) - 37856) < 1,
                   f"world_total={ytd.get('world_total')}"))
    st, sectors = get("/api/sectors?country=WORLD&year=2025")
    checks.append(("2025 sectors", st == 200 and isinstance(sectors, list) and len(sectors) >= 6,
                   f"{len(sectors)} sectors" if isinstance(sectors, list) else str(sectors)[:60]))
except Exception as exc:  # noqa: BLE001
    print("FAILED:", exc)
    print("Is Flask running and is MySQL up?")
    raise SystemExit(1)

ok = True
for name, passed, detail in checks:
    print(("PASS  " if passed else "FAIL  ") + name + "  " + detail)
    ok = ok and passed
print("\nURL:", BASE)
print("RESULT:", "READY for live demo" if ok else "NOT READY")
raise SystemExit(0 if ok else 1)
