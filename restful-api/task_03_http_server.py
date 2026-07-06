#!/usr/bin/python3
"""Simple API built with Python's http.server module."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler that routes GET requests to different endpoints."""

    def do_GET(self):
        """Handle GET requests based on the request path."""
        if self.path == "/":
            self._send_text_response(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)

        elif self.path == "/status":
            self._send_text_response(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json_response(200, info)

        else:
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, status_code, message):
        """Send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """Send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server and keep it running until interrupted."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port {}...".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()


if __name__ == "__main__":
    run()
