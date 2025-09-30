# Write a Python program to create a class Car with attributes brand and model, and create an object of it.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_Car=Car("tata","safari")
print(my_Car.brand)
print(my_Car.model)


# Create a class Student with a method display_info() that prints the student's name and age.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


my_student=Student("vivek",18)
print(my_student.age)
print(my_student.name)


# Create a class Student with a method display_info() that prints the student's name and age.


class Student:
    def __init__(self,name,age):  # first method ka name sirf __init__ ho sakte hai na
        self.name=name
        self.age=age

my_info=Student("vivek",18)



print(my_info.name)
print(my_info.age)



# Create a class Circle with a method to calculate area and circumference.


import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def calculate_area(self,radius):
        self.radius=radius

        return f"area is ",math.pi*radius**2
    
    def calculate_circumference(self,radius):
        self.radius=radius

        return f"circumference is",2*math.pi*radius
 

print(Circle.calculate_area(Circle,7))
print(Circle.calculate_circumference(Circle,7))

        

       
# Write a program to demonstrate single inheritance: Create a class Animal and a subclass Dog that inherits from it.



class Animal:
    def __init__(self):
        return f"hey dogge"
    

class Dod(Animal):
    def function_d(self):
        return f"my name is dogge"

# iske baad samajh nhi aaya 


# Create a class Employee with private attribute salary. Use getter and setter methods to access and modify it.



class Employee:
    def __init__(self,salary):
        self.__salary=salary


    def get_salaty(self):
        
        return self.__salary + "only"




my_sal=Employee(9999)
print(Employee.get_salaty(Employee))

        







# we can access private attributes with getter method just by using :__class__attribute



class Account:
    def __init__(self, balance):
        self.__balance = balance   # private attribute



    def get__balance(self):
        return   self.__balance

acc = Account(1000000000)
# print(acc.get__balance())


# # direct access using name mangling
print(acc._Account__balance)   # ✅ prints 1000




























