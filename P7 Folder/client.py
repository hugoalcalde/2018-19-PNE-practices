

import requests
import http.client
import json
import sys
SERVER = "http://rest.ensembl.org"
PORT = 8080

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))
server = "http://rest.ensembl.org"
ext = "/sequence/id"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
r = requests.post(server + ext, headers=headers, data='{ "ids" : ["ENSG00000165879 "]}')

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
print(repr(decoded))
dictionary = decoded[0]
print(dictionary["seq"])

# performing some calculations with the sequence

sequence = dictionary["seq"]
number_bases = len(sequence)
dictionary_number = {}
dictionary_number["T"] = sequence.count("T")
dictionary_number["A"] = sequence.count("A")
dictionary_number["C"] = sequence.count("C")
dictionary_number["G"] = sequence.count("G")
max_number = max(dictionary_number["T"], dictionary_number["A"], dictionary_number["C"], dictionary_number["G"])
for element in dictionary_number.keys():
    if dictionary_number[element] == max_number:
        popular_base = element
perc_popular = round((dictionary_number[element] / number_bases) * 100)
def perc_base(sequence, base):
        tl = len(sequence)
        counter = sequence.count(base)
        perc = round((counter / tl) * 100, 1)
        return perc
dictionary_perc = {}
dictionary_perc["A"] = perc_base(sequence, "A")
dictionary_perc["T"] = perc_base(sequence, "T")
dictionary_perc["G"] = perc_base(sequence, "G")
dictionary_perc["C"] = perc_base(sequence, "C")
print("There are {} bases in the sequence".format(number_bases))
print("There are {} T bases in the sequence".format(dictionary_number["T"]))
print("The most popular base in the sequence is {} with a percentage of {} %".format(popular_base, perc_popular))
for element in dictionary_perc:
    print("The percentage of {} is : {}".format(element, dictionary_perc[element]))




