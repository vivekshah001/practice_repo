#  Create a program that removes duplicates from a list. 

list=list(map(int,input("enter a list sepreated by space :").split()))

# print(list)

# new=(set(list))
# print(new)

new_list=[]

for items in list:
    if items not in new_list:
        new_list.append(items)



print(new_list)