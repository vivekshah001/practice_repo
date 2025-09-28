# create a function that accepts any number of keyword arguments and prints them in the format key:value
# function with kwargs


def even_gen(**kwarrgs):
    for key,value in kwarrgs.items():
        print(f"{key}:{value}")


even_gen(name="vivek",age=20)