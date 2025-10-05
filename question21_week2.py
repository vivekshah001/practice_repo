#  Create a list comprehension to get squares of all even numbers in a range.


square=[x**2 for x in range(1,10) if x%2==0]
print(square)