

# Create a class Car with attributes brand and model. Create an object of this class and print the values.


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


my_car=Car("toyata","safari")
print(my_car.brand)
print(my_car.model)


# Write a class Student with a constructor that takes name and age. Create two objects and display their details.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

my_std=Student("vivek",19)
print(my_std.name,my_std.age)



# Make a class Calculator with methods add and subtract that take two numbers and return the result.

class Calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2

    def cal(self,number1,number2):
        sum(number1+number2)




mu_cal=Calculator(2,3)
print(mu_cal.sum)