# Q16. Create a program to filter out all non-alphabetic characters from a string. 


string=str(input("enter your string :"))

filter_string=""

for ch in string:
        if ch.isalpha():
                filter_string+=ch
    # if ch not in ["@","!","#","%""&","*"]
        


print(filter_string)