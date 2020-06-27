# 34. Write a Python script to merge two Python dictionaries.

my_dict = { x:x+1 for x in range(1,5)}
sample_dict = {x:x*2 for x in range(6,10)}

my_dict.update(sample_dict)
print(my_dict)