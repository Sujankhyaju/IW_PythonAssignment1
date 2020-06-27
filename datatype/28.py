# 28. Write a Python script to add a key to a dictionary.


Sample_Dictionary = {0: 10, 1: 20}
keys = [x for x in range(2,5)]
values=[y for y in range(10,40,10)]

for i in range(len(keys)):
    Sample_Dictionary.update({keys[i]:values[i]})

print(Sample_Dictionary)