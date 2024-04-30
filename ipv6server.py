from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

#print(socket.getaddrinfo('localhost','http'))
server = HTTPServerV6(('::', 80), SimpleHTTPRequestHandler)
server.serve_forever()

