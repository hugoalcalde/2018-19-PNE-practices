 # Working with a server that perform operations on a sequence
from seq_4 import Seq
import socket

PORT = 8080
IP = "212.128.253.85"
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
    list_response = []
    list_msg = msg.split("\n")
    if list_msg[0] == "" :
        clientsocket.send(str.encode("ALIVE"))
        clientsocket.close()
    else :
        for letter in list_msg[0]:
            if letter != "A" and letter != "C" and letter != "G" and letter != "T" :
                list_response.append("NOT VALID")
        if len(list_response) == 0 :
            list_response.append("OK")
            sequence_client = Seq(list_msg[0])
            list_msg.remove(list_msg[0])
            for element in list_msg :
                print(element)
                if element == "len" :
                    response = sequence_client.len()
                    response = str(response)
                    list_response.append(response)
                elif element == "complement" :
                    response = sequence_client.complement()
                    response = response.strbases
                    list_response.append(response)
                elif element == "reverse" :
                    response = sequence_client.reverse()
                    response = response.strbases
                    list_response.append(response)
                elif element == "countA" :
                    response = sequence_client.count("A")
                    response = str(response)
                    list_response.append(response)
                elif element == "countC":
                    response = sequence_client.count("C")
                    response = str(response)
                    list_response.append(response)
                elif element == "countT":
                    response = sequence_client.count("T")
                    response = str(response)
                    list_response.append(response)
                elif element == "countG":
                    response = sequence_client.count("G")
                    response = str(response)
                    list_response.append(response)
                elif element == "percA":
                    response = sequence_client.perc("A")
                    response = str(response)
                    list_response.append(response)
                elif element == "percC":
                    response = sequence_client.perc("C")
                    response = str(response)
                    list_response.append(response)
                elif element == "percT":
                    response = sequence_client.perc("T")
                    response = str(response)
                    list_response.append(response)
                elif element == "percG":
                    response = sequence_client.perc("G")
                    response = str(response)
                    list_response.append(response)
                else :
                    response = "ERROR"
                    list_response.append(response)

        str_send = ""
        for element in list_response :
            str_send = str_send + element + "\n"
        clientsocket.send(str.encode(str_send))
        clientsocket.close()





