import socket
import termcolor


# SERVER IP, PORT
IP = "212.128.253.79"
PORT = 8080



while True:


    msg = input("> ")


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()
    if response == "exit" :
        s.close()
    else :
        # Print the server's response
        print("Response:")
        termcolor.cprint(response, "red")

        s.close()