# 1. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'

input_string = input("Enter a string::")
dict_string= {}
for i in input_string:

    if i.isalpha()== True:
        count=input_string.count(i)
        dict_string.update({i:count})
    
print(dict_string)
