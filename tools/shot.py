#!/usr/bin/env python3
"""
Tiny Chrome DevTools Protocol driver (no npm needed).

Usage:
  python3 shot.py --url http://127.0.0.1:5001/ --out page.png --width 1440 --height 1000 --full
  python3 shot.py --url ... --out el.png --selector "#mapChart"
  python3 shot.py --url ... --out report.pdf --pdf
  python3 shot.py --url ... --check "#kpiTotal"      # print console + evaluate
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import time

import requests
import websocket

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9333
PROFILE = "/tmp/cc-chrome-profile"


class CDP:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, timeout=30)
        self.i = 0
        self.events = []
        self.logs = []

    def send(self, method, params=None):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("method"):
                self.events.append(msg)
                self._capture(msg)
                continue
            if msg.get("id") == self.i:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def _capture(self, msg):
        m = msg["method"]
        if m == "Runtime.consoleAPICalled":
            args = " ".join(str(a.get("value", a.get("description", ""))) for a in msg["params"]["args"])
            self.logs.append(("console." + msg["params"]["type"], args))
        elif m == "Runtime.exceptionThrown":
            d = msg["params"]["exceptionDetails"]
            self.logs.append(("exception", d.get("text", "") + " " + str(d.get("exception", {}).get("description", ""))))
        elif m == "Log.entryAdded":
            e = msg["params"]["entry"]
            self.logs.append(("log." + e["level"], e["text"] + " " + e.get("url", "")))

    def wait(self, expr, timeout=25):
        end = time.time() + timeout
        while time.time() < end:
            r = self.send("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True})
            v = r.get("result", {}).get("value")
            if v:
                return v
            time.sleep(0.25)
        raise TimeoutError(f"condition never true: {expr}")

    def eval(self, expr):
        r = self.send("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True})
        return r.get("result", {}).get("value")


def launch():
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
         "--disable-gpu-sandbox", "--in-process-gpu", "--disable-dev-shm-usage",
         "--disable-software-rasterizer", "--disable-breakpad",
         "--disable-crash-reporter", "--hide-scrollbars",
         "--no-first-run", "--no-default-browser-check", "--disable-extensions",
         f"--remote-debugging-port={PORT}", f"--user-data-dir={PROFILE}",
         "--window-size=1440,1000", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(120):
        try:
            requests.get(f"http://127.0.0.1:{PORT}/json/version", timeout=0.5)
            return proc
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("Chrome did not start")


def open_page(url):
    r = requests.put(f"http://127.0.0.1:{PORT}/json/new?{url}", timeout=5)
    r.raise_for_status()
    return r.json()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--out")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=1000)
    ap.add_argument("--scale", type=float, default=2.0)
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--selector")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--check")
    ap.add_argument("--wait", default="document.querySelector('#kpiTotal') && document.querySelector('#kpiTotal').textContent.trim() !== '—'")
    ap.add_argument("--json-out")
    ap.add_argument("--transparent", action="store_true")
    a = ap.parse_args()

    proc = launch()
    try:
        page = open_page(a.url)
        cdp = CDP(page["webSocketDebuggerUrl"])
        cdp.send("Page.enable")
        cdp.send("Runtime.enable")
        cdp.send("Log.enable")
        cdp.send("Emulation.setDeviceMetricsOverride",
                 {"width": a.width, "height": a.height, "deviceScaleFactor": a.scale, "mobile": False})
        cdp.send("Page.navigate", {"url": a.url})
        cdp.wait("document.readyState === 'complete'", 30)
        try:
            cdp.wait(a.wait, 30)
        except TimeoutError as e:
            print("WARN:", e, file=sys.stderr)
        cdp.wait("new Promise(r => setTimeout(() => r(true), 900))", 10)

        result = {}
        if a.check:
            result["check"] = cdp.eval(a.check)

        if a.out and a.pdf:
            r = cdp.send("Page.printToPDF", {
                "printBackground": True, "preferCSSPageSize": False,
                "paperWidth": 8.27, "paperHeight": 11.69,
                "marginTop": 0, "marginBottom": 0, "marginLeft": 0, "marginRight": 0,
            })
            with open(a.out, "wb") as f:
                f.write(base64.b64decode(r["data"]))
        elif a.out and a.selector:
            box = cdp.eval("(() => { const e = document.querySelector(%s); if(!e) return null; const r = e.getBoundingClientRect(); return {x:r.x+scrollX, y:r.y+scrollY, w:r.width, h:r.height}; })()" % json.dumps(a.selector))
            if not box:
                raise RuntimeError("selector not found: " + a.selector)
            cap_params = {
                "format": "png", "captureBeyondViewport": True,
                "clip": {"x": box["x"], "y": box["y"], "width": box["w"], "height": box["h"], "scale": 1},
            }
            if a.transparent:
                cap_params["omitBackground"] = True
            r = cdp.send("Page.captureScreenshot", cap_params)
            with open(a.out, "wb") as f:
                f.write(base64.b64decode(r["data"]))
            result["box"] = box
        elif a.out:
            if a.full:
                m = cdp.send("Page.getLayoutMetrics")
                size = m["cssContentSize"]
                clip = {"x": 0, "y": 0, "width": size["width"], "height": size["height"], "scale": 1}
            else:
                clip = None
            params = {"format": "png"}
            if clip:
                params["clip"] = clip
                params["captureBeyondViewport"] = True
            r = cdp.send("Page.captureScreenshot", params)
            with open(a.out, "wb") as f:
                f.write(base64.b64decode(r["data"]))
            result["screenshot"] = a.out

        result["errors"] = [l for l in cdp.logs if l[0] in ("exception", "log.error", "console.error")]
        result["logs"] = cdp.logs[-40:]
        if a.json_out:
            with open(a.json_out, "w") as f:
                json.dump(result, f, indent=2)
        print(json.dumps(result, indent=1)[:6000])
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    main()
