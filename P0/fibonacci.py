print("printing the n first elements of the fibonacci series")
n = 10
def fibonacci(n) :
    list_fibonacci= [0, 1]
    for elem in range(n-2) :
        i = list_fibonacci[elem] + list_fibonacci[elem+1]
        list_fibonacci.append(i)
    print(list_fibonacci)
fibonacci(n)