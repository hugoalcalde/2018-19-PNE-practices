"""using the Seq class and servers"""

from seq_2 import Seq
import socket


def client(): #this function will ask the user to enter a sequence
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8080
    IP = "212.128.253.64" #this the IP of the teacher's computer, but it also works with other IPs with a server
    s.connect((IP, PORT))
    sequence = input("Please select the sequence you want to work with : ")
    sequence = Seq(sequence)
    complement = sequence.complement()
    reverse = sequence.reverse()
    complement_sequence = complement.strbases #we want to send the sequence (letters) not the object
    reverse_sequence = reverse.strbases #same as above
    s.send(str.encode("The complement sequence of the input sequence is : "))
    s.send(str.encode(complement_sequence))
    s.send(str.encode("\nThe reverse sequence of the input sequence is : "))
    s.send(str.encode(reverse_sequence))
    s.close()
    return client()

client()


