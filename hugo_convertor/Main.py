
import socketserver
import EntranceHttpRequestHandler


if __name__=='__main__':
    handler = EntranceHttpRequestHandler.EntranceHttpRequestHandler
    httpd = socketserver.TCPServer(("", 8001), handler)
    httpd.serve_forever()