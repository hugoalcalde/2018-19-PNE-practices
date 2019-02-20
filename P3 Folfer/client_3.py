"""This is a code of a client for testing our server"""
import socket



# SERVER IP, PORT
IP = "212.128.253.85"
PORT = 8080

msg = """ACCTTT\nlen\ncomplement\ncountA\npercA\ncountC"""


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))
response = s.recv(2048).decode()
print(response)
s.close()