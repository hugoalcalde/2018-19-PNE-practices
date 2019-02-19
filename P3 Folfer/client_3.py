"""This is a code of a client for testing our server"""
import socket



# SERVER IP, PORT
IP = "212.128.253.79"
PORT = 8081



while True:


    msg = input("> ")


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))
    s.close()