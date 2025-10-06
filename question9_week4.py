
# write a program to check if two strings are anagrams.

a=str(input("enter your string :"))
b=str(input("enter your string :"))

if sorted(a)==sorted(b):
    print("your string are anagrams")
else:
    print("no not")
