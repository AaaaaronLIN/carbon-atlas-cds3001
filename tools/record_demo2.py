#!/usr/bin/env python3
"""Record the 90-second Carbon Atlas demo by sampling the page with Page.captureScreenshot.

Robust alternative to CDP screencast (which crashed in this environment).
Output: out/presentation/ads/video/carbon_atlas_demo_90s.mp4 (1280x720, H.264, silent)
"""
import base64
import json
import os
import shutil
import subprocess
import time

import requests
import websocket

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9445
PROFILE = "/tmp/cc-record2-profile"
URL = "http://127.0.0.1:5001/?theme=stage"
FRAMES = "/tmp/demo_frames2"
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "presentation", "ads", "video")
OUT = os.path.join(OUT_DIR, "carbon_atlas_demo_90s.mp4")
FFMPEG = "/tmp/ffmpegpkg/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v9.0"


class CDP:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, timeout=60)
        self.i = 0

    def send(self, method, params=None):
        self.i += 1
        mid = self.i
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("method"):
                continue
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def js(self, expression):
        res = self.send("Runtime.evaluate", {"expression": expression, "returnByValue": True,
                                             "awaitPromise": True})
        return res.get("result", {}).get("value")

    def shot(self, quality=82):
        # no clip: capture the current viewport (a clip would target page coordinates
        # and return black once the page has scrolled)
        res = self.send("Page.captureScreenshot", {"format": "jpeg", "quality": quality})
        return base64.b64decode(res["data"])


def launch():
    subprocess.run(["pkill", "-f", f"remote-debugging-port={PORT}"], capture_output=True)
    time.sleep(1)
    shutil.rmtree(PROFILE, ignore_errors=True)
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-gpu-sandbox",
         "--in-process-gpu", "--disable-dev-shm-usage", "--disable-software-rasterizer",
         "--disable-breakpad", "--disable-crash-reporter", "--hide-scrollbars",
         "--no-first-run", "--no-default-browser-check", "--disable-extensions",
         "--force-device-scale-factor=1", "--window-size=1440,810",
         f"--remote-debugging-port={PORT}", f"--user-data-dir={PROFILE}",
         "--autoplay-policy=no-user-gesture-required", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(120):
        try:
            requests.get(f"http://127.0.0.1:{PORT}/json/version", timeout=0.5)
            return proc
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("chrome did not start")


# (seconds from start, JS action)
ACTIONS = [
    (3.0, "document.querySelector('#storyBtn').click()"),
    (17.0, "document.querySelector('#storySkip').click()"),
    (18.5, "document.querySelector('#where').scrollIntoView({behavior:'smooth',block:'start'})"),
    (20.5, "var s=document.querySelector('#countrySelect'); s.value='China'; s.dispatchEvent(new Event('change'))"),
    (24.0, "document.querySelector('#rankTable thead th[data-key=\"change\"]').click()"),
    (27.0, "document.querySelector('#what').scrollIntoView({behavior:'smooth',block:'start'})"),
    (31.0, "var s=document.querySelector('#countrySelect'); s.value='India'; s.dispatchEvent(new Event('change'))"),
    (35.0, "document.querySelector('#when').scrollIntoView({behavior:'smooth',block:'start'})"),
    (37.0, "var q=document.querySelector('#compareSelect'); q.value='United States'; q.dispatchEvent(new Event('change'))"),
    (41.0, "document.querySelector('#modeIdx').click()"),
    (45.0, "document.querySelector('#findings').scrollIntoView({behavior:'smooth',block:'start'})"),
    (49.0, "document.querySelector('#team').scrollIntoView({behavior:'smooth',block:'start'})"),
    (53.0, "document.querySelector('#method').scrollIntoView({behavior:'smooth',block:'start'})"),
    (58.0, "document.querySelector('#themeBtn').click()"),
    (62.0, "document.querySelector('#themeBtn').click()"),
    (65.0, "window.scrollTo({top:0,behavior:'smooth'})"),
    (67.0, "document.querySelector('#resetBtn').click()"),
    (68.0, "document.querySelector('#yearButtons .chip[data-year=\"2026\"]').click()"),
    (72.0, "document.querySelector('#yearButtons .chip[data-year=\"2025\"]').click()"),
    (74.0, "document.querySelector('#where').scrollIntoView({behavior:'smooth',block:'start'})"),
    (77.0, "document.querySelector('#countrySelect').value='WORLD'; document.querySelector('#countrySelect').dispatchEvent(new Event('change'))"),
    (80.0, "window.scrollTo({top:0,behavior:'smooth'})"),
    (84.0, "document.querySelector('#storyBtn').click()"),
]
LIMIT = 90.0


def main():
    shutil.rmtree(FRAMES, ignore_errors=True)
    os.makedirs(FRAMES, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    proc = launch()
    try:
        page = requests.put(f"http://127.0.0.1:{PORT}/json/new?{URL}", timeout=5).json()
        c = CDP(page["webSocketDebuggerUrl"])
        c.send("Page.enable")
        c.send("Runtime.enable")
        c.send("Emulation.setDeviceMetricsOverride",
               {"width": 1440, "height": 810, "deviceScaleFactor": 1, "mobile": False})
        c.send("Page.navigate", {"url": URL})
        while True:
            if c.js("document.readyState === 'complete' && document.querySelector('#kpiTotal') && document.querySelector('#kpiTotal').textContent.trim() !== '—'"):
                break
            time.sleep(0.2)
        time.sleep(1.5)
        print("current kpi:", c.js("document.querySelector('#kpiTotal').textContent"))

        t0 = time.time()
        ai = 0
        i = 0
        stamps = []
        while True:
            now = time.time() - t0
            if now >= LIMIT:
                break
            while ai < len(ACTIONS) and ACTIONS[ai][0] <= now:
                try:
                    c.js(ACTIONS[ai][1])
                except Exception as exc:
                    print("action err", ACTIONS[ai][0], exc)
                ai += 1
            try:
                data = c.shot()
            except Exception as exc:
                print("shot err", exc)
                time.sleep(0.05)
                continue
            with open(os.path.join(FRAMES, f"f{i:05d}.jpg"), "wb") as f:
                f.write(data)
            stamps.append(time.time() - t0)
            i += 1
        print("frames:", i, "avg fps:", round(i / stamps[-1], 2) if stamps else 0)

        lines = []
        for idx in range(i):
            if idx < i - 1:
                dur = stamps[idx + 1] - stamps[idx]
            else:
                dur = 1 / 15
            dur = max(1 / 60, min(0.5, dur))
            lines.append(f"file '{os.path.join(FRAMES, f'f{idx:05d}.jpg')}'")
            lines.append(f"duration {dur:.4f}")
        lines.append(f"file '{os.path.join(FRAMES, f'f{i-1:05d}.jpg')}'")
        listfile = os.path.join(FRAMES, "list.txt")
        with open(listfile, "w") as f:
            f.write("\n".join(lines) + "\n")

        cmd = [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", listfile,
               "-fps_mode", "cfr", "-r", "30",
               "-vf", "scale=1280:720:flags=lanczos,format=yuv420p",
               "-c:v", "libx264", "-preset", "medium", "-crf", "22",
               "-pix_fmt", "yuv420p", "-color_range", "tv",
               "-movflags", "+faststart", OUT]
        print("encoding...")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print("wrote", OUT, os.path.getsize(OUT), "bytes")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    main()
