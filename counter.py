# Count how many times each character appears in the string "dataanalysis" using Counter


from collections import Counter

data="dataanalysis"

count=Counter(data)
print(count)

# Find the 3 most common words in this list using Count


c=Counter(["python", "sql", "python", "data", "python", "sql", "excel"])

print(c.most_common(3))

