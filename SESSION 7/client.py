"""Creating our first socket"""

import socket
# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # af_inet means that your socket connects to internet

print("Socket created")

PORT = 8080
IP = "212.128.253.64"

# Connect to the server

s.connect((IP, PORT))

# Sending a message to the server

s.send(str.encode("HELLO FROM MY CLIENT"))

msg = s.recv(2048).decode("utf-8")
print("Message from the server : ")
print(msg)

s.close()


print("the end")

