#  Write a script that extracts hashtags from a tweet.


script=str(input("enter your tweet :"))

remove_hastag=script.replace("#","")

print("your tweet after removing hastag :",remove_hastag)
