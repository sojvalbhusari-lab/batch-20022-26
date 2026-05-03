from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class HtmlPreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        request_path = urlsplit(self.path).path
        if request_path in ("/", "/main%20page", "/main page"):
            self.path = "/mainpage.html"
        super().do_GET()

    def guess_type(self, path):
        if path.endswith("/mainpage.html") or path.endswith("/main%20page") or path.endswith("/main page"):
            return "text/html; charset=utf-8"
        return super().guess_type(path)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 3002), HtmlPreviewHandler)
    server.serve_forever()
