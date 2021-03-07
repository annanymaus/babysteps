#!/usr/bin/env python3

import sys

n = input("Enter a string : ")

def palindrome(i):
    if (len(i)<2):
        print ("This string is a palindrome.")
        sys.exit(0)
    if (i[0] == i[-1]):
        return palindrome(i[1:-1])
    else:
        print ("Not a palindrome")
        sys.exit(1)

print(palindrome(n))

    
