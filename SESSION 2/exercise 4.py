input_sequence = input("Introduce a valid DNA sequence : ").lower()
print("Total lenght : ", len(input_sequence))
print("A : ", input_sequence.count("a"))
print("C : ", input_sequence.count("c"))
print("T : ", input_sequence.count("t"))
print("G : ", input_sequence.count("g"))
print("Thank you for using this program")
#exercise 5
def read_file_dna(file):
    counter = 0
    with open(file) as f:
        for line in f:
            line.strip("\n")
            counter += len(line)
    print(counter)


