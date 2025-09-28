# create a function that returns both the area and the circumference of a circle when radius is given

import math

def radius(num):
    area= math.pi*num**2
    circ=2*math.pi*num
    return area,circ


a,c =(radius(5))


print("area is:",a.__round__(3),"circumference is :" ,c.__round__(3))




