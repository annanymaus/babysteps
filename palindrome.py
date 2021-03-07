 

import sys

n = input ("Enter a string : ")


for i in n:
    if (i == 0):
        sys.exit(1)
    if (n[::1] == n[::-1]):
        print ("The string is a palindrome")
        sys.exit(2)
    else:
        print ("Not a palindrome")
        sys.exit(3)
    