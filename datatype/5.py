# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

input_string = input("Enter a string::")

if len(input_string)>=3:
    if input_string.endswith('ing'):
        input_string +='ly'

    else:
        input_string +='ing'

print(input_string)