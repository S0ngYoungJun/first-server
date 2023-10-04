from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("안녕하세요".encode('utf-8'))

httpd = HTTPServer(('127.0.1.0.1', port), SimpleHTTPRequestHandler)
print(f'Server running on port:{port}')
httpd.serve_forever()