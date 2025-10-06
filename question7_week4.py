# Create a Python function to check if a string is a pangram.

a=str(input("enter your string :"))
b=str(input("enter your string :"))

if sorted(a)==sorted(b):
    print("pangram")
else:
    print("not")