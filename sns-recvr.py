from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import simplejson
import time

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        timestr = time.strftime("%Y%m%d-%H%M%S")
        data = simplejson.loads(self.data_string)
        with open(timestr + ".json", "w") as outfile:
            simplejson.dump(data, outfile)
        print "{}".format(data)

        return

def run(server_class=HTTPServer, handler_class=S, port=9999):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Listening to the topic ... '
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
