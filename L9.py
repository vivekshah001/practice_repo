# list uniqueness checker
'''
A=["apple","bannana","mango","apple","mango"]

for i in A:
    if A.count(i)>1:
        print(i,"is duplicate")
        
'''

# method 2

items=["apple","bannana","orange","apple","mango"]

uni_item=set()

for item in items:
    if item in uni_item:
        print("duplicate:",item)
        break
    uni_item.add(item)