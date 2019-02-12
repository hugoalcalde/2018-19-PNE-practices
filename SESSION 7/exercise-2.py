import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8080
IP = "212.128.253.64"
s.connect((IP, PORT))
def chat():
    sent_message = input("Type your message : ")
    s.send(str.encode(sent_message))
    return chat()
chat()
s.close()
