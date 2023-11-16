from http.server import *
import socketserver


class myhandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            return SimpleHTTPRequestHandler.do_GET(self)


PORT = 5000

handler = myhandler


myserver = socketserver.TCPServer(("", PORT), handler)
myserver.serve_forever()
print(f"Server started at {PORT}")
