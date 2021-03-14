#!/usr/bin/env python3

#program to print the hill number for a given input

num = input("Enter a number : ")

def hillnum(num):
    hill = [ ]
    #defining range where [i-1] and [i+1] fall between 0 and len(num)-1
    for i in range(1,len(num)-1):
        if num[i]>num[i-1] and num[i]>num[i+1]:
            hill.append(num[i])
    return hill

#termination condition if input has less than 3 digits since a 
#minimum of 3 digits is required to form a hill
if len(num)<3:
    print ("number length too short")

c = hillnum(num)

#print hill numbers
print (c) 

#print no. of hill numbers
print (len(c))

