"""this is the main program ot the project"""
from seq import Seq
seq_1 = Seq("AGTACACTGGT")
seq_2 = Seq("CGTAAC")
seq_3 = seq_1.complement()
seq_4 = seq_3.reverse()
list_sequences = [seq_1, seq_2, seq_3 , seq_4]
counter = 0
for element in list_sequences :
    counter += 1
    print("\nSequence {} : {}".format(counter, element.strbases))
    print("Length : {}".format(element.len()))
    print("Bases count: A: {} C:{} T:{} G:{}".format(element.count("A") , element.count("C"), element.count("T"), element.count("G")))
    print("Percentage: A: {}% C:{}% T:{}% G:{}%".format(element.perc("A"), element.perc("C"), element.perc("T"),
                                                       element.perc("G")))

