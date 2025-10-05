
# Create a number guessing game.

import random

print("this is a number gussing game (1-10) :")



n=int(input("enter a number :"))

secreate=random.randint(1,10)




if n==secreate:
    print("congrulations you guss the right number")
else:
    print('bad luck try next time')