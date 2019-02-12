import socket
def chat():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8080
    IP = "212.128.253.80" #exercise 4 has been done by changing this IP to my own IP (it worked)
    s.connect((IP, PORT))
    sent_message = input("Type your message : ")
    s.send(str.encode(sent_message))
    return chat()
chat()
s.close()