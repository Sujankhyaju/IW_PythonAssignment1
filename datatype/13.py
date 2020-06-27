# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).


input_string =input("enter a comma separated sequence of words::").split(',')


input_string = list(set(input_string))
input_string.sort()
print(input_string)
