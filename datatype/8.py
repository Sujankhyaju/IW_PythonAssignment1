# 8. Write a Python program to remove the n th index character from a nonempty
# string.

input_string = input("Enter a string::")
input_string= list(input_string)
print(type(input_string))
input_string.pop()
input_string = "".join(input_string)
print(input_string)