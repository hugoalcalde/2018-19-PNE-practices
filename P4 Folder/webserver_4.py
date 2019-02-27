import socket
import termcolor
import requests

# Change this IP to yours!!!!!
IP = "10.0.2.15"
PORT = 8088
MAX_OPEN_REQUESTS = 5

def process_client(cs):
    f = open("index.html")
    contents = f.read()
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = clientsocket.recv(2048).decode("utf-8")
    print(msg)
    msg = msg.split(" ")
    if msg[1].endswith("/blue") :
        f = open("blue.html")
        contents = f.read()
    elif msg[1].endswith("/pink") :
        f = open("pink.html")
        contents = f.read()
    elif msg[1].endswith("/"):  #as we are using the startswith function it is necessary to use the input order
        f = open("index.html")
        contents = f.read()
    else :
        f = open("error.html")
        contents = f.read()


    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    response_msg = status_line + header + "\r\n" + contents
    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)

