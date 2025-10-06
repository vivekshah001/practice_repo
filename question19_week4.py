#  Write a program that accepts a string and counts vowels and consonants. 

string=str(input("enter your string :"))

count_vowel=0
count_consonent=0


for items in string:
    if items in ["a","e","i","o","u"]:
        count_vowel+=1
    else:
        count_consonent+=1


print("no of vowels in uour string :",count_vowel)
print("no of consonent in your string :",count_consonent)