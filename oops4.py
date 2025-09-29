
# modify the car class to encapulate the brand attribute and provide a getter method to access it.

class Car:
    def __init__(self,brand,model):
        self.model=model
        self.__brand=brand


    def get__brand (self):
        return self.__brand + "!"


class Eletriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size


my_car=Car("tpoyata","fortuner")
print(my_car.get__brand())

my_car=Eletriccar("tesla","model s","85kWh")
# print(my_car.battery_size)

print(my_car.get__brand())

