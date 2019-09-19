# Enrique Pesantez wrote this Programming on 9/19/19
# This program su,s the value of pi


def piApx(num):
    
    # formula
    sumN = 0
    denom = 1
    n = 4
    for i in range(num):
        sumN = (n/denom) + sumN
        denom = denom + 2
        n = -1 * n
    print("The value of π is approximately", sumN)


piApx(eval(input("Enter num:")))
