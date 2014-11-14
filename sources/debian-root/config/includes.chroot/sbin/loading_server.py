from os import curdir, sep
from os.path import join as pjoin

from http.server import BaseHTTPRequestHandler, HTTPServer

class StoreHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        with open('/var/www/loading.html') as fh:
                                                self.send_response(200)
                                                self.send_header('Content-type', 'text/html')
                                                self.end_headers()
                                                self.wfile.write(fh.read().encode())


server = HTTPServer(('', 6000), StoreHandler)
server.serve_forever()
