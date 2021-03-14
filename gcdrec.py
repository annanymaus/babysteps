#!/usr/bin/env python3

#program to find gcd of two given numbers

#take an input for a and b from user
a = int(input("Enter a : "))
b = int(input("Enter b : "))

#recursive function to calculate gcd
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

#print result
print(gcd(a,b))