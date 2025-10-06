#  Handle a ZeroDivisionError using try-except. 

try:
    a=10
    b=0
    div=a/b
    print(div)
except ZeroDivisionError:
    print("you can divide a number with 0")