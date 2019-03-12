import http.server
import socketserver
import termcolor

PORT = 8002


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # printing the request line
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/" or (self.path).startswith("/echo") :
            f = open("exercise1.html", "r")
            content = f.read()
            print(self.path)
            msg = (self.path).split("?")
            for element in msg :
                    print(element)
                    echo = element[4:]
                    echo = echo.replace("+", " ")
            if "&" in echo:
                echo = echo.split("&")
                echo = echo[0]
                capital = echo[1]
                print(capital)
            else :
                capital = ""
            f = open("echo.html", "w")
            if len(echo) > 0 :
                if len(capital) == 0
                    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>ECHO MESSAGE</title>\n</head>\n<body>\n<p>This is the echo message :</p>\n<p>{}</p>\n</form>\n<a href="/">[MainPage]</a>\n</body>\n</html>'.format(echo))
                else :
                f.write(
                    '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>ECHO MESSAGE</title>\n</head>\n<body>\n<p>This is the echo message :</p>\n<p>{}</p>\n</form>\n<a href="/">[MainPage]</a>\n</body>\n</html>'.format(echo.upper()))
f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>ECHO MESSAGE</title>\n</head>\n<body>\n<p>This is the echo message :</p>\n<p>{}</p>\n</form>\n<a href="/">[MainPage]</a>\n</body>\n</html>'.format(echo))

                f.close()
                f = open("echo.html", "r")
                content = f.read()
                f.close()
        else :
            f = open("error.html" , "r")
            content = f.read()
            f.close()

        self.send_response(200)

        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))



# Main program


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    print("Serving at PORT : {}".format(PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
