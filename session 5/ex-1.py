def count_bases(seq):
    """Counting the number of As in the sequence"""
    dict_bases =
    a = seq.count("A")
    c = seq.count("C")
    t = seq.count("T")
    g = seq.count("G")
    dict_bases.update("A", a)
    dict_bases.update("C", c)
    dict_bases.update("T", t)
    dict_bases.update("G", g)
    return dict_bases
seq = input("Input the sequence: ")
dict_bases = count_bases(seq)
tl = len(seq)
for keys in dict_bases.keys() :
    if tl > 0 :
        perc = round(100.0 * dict_bases[keys] / tl , 1)
    else :
        perc = 0
print("The total length is: {}".format(tl))
print("The percentage of As is: {}%".format(perc))
