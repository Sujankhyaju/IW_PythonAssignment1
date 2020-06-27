# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

sample_dict = { x:x**2 for x in range(1,16)}

print(sample_dict)