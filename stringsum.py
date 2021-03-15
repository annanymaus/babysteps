#!/usr/bin/env python3

#program to calculate the sum of digits in string of space-separated numbers

#take input from user and split it into a list of strings
n = input("Enter numbers separated by spaces : ").split()

#define sum and initialise to 0
sum = 0

for i in range(len(n)):
    #convert each list element to int
    n[i] = float(n[i])
    #calculate sum
    sum = sum + n[i]

#print sum
print(sum)
