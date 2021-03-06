#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Creates a local HTTP server on the curent directory.

'''

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import webbrowser

def main():
    handlerClass = SimpleHTTPRequestHandler
    serverClass = BaseHTTPServer.HTTPServer
    protocol = "HTTP/1.0"


    if(sys.argv[1:]):
        port = int(sys.argv[1])
    else:
        port = 8000

    serverAdress = ("127.0.0.1", port)

    handlerClass.protocol_version = protocol
    httpd = serverClass(serverAdress, handlerClass)

    sa = httpd.socket.getsockname()

    print("\tServing on http://" + str(sa[0]) + ":" + str(sa[1]) )
    print("\tPress Ctrl+c to stop...")

    # open the web browser
    webbrowser.open("http://" + str(sa[0]) + ":" + str(sa[1]) )

    httpd.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("\tNo more serving.")
        exit()
