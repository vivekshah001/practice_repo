
# create an eletriccar class that inherits from the car class and has an additional attribute battery_size.


class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand


class Eletriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size


my_car=Car("tpoyata","fortuner")
print(my_car.brand)

my_car=Eletriccar("tesla","model s","85kWh")
print(my_car.battery_size)
