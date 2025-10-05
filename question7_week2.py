
# Convert a list into a tuple and vice versa. 

lists=(list(map(int,input("enter a number sepreated by space :").split())))

tupple_convert=(tuple(lists))

print(type(tupple_convert))

list_convert=(list(tupple_convert))

print(type(list_convert))