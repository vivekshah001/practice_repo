# prime number checker


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        # Ye else for loop ka hai, sirf tab execute hoga agar loop break na ho
        print(num, "is prime")
else:
    print(num, "is not prime")

         


