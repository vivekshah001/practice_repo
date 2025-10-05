
# . Check whether a character is a vowel or consonant.

character=str(input("enter a character :"))

for i in character:
    if i in ["a","e","i","o","u"]:
        print("vowel")
    else:
        print("consonent")