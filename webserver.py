#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer


def start(port):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)
    print "Webserver started at port", port
    httpd.serve_forever()
