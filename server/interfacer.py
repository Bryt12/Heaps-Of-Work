import json
import http.server

class Interfacer:
    def __init__(self, server):
        pass

    class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def __init__(self, server):
            self.server = server
            super.__init__(self)

        def do_HEAD(self):
            pass
        
        def do_POST(self):
            output_raw = {}

    def __init__(self, u):
        self.user = u
