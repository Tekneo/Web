import http.server
import socketserver

Port = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", Port), Handler) as httpd:
	print("Server at Port", Port)
	httpd.serve_forever()
