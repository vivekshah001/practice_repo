
# Write a program to calculate the sum of digits of a number.

N=str(input("enter 2 digit number :"))

digit=str(N)

first=digit[0]
second=digit[1]
third=digit[2]



first_digit=int(first)
second_digit=int(second)
third_digits=int(third)
sum_of_digits=first_digit+second_digit+third_digits

print("the sum of digits are :",sum_of_digits)