#  Create a program to print the Fibonacci series up to N terms


N=int(input("enter a number :"))

a=0
b=1

print(a,b,end=" ")
for i in range(N-2):
    c=a+b
    print(c ,end=" ")
    a=b
    b=c 