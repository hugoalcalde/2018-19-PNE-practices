def read_file_dna(file):
    counter_a = 0
    counter_c = 0
    counter_g = 0
    counter_t = 0
    counter_total = 0
    with open(file) as f:
        for line in f:
            line =line.replace("\n", "")
            line =line.replace(" ", "")
            counter_a += line.count("A")
            counter_c += line.count("C")
            counter_g += line.count("G")
            counter_t += line.count("T")
            counter_total += len(line)
        print(" A : ", counter_a, "\n", "C : ", counter_c, "\n", "G : ", counter_g, "\n", "T : ", counter_t, "\n", "TOTAL LENGTH : " , counter_total)


read_file_dna("dna.txt")