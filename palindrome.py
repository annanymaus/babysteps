#!/usr/bin/env python3

#program to check if a given string is a palindrome
 
n = input ("Enter a string : ")

if (n[::1] == n[::-1]):
    print ("The string is a palindrome")   
else:
    print ("Not a palindrome")
    