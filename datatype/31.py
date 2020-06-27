# Write a Python program to iterate over dictionaries using for loops.
sample_dict = { x:x**2 for x in range(1,10,2)}
print("keys---values")
for key,value in sample_dict.items():
    
    print(key,'----',value)