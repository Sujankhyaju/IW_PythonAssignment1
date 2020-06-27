# 45. Write a Python program to find the index of an item of a tuple.

sample_tuple = (1,2,3,4,5)

print(sample_tuple)
item = int(input("Enter an item from given tuple::"))

print("Index of input item is:",sample_tuple.index(item)) if item in sample_tuple else print("Invalid")



