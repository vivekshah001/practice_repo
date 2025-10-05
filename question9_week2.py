# Write a function to count the frequency of elements in a list. 

# lists=(list(map(int,input("enter a number sepreated by space :").split())))

# # print(lists)
# def count_frequency():


# new_list={}

# for items  in lists:
#     if items in new_list:
#         new_list[items]+=1
#     else:
#         new_list[items]=1
#         return items
        



   


# print(f"there a {count} in this list")
# # print(new_list)



def count_frequency(lst):
    freq = {}  # empty dictionary to store counts
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Input from user
lists = list(map(int, input("Enter numbers separated by space: ").split()))

# Call function and print
frequency = count_frequency(lists)
print("Frequency of elements:", frequency)
