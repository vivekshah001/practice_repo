# . Write a function to check if a string is an anagram.

def check_anagram(word1,word2):
    return sorted(word1)==sorted(word2)


print(check_anagram("race","care"))
print(check_anagram("sah","sah"))