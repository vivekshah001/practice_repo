
# Write a program that checks whether a given year is a leap year


year=int(input("enter a year :"))

if (year%400==0) or (year%4==0 and year%100 !=0):
    print("provided year is leap")
else:
    print("year is not leap")  

    