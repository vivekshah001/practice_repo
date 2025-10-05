# . Write a function that returns the factorial of a number. 

num=int(input("enter a number :"))

factor=1

for fac in range(2,num+1):
    factor += factor*fac

print(factor) 