def fibonacci(n):
    lst = []
    a,b = 0,1
    for i in range(n):
        lst.append(a)
        a,b = b, a+b
    return lst
print(fibonacci(6))