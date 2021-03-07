#!/usr/bin/env python3

n = input("Enter a number : ")

def fact(i):
    if (int (i) >=2):
        c = i * fact(i-1)
        return c
    else:
        return 1

print (fact(int (n)))
