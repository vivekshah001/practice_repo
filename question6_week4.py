# . Write a program that takes a string and returns the string in reverse order without using [::-1]



string=str(input("enter a string :"))

rev_str=" "

for ch in string:
    rev_str=ch + rev_str

print(rev_str)
