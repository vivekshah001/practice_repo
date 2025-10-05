# . Create a tuple and access its elements. 

tupple_items=(tuple(map(int,input("enter a tupple seperated by space :").split())))

print(tupple_items)
# print(type(tupple_items))


for items in tupple_items:
    print(items)