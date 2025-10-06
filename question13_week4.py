
#  Write a function to count how many times a substring appears in a string. 



def count(string,sub):
    return string.count(sub)


a=str(input("enter your string :"))
b=str(input("enter your substring :"))


count_sub=count(a,b)
print("your substring appears ",count_sub," times in your string")