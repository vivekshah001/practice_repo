# create a car class with attributes(variales) like brand and model.then create an instance(object) of the class

class Car:
    def __init__(self,userbrand,usermodel):
        self.brand=userbrand
        self.model=usermodel




my_car=Car("toyata","motort")
print(my_car.brand)
print(my_car.model)

my_car_=Car("bmw","iseries")
print(my_car_.brand)
print(my_car_.model)