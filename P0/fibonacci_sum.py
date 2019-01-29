def fibonacci(n) :
    list_fibonacci= [0, 1]
    for elem in range(n-2) :
        i = list_fibonacci[elem] + list_fibonacci[elem+1]
        list_fibonacci.append(i)
    return list_fibonacci


n = int(input("Select the number of elements of the series that you want to add"))
i = 0
list_fibonacci = fibonacci(n)
for elem in list_fibonacci:
     i += elem
print(i)

