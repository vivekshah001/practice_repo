
# demonstrate polymorphism by defining a method fuel_type in both car and eletriccar classes ,but with different behivaour.



class Car:
    def __init__(self,brand,model):
        self.model=model
        self.__brand=brand


    def get__brand (self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "petrol or diesel"


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
# print(my_car.battery_size)

print(my_car.get__brand())
print(my_car.fuel_type())

