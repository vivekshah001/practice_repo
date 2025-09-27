
# leap year checker


year=int(input("enter your year :"))

if (year%400==0) or ( year%4==0 and year%100 !=0 ):
    print("year is leap")
else:print("not a leap year")
