
import socketserver
import gitbook_site.EntranceHttpRequestHandler as EH


if __name__=='__main__':
    handler = EH.EntranceHttpRequestHandler
    httpd = socketserver.TCPServer(("", 8001), handler)
    httpd.serve_forever()