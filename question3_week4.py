#  Write a script to count the frequency of each character in a string.

a=str(input("enter a string :"))

d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)