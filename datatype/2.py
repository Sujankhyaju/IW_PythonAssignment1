# 2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

input_string = input("Enter a string")
# output_string =""
if len(input_string)>=2:
    output_string= input_string[:2] + input_string[-2:]

elif len(input_string)==2:
    output_string= input_string + input_string
else:
    output_string="Empty string"

print(output_string)