
# create a program to count the number of vowels in a string


# vowel count in a string
s = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
