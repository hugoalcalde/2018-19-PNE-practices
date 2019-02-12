"""this is a program to interact from client to server"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8080
IP = "212.128.253.64" #this is the IP of the computer that is working as a client
s.connect((IP, PORT))
sequence = input("Please select the sequence you want to work with : ")
s.send(str.encode(sequence))
msg = s.recv(2048).decode("utf-8")
print(msg)


