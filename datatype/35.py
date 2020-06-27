# 35. Write a Python program to iterate over dictionaries using for loops.

sample_dict={ x:x*2 for x in range(1,5)}

value = sample_dict.values()
print(value)
print("The sum of values of keys is:",sum(value))
