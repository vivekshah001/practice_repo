#  Write a Python program to count the frequency of each word in a file. 

file_name=str(input("enter your file name with extension :"))
with open(file_name,'r') as f:
    a=f.read()
    a=a.split()
    word_count={}
    for i in a:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    print(word_count)