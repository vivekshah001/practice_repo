#  Write a function to find common elements in two lists. 

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

# def function_common():
#     for items in list1:
#         if items in list2:
#             print(f"{items} are common in both lists")



# function_common()



def common_function(list1,list2):
    return list(set(list1) & set(list2))

print(f"common elements are ",common_function(list1,list2))