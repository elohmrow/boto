from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import simplejson
import time
import re
import os
from create_jira_ticket import ticket

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

        data = simplejson.loads(self.data_string)

        message = data['Message'].rsplit(':::', 1)[0]
        error_level = data['Message'].rsplit(':::', 1)[1]

        p = re.compile('account:\s+(.*?)\+>')
        if p.search(message) is None:
            account = "logs"
        else:
            account = (p.search(message).group(1)).strip()

        logit(account, message, error_level)

        return

def logit(account, message, error_level):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    cwd = os.getcwd()

    # { timestr, [snsTopic], account, [messageID], error_level }
    items = (timestr, "snsTopic", account, "messageID", error_level)
    logfile = open('sns-recvr.log', 'a+')
    logfile.write(",".join(items))
    logfile.write("\n")
    logfile.close()  

    if error_level == 'ERROR':
        # create a JIRA ticket:
        ticket(message)
    elif error_level == 'WARNING':
        return      
    else:
        account = os.path.join(cwd, account)
        if not os.path.isdir(account):
            os.makedirs(account)
        
        with open(os.path.join(account, timestr + ".json"), "w") as outfile:
            simplejson.dump(message, outfile)

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
