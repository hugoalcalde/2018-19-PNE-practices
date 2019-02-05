def count_bases(seq):
    """Counting the number of As in the sequence"""
    a = seq.count("A")
    c = seq.count("C")
    t = seq.count("T")
    g = seq.count("G")
    dict_bases= {"A":a , "C":c , "T":t , "G":g}
    return dict_bases
seq_1 = input("Input the first sequence: ")
seq_2 = input("Input the second sequence: ")
list_sequences = [seq_1 , seq_2]
counter = 0
for element in list_sequences :
    counter += 1
    print("Information of the {}º sequence".format(counter))
    dict_bases = count_bases(element)
    tl = len(element)
    for keys in dict_bases.keys() :
        if tl > 0 :
            perc = round(100.0 * dict_bases[keys] / tl , 1)
            print(keys, ":\n", "counter : {}".format(dict_bases[keys]))
            print("The percentage of {} is {}%".format(keys, perc))
        else :
            perc = 0
    print("The total length is: {}".format(tl))
