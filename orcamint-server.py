"""OrcaMint — simple static server for Railway hosting."""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT      = int(os.environ.get("PORT", 8080))
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(BASE_DIR, "index.html")

# Scoped CORS — override with CORS_ORIGINS env (comma-separated)
_CORS_ORIGINS = [o.strip() for o in os.environ.get(
    "CORS_ORIGINS",
    "https://orcamint.xyz,http://localhost:8080,http://127.0.0.1:8080"
).split(",") if o.strip()]


def _cors_for(handler) -> str:
    origin = (handler.headers.get("Origin") or "").strip()
    if origin in _CORS_ORIGINS:
        return origin
    return _CORS_ORIGINS[0] if _CORS_ORIGINS else "https://orcamint.xyz"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress access log noise

    def do_GET(self):
        if self.path in ("", "/", "/index.html"):
            self._serve_html()
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", _cors_for(self))
        self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _serve_html(self):
        if not os.path.exists(HTML_FILE):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OrcaMint server running")
            return
        with open(HTML_FILE, "rb") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"OrcaMint server starting on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
