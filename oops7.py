
# add a static method to the car calass that return a general description of car.



class Car:
    total_car=0

    def __init__(self,brand,model):
        self.model=model
        self.__brand=brand
        Car.total_car += 1


    def get__brand (self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "petrol or diesel"
    

    @staticmethod
    def car_description():
        return "Cars are vehicles that run on roads and are used for transportation."



class Eletriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "electricity"


my_car=Car("tpoyata","fortuner")
print(my_car.get__brand())
print(my_car.fuel_type())


my_car=Eletriccar("tesla","model s","85kWh")

print(my_car.battery_size)

print(my_car.get__brand())

print(my_car.fuel_type())

print("total cars:",Car.total_car)

print(my_car.car_description())