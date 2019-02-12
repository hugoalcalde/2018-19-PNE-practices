""" Example of reading a file located in
our local file system"""

NAME = "mynotes"

myfile = open(NAME, "r")


print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))


