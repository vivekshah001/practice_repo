
# sum of even number


num=int(input("enter a number :"))
sum=0

for i in range(0,num+1):
    if i%2==0:
        sum+=i
print("sum of even number is :",sum)


