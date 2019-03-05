import http.server
import socketserver

PORT = 8004


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line : " + self.requestline)
        print("Cmd : " + self.command)
        print("Path: " + self.path)


        if self.path == "/" :
            f = open("index.html")
            content = f.read()
        else :
            f = open("pink.html") #no me funciona
            content = f.read()
        f.close()

        self.send_response(200);
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(content)))

        self.end_headers()

        self.wfile.write(str.encode(content))
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port ", PORT)

    httpd.serve_forever()

