# Enrique Peantez Created this Program on 9/19/19
# This program runs the fibonacci sequence


def fibonacci(n): 
    a = 0
    b = 1
    for i in range(0, n+1):
        if i == 0: 
            print(a) 
        elif i == 1: 
            print(b) 
        else: 
            c = a + b 
            a = b 
            b = c 
            print(b)


fibonacci(int(input("What nth number:")))
