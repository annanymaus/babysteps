#!/usr/bin/env python3

#Sieve of Eratosthenes

#take input from user
n = int(input("Enter a number : "))

#create list to store all numbers
listofnums = []

#store all numbers to the list created above
for i in range(2,n+1):
    listofnums.append(i)

#loop to jump from one number to the next
for num in listofnums:
    #loop to divide each number with num
    for numdiv in listofnums:
        #condition to prevent the same number from dividing itself
        if num != numdiv:
            #condition to remove all multiples
            if numdiv%num == 0:
                listofnums.remove(numdiv)

#print the result
print(listofnums)
