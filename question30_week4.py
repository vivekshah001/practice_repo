# Write a function to remove punctuation from a string. 

string=str(input("enter your string :"))

new_str=""

for items in string:
    if items.isalpha():
        new_str+=items


print("string after removing punctuation :",new_str)