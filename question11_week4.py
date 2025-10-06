
#  Create a program that extracts numbers from a string and returns their sum. 

a=str(input("enter you str :"))

num=0

for items in a:
    if items.isdigit():
        num+=int(items)

print(num)