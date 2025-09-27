

# find the first non repetitive char

chara ="boomber"

for i in chara:
    if chara.count(i)==1:
      print(i)
      break