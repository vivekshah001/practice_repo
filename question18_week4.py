
#  Create a program that counts words, characters, and lines in a paragraph. 

string=(str(input("enter your paragraph :")))

words=string.split()

print("number of words :",len(words))

character=string.replace(" ","")

print("no of character in your paragraph is : ",len(character))

lines=string.splitlines()
print("no of line in your paragrapg :",len(lines))