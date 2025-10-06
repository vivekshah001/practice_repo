#  Create a program that removes all duplicate characters from a string.

a=str(input("enter your string :"))

uni_str=""

for ch in a:
    if ch not in uni_str:
        uni_str+=ch


print(uni_str)
