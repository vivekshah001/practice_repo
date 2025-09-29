# demonstarte the use of ()insances TO CHECK IF MY_TESLA IS an instance of car and eletriccar.



class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__model=model
        self.__brand=brand
        Car.total_car += 1


    def get__brand (self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "petrol or diesel"
    

    @staticmethod
    def car_description():
        return "Cars are vehicles that run on roads and are used for transportation."
    
    @property
    def model(self):
        self.__model



class Eletriccar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "electricity"


my_car=Car("tpoyata","fortuner")

print(isinstance(my_car,Car))
print(isinstance(my_car,Eletriccar))

