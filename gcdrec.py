#!/usr/bin/env python3

#program to find gcd of two given numbers

#take an input for a and b from user
a = input("Enter a : ")
b = input("Enter b : ")

#recursive function to calculate gcd
def gcd(a,b):
    if int(b)==0:
        return a
    return gcd(int(b),int(a)%int(b))

#print result
print(gcd(a,b))