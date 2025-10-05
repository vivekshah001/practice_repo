#  Write a program to merge two dictionaries. 

dictionary1={"vivek":100,"subham":200,"raj":244,"mannu":340 }
dictionary2={"rajkumar":230,"golu":420}




combined={**dictionary1,**dictionary2}

print(combined)
dictionary1.update(dictionary2)
print(dictionary1)


comnined_2= dictionary1 | dictionary2

print(comnined_2)

# list1=[1,2,3,4,5,5]
# list2=[5,6,7,8,9,0]


# print(list1+list2)