#!/usr/bin/env python3
"""
dev_server.py — Servidor local de desarrollo para MKT_VISA Hub
==============================================================
Uso:
    python3 dev_server.py
    → abre http://localhost:8888

Endpoints especiales:
    POST /rebuild  → corre build_manifest.py y devuelve resultado JSON
    GET  /*        → sirve archivos estáticos (index.html, assets/, src/, etc.)
"""

import os, json, subprocess, sys, pathlib
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT      = 8888
REPO_ROOT = pathlib.Path(__file__).resolve().parent
SCRIPT    = REPO_ROOT / "scripts" / "build_manifest.py"

class DevHandler(SimpleHTTPRequestHandler):

    def log_message(self, fmt, *args):
        # Formato limpio en terminal
        status = args[1] if len(args) > 1 else '?'
        color  = '\033[92m' if str(status).startswith('2') else '\033[91m'
        reset  = '\033[0m'
        print(f"  {color}{status}{reset}  {self.command} {self.path}")

    def do_POST(self):
        if self.path == '/rebuild':
            self._run_rebuild()
        else:
            self.send_error(404, "Not found")

    def _run_rebuild(self):
        print(f"\n🔄  Rebuilding manifest...\n{'─'*40}")
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True, text=True, cwd=str(REPO_ROOT)
        )
        ok     = result.returncode == 0
        output = result.stdout + result.stderr
        print(output)
        print('─'*40)
        print(f"{'✅ Done' if ok else '❌ Error'}\n")

        body = json.dumps({
            "ok":     ok,
            "output": output.strip(),
        }).encode()

        self.send_response(200)
        self.send_header("Content-Type",  "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin",  "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()


if __name__ == "__main__":
    os.chdir(REPO_ROOT)           # servir desde la raíz del repo
    server = HTTPServer(("", PORT), DevHandler)
    print(f"""
╔══════════════════════════════════════════╗
║   MKT VISA Hub · Dev Server              ║
║   http://localhost:{PORT}                   ║
║                                          ║
║   POST /rebuild  →  reconstruye manifest ║
║   Ctrl+C         →  detener servidor     ║
╚══════════════════════════════════════════╝
""")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋  Servidor detenido.\n")
