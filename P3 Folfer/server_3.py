 # Working with a server that perform operations on a sequence
from seq_4 import Seq
import socket

PORT = 8081
IP = "212.128.253.79"
MAX_OPEN_REQUEST = 5


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at : {} , {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()  # will block the server and will wait until the client is connected

    #  -- process the client request
    print("Attending client: {}".format(address))
    msg = clientsocket.recv(2048).decode("utf-8")
    list_msg = msg.split("\\n")
    list_response = []
    for letter in list_msg[0]:
        if letter != "A" and letter != "C" and letter != "G" and letter != "T" :
            list_response.append("NOT VALID")



