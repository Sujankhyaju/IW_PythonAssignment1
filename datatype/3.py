# 3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

input_string = input("Enter a string::")
input_string = input_string.lower()

first_character = input_string[0]
output_string = first_character + input_string[1:].replace(first_character,'$')

print(output_string)


