import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    self.path = './public/index.html'
    return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object= MyHttpRequestHandler

PORT = 8080

my_server = socketserver.TCPServer(("",PORT), handler_object)

my_server.serve_forever()