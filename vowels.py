#!/usr/bin/env python3

n = input ("Enter a string : ")

def vcount(i, j):
    if (j == len(i)):
        return 0
    if (i[j] == 'a' or i[j] == 'e' or i[j] == 'i' or i[j] == 'o' or i[j] == 'u'):
       return vcount(i, j+1) + 1
    else:
        return vcount(i, j+1)
    
print (vcount(n, 0))