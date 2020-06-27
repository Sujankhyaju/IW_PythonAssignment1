# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).


No_of_items = int(input("Enter no. of items in dictionary::"))
sample_dict = { x:x*x for x in range(1,No_of_items)}

print(sample_dict)