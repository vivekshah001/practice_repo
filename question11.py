
# . Write a program to find the sum of first N natural numbers.

n=int(input("enter a number"))

sum=0

for i in range(0,n+1):
    sum+=i

print("sum of your number is :",sum)