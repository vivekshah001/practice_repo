#   Write a program to count the number of words starting with a vowel in a string. 


string=str(input("enter your string :"))

count=0

for items in string.split():
    if items.startswith("a" or "e" or "i" or "o" or "u"):
        count+=1


print(count)