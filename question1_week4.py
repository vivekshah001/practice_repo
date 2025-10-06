#  Write a Python program to check if a string has all unique characters. 

a=str(input("enter your string :"))

uniquw_char=""

for ch in a:
    if ch in uniquw_char:
        print("duplicate found :",ch)
    elif ch not in uniquw_char:
        uniquw_char+=ch
    else:
        print("all characters are unique")
