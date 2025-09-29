
# Create a class Student with attributes: name and age.
# Make a method to print the student’s details.
#  Create an object and call that method.


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def fullname(self,name,age):
        print (f"{self.name}{self.age}")

my_std=Student("vivek",19)

print(my_std.fullname("vivek",19))



