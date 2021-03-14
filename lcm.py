#!/usr/bin/env python3

#take an input for a and b from user
a = int(input("Enter a : "))
b = int(input("Enter b : "))

#recursive function to calculate gcd
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

#formula to calculate lcm of two numbers
result = int((a*b)/gcd(a,b))

#print result
print("LCM of given numbers : " + str(result))
