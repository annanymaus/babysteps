#!/usr/bin/env python3

#program to find factorial of a given number

#take input from user
n = input("Enter a number : ")

#recursive func. to calculate factorial
def fact(i):
    #base check for 0! and 1!
    if (int (i) < 2):
        return 1

    #calculation for numbers greater than/equal to 2    
    c = i * fact(i-1)
    return c

#print the result
print (fact(int (n)))
