def count_bases(seq):
    """Counting the number of As in the sequence"""
    a = seq.count("A")
    c = seq.count("C")
    t = seq.count("T")
    g = seq.count("G")
    dict_bases= {"A":a , "C":c , "T":t , "G":g}
    return dict_bases
seq = input("Input the sequence: ")
dict_bases = count_bases(seq)
tl = len(seq)
for keys in dict_bases.keys() :
    if tl > 0 :
        perc = round(100.0 * dict_bases[keys] / tl , 1)
        print(keys, ":\n", "counter : {}".format(dict_bases[keys]))
        print("The percentage of {} is {}%".format(keys, perc))
    else :
        perc = 0
print("The total length is: {}".format(tl))

