#!/usr/bin/env python3

#program to find the nth fibonacci number using recursion (and no for loops)

import sys

#function definition
def fib(p):
    if (p == 0):
        return 0
    elif (p == 1):
        return 1
    else:
        #recursive equation
        c = fib(p-1) + fib(p-2)
        return c 

#take an input
print ("Enter a number : ")
n = input()
print()              #print empty line
print("˜˜˜˜˜˜˜˜˜˜˜") #aesthetic element
print()              #print empty line

#if the input is a negative integer
try:
    if (int(n) < 0):
        print("i don't need this kind of negativity in my life.")
        sys.exit(2) #program ends
#if the input is any other character apart from numbers
except SystemExit:  #to handle SystemExit exception thrown by sys.exit() in try
    sys.exit(2)
except:
    print("input is clearly not a number -___- ")
    sys.exit(3) #program ends

#printing the final result
print(fib(int(n)))
sys.exit(4)
