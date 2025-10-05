#  Write a program to find the second highest number in a list. 

l=[1,2,3,4,5,6,7,8,9]

max_l=max(l)

second_l=l.remove(max_l)

print(max(second_l))