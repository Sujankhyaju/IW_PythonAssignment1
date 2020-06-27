# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :

input_string = input("Enter a string like '[{{}}]::")
append_string = input("Enter a word::")
center = int(len(input_string)/2)

input_string = input_string[:center]+ append_string + input_string[center:]
print(input_string)