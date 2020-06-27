# 37. Write a Python program to multiply all the items in a dictionary

sample_dict={ x:x*2 for x in range(1,5)}

values= sample_dict.values()

print(values)

result =1

for value in values:
    result *= value

print(result)