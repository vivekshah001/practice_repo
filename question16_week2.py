# . Create a function that checks whether a string is a palindrome. 


# def palidrome_fun(string):  

#     reverse=string[::-1]

# if string==reverse:
#     print("palindrome")
# else:
#     print("not palindroem ")


# palidrome_fun("mam")


def palindrome_fun(string):
    # reverse the string
    reverse = string[::-1]
    
    if string == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"

# taking input from user
user_input = input("Enter your string: ")
print(palindrome_fun(user_input))
