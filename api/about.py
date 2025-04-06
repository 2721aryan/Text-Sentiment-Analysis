from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the static HTML page
        try:
            public_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
            with open(os.path.join(public_dir, 'about.html'), 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())
        return 