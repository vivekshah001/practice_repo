# Create a program that finds the first non-repeating character in a string.
a=str(input("enter a string :"))
for i in a:
    if a.count(i)==1:
        print("first non-repeating character is :",i)
        break