# transportation mode selection

distance=int(input("enter the distance :"))

if distance <=3:
    print("you should go by walking")
elif distance<=15:
    print("you shoild cover this distance by bike")
elif distance>15:
    print("you should book a car to cover this distance")


