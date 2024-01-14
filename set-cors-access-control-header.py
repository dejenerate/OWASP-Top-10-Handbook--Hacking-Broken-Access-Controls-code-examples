#!/usr/bin/env python3
# encoding: utf-8

from http.server import HTTPServer, SimpleHTTPRequestHandler
from flask import request

whitelistedDomains = ["https://allowed-domain1.com", "https://allowed-domain2.com"]


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        originHeader = request.environ['HTTP_ORIGIN']
        if 'HTTP_ORIGIN' in request.environ and originHeader in whitelistedDomains:

            self.send_header('Access-Control-Allow-Origin', originHeader)
        return super(CORSRequestHandler, self).end_headers()


httpd = HTTPServer(('https://allowed-url.com', 80), CORSRequestHandler)
httpd.serve_forever()
