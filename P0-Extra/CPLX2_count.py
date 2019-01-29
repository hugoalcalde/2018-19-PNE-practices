file = "CPLX2.txt"
with open(file) as f :
    counter_a = 0
    counter_c = 0
    counter_t = 0
    counter_g = 0
    for line in f :
            if line.startswith(">") :
                continue
            else:
                counter_a += line.count("A")
                counter_c += line.count("B")
                counter_t += line.count("T")
                counter_g += line.count("G")
    print("A : " , counter_a)


