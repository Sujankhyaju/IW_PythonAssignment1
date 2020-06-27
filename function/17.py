# 17. Write a Python program to find if a given string starts with a given character using Lambda.

sample_str = input("Enter a string::")
start_char = input("Enter a character to find if the string starts with it::")

# lst = [1,2,3]
check = lambda start_char, sample_str: sample_str.lower().startswith(start_char.lower())

print(check(start_char,sample_str))