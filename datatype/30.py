# Write a Python script to check whether a given key already exists in a dictionary.
sample_dict = { x:x**2 for x in range(1,5)}
print(sample_dict)

input_key = int(input("Enter any key"))

if input_key in sample_dict.keys():
    print("Already present")
else:
    print("Key Missing")