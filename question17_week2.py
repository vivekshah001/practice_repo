#  Write a function to count vowels in a string. 


def vowel_counter(string):
    count=0
    for ch in string:
        if ch in ["a","e","i","o","u"]:
            count+=1
    print(f"there are {count} in your string ")

vowel_counter("abcde")