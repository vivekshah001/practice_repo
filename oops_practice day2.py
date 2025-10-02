
# Create a class called Car with two attributes: brand and model.
# Use a constructor (__init__) to initialize these values.
# Create an object of the class and print the car’s brand and model.


# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# my_car=Car("tata","safari")

# print(my_car.model)
# print(my_car.brand)



# Create a class Student that stores a student’s name and age.
# Write a method called display_info() that prints both values in a readable format.
# Create one student object and call the method.

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_info(self,name,age):
#         return(f"studet name is {name},and he is {age}y/s old")

# my_info=Student("vivek",19)

# print(my_info.display_info("vivek",19))


# Rectangle – Area and Perimeter
# Create a class Rectangle with attributes length and width.
# Add two methods:
# area() → returns the area of the rectangle
# perimeter() → returns the perimeter
# Create an object and use both methods.


class Rectangle:
    def __init__(self, lenght,width):
        self.lenght=lenght
        self.width=width

    def area(self,lenght,width):
        self.width=width
        self.lenght=lenght
        return f"area is :",lenght*width
    
    def perimeter(self,lenght,width):
        self.lenght=lenght
        self.width=width
        return f"perimeter is :",2*(lenght+width)
    

rect=Rectangle(19,10)
print(rect.area(19,10))
