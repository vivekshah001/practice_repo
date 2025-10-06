# . Create a program to find the longest word in a sentence. 


a=str(input("enter a string :"))

a=a.split()
longest_word=""
for i in a:
    if len(i)>len(longest_word):
        longest_word=i
print("longest word is :",longest_word)