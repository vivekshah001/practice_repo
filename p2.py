
# movie ticket pricing

day=input("enter a day :")

age=int(input("enter your age :"))

price=12 if age >=18 else 8

if day=="wensday":
    price=price-2

print("your tickrt price",price)
