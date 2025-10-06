#  Write a program that accepts a sentence and calculates the number of upper and lower case letters. 

a=str(input("enter a string :"))

l_count=0
u_count=0

for ch in a :
    if ch.islower():
        l_count+=1
    else:
        u_count+=1

print(l_count)
print(u_count)