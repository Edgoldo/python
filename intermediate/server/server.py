"""
Web Server

Establish a web server using http package that contains HTTPServer and 
BaseHTTPRequestHandler classes. To install http is need to input the 
next command:
    $ pip install http

Manage get requests and make the server locally in code-specified port.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File not found"
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()