
# Create a program to print all Armstrong numbers between 1 to 1000. 

num=(input("enter a number :"))




digits = [int(d) for d in str(num)]

digit_len=len(digits)


# print(digits)

for i in digits:
    kk=i**digit_len
    sum=sum(kk)

    if sum==int(num):
        print("P")
    else:
        print("N")