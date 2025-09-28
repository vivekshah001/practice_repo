# here we will do some args and kwargs practice question


# write a function using *args that returns the sum of all number passed 

def sum_of_all(*args):
     return sum(args)

print(sum_of_all(1,2,3))


# write a function using *args that returns the larges number passed



def largest_number(*args):
     return max(args)


print(largest_number(1,6,9,3))




# write a function using *args that join multiple strings into one single string with space




def join_str(*args):
     return " ".join(args)

print(join_str("vivek","sah"))



# write a function using **kwargs that print a student name,age and course.

def school_std(**kwargs):
     for key,value in kwargs.items():
            print(f"{key}:{value}")
          
school_std(name="vivek",age=20)





#  write a function using **kwargs that returns a dictionary of product  details.

def pro_details(**kwargs):
     for key,value in kwargs.items():
          print(f"{key}:{value}")


pro_details(mobile=20000,laptop=199900)