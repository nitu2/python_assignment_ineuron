n = int(input("Enter number: "))
a, b = 0,1
if n <0 :
    print("incorrect input")
elif n ==0 :
    print(0)
elif n==1:
    print(1)
else:
    for i in range(1, n):
        c = a+b
        a = b
        b = c
print(b)

#Python Program for How to check if a given number is Fibonacci number?
import math
n = 10
a, b= (5*n*n+4),(5*n*n-4)
sq_a = int(math.sqrt(a))
sq_b = int(math.sqrt(b))
if sq_a*sq_a == a or sq_b*sq_b == b:
    print("It is a fibonacci no.")
else:
    print("It is not a fibonacci no.")

#Python Program for n\’th multiple of a number in Fibonacci Series
n_mul = int(input("Enter number: "))
a, b = 0,1
seq = []
for i in range(1, 10):
    c = a+b
    a = b
    b = c
    seq.append(b)
for i in range(len(seq)):
    if i % n_mul ==0:
        print(i, " is multiple of ", n_mul)

#Program to print ASCII Value of a character
ch = str(input("Enter a character: "))
print(ord(ch))
#Python Program for Sum of squares of first n natural numbers
n = int(input("Enter number: "))
s =0

print(sum([s + i**2 for i in range(1, n+1)]))
#Python Program for cube sum of first n natural numbers
n = int(input("Enter number: "))
s =0
print(sum([s + i**3 for i in range(1, n+1)]))

#Python Program to find sum of array
n = int(input("Enter number: "))
a = range(1, n+1)
print(sum(a))

#Python Program to find largest element in an array
n = 4
a = []
for i in range(1, n+1):
    i = input("Enter number ")
    a.append(i)
print("largest element is ", max(a))

#Python Program for array rotation
a = [1,2,3]
print(a[::-1])

#Python Program for Reversal algorithm for array rotation
a = [1,2,3]
i = len(a)-1
while i+1 >0:
    print(a[i])
    i-=1
    
#Python Program to Split the array and add the first part to the end
import numpy as np
from numpy.lib.function_base import delete
a = [1,2,3,4,5]
b = a[0:3:1]
c = delete(a,[0,1,2], axis =0)
c=list(c)
for i in b:
    c.append(i)
print(c)
