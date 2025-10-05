
#  Check if a given year is a leap year or not.

year=int(input("enter your year :"))

if (year%4==0 and year%100 !=0) or (year % 400==0) :
    print("year is leap")
else:
    print("year is not leap")
