"""
Computer Science & Modern AI Evolution — Python HTTPS Educational Web Server
School Project Main Application (main.py)
"""

import http.server
import json
import os
import re
import ssl
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CERT_DIR = BASE_DIR / "certs"
CERT_FILE = CERT_DIR / "cert.pem"
KEY_FILE = CERT_DIR / "key.pem"


def hello_world():
    print("Hello, world! Welcome to the Computer Science & AI Evolution Portal.")


def validate_registration(
    username: str = "",
    email: str = "",
    password: str = "",
    confirm_password: str = "",
) -> tuple[bool, list[str]]:
    """Validate user registration form fields and prevent empty submissions."""
    errors = []

    username = (username or "").strip()
    email = (email or "").strip()
    password = (password or "").strip()
    confirm_password = (confirm_password or "").strip()

    if not any([username, email, password, confirm_password]):
        return False, ["Form cannot be submitted empty. All fields are required."]

    if not username:
        errors.append("Username is required.")
    elif len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
    elif not re.match(r"^[a-zA-Z0-9_]+$", username):
        errors.append("Username can only contain letters, numbers, and underscores.")

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not email:
        errors.append("Email is required.")
    elif not re.match(email_pattern, email):
        errors.append("Please enter a valid email address.")

    if not password:
        errors.append("Password is required.")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    elif not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
        errors.append("Password must include at least one uppercase letter and one number.")

    if not confirm_password:
        errors.append("Please confirm your password.")
    elif password != confirm_password:
        errors.append("Passwords do not match.")

    return len(errors) == 0, errors


def ensure_https_certificates() -> bool:
    """Generate a local self-signed SSL/TLS certificate for HTTPS if not already present."""
    if CERT_FILE.exists() and KEY_FILE.exists():
        return True

    CERT_DIR.mkdir(parents=True, exist_ok=True)
    openssl_candidates = [
        "openssl",
        r"C:\Program Files\Git\usr\bin\openssl.exe",
    ]

    for openssl_bin in openssl_candidates:
        try:
            subprocess.run(
                [
                    openssl_bin,
                    "req",
                    "-x509",
                    "-newkey",
                    "rsa:2048",
                    "-keyout",
                    str(KEY_FILE),
                    "-out",
                    str(CERT_FILE),
                    "-days",
                    "365",
                    "-nodes",
                    "-subj",
                    "/CN=localhost/O=CS-AI-School-Project",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            continue

    return False


class EducativeAIRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom Python HTTP/HTTPS handler for the Computer Science & AI Portal."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        if self.path == "/api/topics":
            payload = {
                "project": "Computer Science & Its Benefits in the Modern AI Evolution",
                "language": "Python",
                "pillars": [
                    "Algorithms & Complexity",
                    "Computer Architecture & Parallel GPUs",
                    "Python & Data Science Ecosystems",
                    "Cybersecurity & HTTPS Cryptography",
                ],
            }
            self._send_json(200, payload)
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/register":
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            try:
                data = json.loads(raw_body)
            except json.JSONDecodeError:
                data = {}

            is_valid, errors = validate_registration(
                data.get("username", ""),
                data.get("email", ""),
                data.get("password", ""),
                data.get("confirm_password", ""),
            )
            status_code = 200 if is_valid else 400
            self._send_json(status_code, {"valid": is_valid, "errors": errors})
            return

        self._send_json(404, {"error": "Endpoint not found"})

    def _send_json(self, status_code: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run_server(port: int = 8443):
    """Run the educational web portal over HTTPS (with automatic fallback to HTTP)."""
    hello_world()
    has_certs = ensure_https_certificates()
    server_address = ("0.0.0.0", port)
    httpd = http.server.HTTPServer(server_address, EducativeAIRequestHandler)

    if has_certs:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=str(CERT_FILE), keyfile=str(KEY_FILE))
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        protocol = "https"
    else:
        protocol = "http"

    print(f"Serving Computer Science & AI Portal at {protocol}://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
