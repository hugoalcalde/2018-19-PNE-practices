import json
import termcolor

f = open("person.json", "r")

person = json.load(f)

for element in person :
    termcolor.cprint("Name: ", "green", end= ' ')

    print(element['Firstname'], element['Lastname'])

    termcolor.cprint("Age: ", "green", end = ' ')

    print(element["Age"])

    for i, num in enumerate(element["phoneNumber"]) :
        termcolor.cprint( "Phone {}".format(num["Number"]), "blue", end = ' ')
        termcolor.cprint("Type: ", "red", end = ' ')
        print(num["type"])
    print("\n")



