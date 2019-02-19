import socket
import termcolor


PORT = 8080
IP = "212.128.253.79"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    if msg == "EXIT":
        print("Connection finished")
        cs.send(str.encode("exit"))
        cs.close()
    else :
        # printing the message from the client in a different color (exercise 3)
        termcolor.cprint("Message from the client : {}".format(msg), "green")

        # sending the message back (echo-server)
        cs.send(str.encode(msg))
        cs.close()

# Create a socket for connecting to the clients


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT)) # ONE PARAMETER BUT IT IS A TUPPLE

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at : {} , {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept() # will block the server and will wait until the client is connected

    # -- process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)


