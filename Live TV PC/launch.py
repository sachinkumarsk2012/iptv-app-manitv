from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import shutil
import subprocess
import time
import urllib.request
import webbrowser


APP_DIR = Path(__file__).resolve().parent


class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def log_message(self, _format, *_args):
        pass


def browser_candidates():
    paths = [
        shutil.which("msedge"),
        os.path.join(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"), "Microsoft", "Edge", "Application", "msedge.exe"),
        os.path.join(os.environ.get("PROGRAMFILES", r"C:\Program Files"), "Microsoft", "Edge", "Application", "msedge.exe"),
        shutil.which("chrome"),
        os.path.join(os.environ.get("PROGRAMFILES", r"C:\Program Files"), "Google", "Chrome", "Application", "chrome.exe"),
    ]
    seen = set()
    for path in paths:
        if path and path not in seen and os.path.isfile(path):
            seen.add(path)
            yield path


def main():
    if not (APP_DIR / "index.html").is_file():
        raise FileNotFoundError("index.html is missing from the Live TV app folder")
    server = ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
    server.daemon_threads = True
    port = server.server_address[1]
    url = f"http://127.0.0.1:{port}/"
    print(f"Livewave is starting at {url}", flush=True)
    import threading
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    for _ in range(30):
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if response.status == 200:
                    break
        except Exception:
            time.sleep(0.1)
    opened = False
    for browser in browser_candidates():
        try:
            subprocess.Popen([browser, f"--app={url}", "--start-fullscreen", "--no-proxy-server"], close_fds=True)
            opened = True
            break
        except OSError:
            continue
    if not opened:
        opened = webbrowser.open(url)
    if not opened:
        print("Could not open a browser automatically. Copy this address into Edge or Chrome:", flush=True)
        print(url, flush=True)
    print("Keep this window open while Livewave is running. Press Ctrl+C here to stop the local server.", flush=True)
    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("\nStopping Livewave server.", flush=True)
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Livewave could not start: {error}", flush=True)
        input("Press Enter to close this window...")
