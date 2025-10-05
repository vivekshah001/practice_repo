
# Write a function to remove all punctuation from a string. 

def remove_punctuation(string):
    punctuation=["!","@","#","%","^","&","*"]
    no_punc=" "
    for ch in string:
        if ch  not in  punctuation:
            no_punc+=ch
    return no_punc


# remove_punctuation("vive!")
print(remove_punctuation("vive!"))




# def remove_punctuation(text):
#     punctuation = ["!", "@", "#", "$", "%", "^", "&", "*"]  # you can add more
#     no_punc = ""
#     for ch in text:
#         if ch not in punctuation:
#             no_punc += ch
#     return no_punc

# result = remove_punctuation("vive$")
# print(result)
