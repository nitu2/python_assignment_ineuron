# Write a Python program to find those numbers which are divisible by 7
# and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500, 2701):
    if i % 7 and i % 5 ==0:
        print(i)

#Python program to add two numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Sum of two numbers is: {} + {} = {}".format(a,b,a+b))

#Maximum of two numbers in Python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a > b:
    print(a, "is greater")
elif b>a:
    print(b, "is greater")
else:
    print("both are equal")

#Python Program for factorial of a number
a = int(input("Enter number: "))
fact =1
for i in range(1,a+1):
    if a == 0 or a ==1:
        print(1)
    elif a <0 :
        print(0)
    else:
        fact = fact * i
print(fact)

#Python Program for simple interest
p, r, t = 5000, 5, 10
print("Simple interest for principal amount {} at rate {}, for time period {} is {} ".format(p, r, t,
(p*r*t)/100 ))

#Python Program for compound interest
p, r, t = 10000, 10.25, 5
A = (p*(pow((1+r/100), t)))._round_()
ci = A-p
print("Compound interest for principal amount {} at rate {}, for time period {} is {} ".format(p, r, t,ci))

#Python Program to check Armstrong Number
a = 663
temp = a
length = len(str(a))
sum =0
while temp > 0:
    digit = temp%10
    sum = sum + pow(digit,length)
    temp = temp// 10
    if sum == a:
        print("it is an amstrong number")
    else:
        print("it is not an amstrong number")

# Python Program for Program to find area of a circle
r= int(input("Enter radius: "))
PI = 3.14
area = PI*(pow(r,2))
print("Area of circle is {}" .format(area))

#Python program to print all Prime numbers in an Interva
for i in range(0, 100):
    if i > 1 :
        for j in range(2, i):
            if i % j ==0:
                break
            else:
                print(i)
#Python program to check whether a number is Prime or not
a = int(input("Enter number: "))
if a > 1 :
    for j in range(2, a):
        if a % j ==0:
            print("not a prime number")
            break
        else:
            print("is a prime number")