# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def concat(str1,str2):
    strng = str1
    str1 = str1.replace(str1[:2],str2[:2])
    str2 = str2.replace(str2[:2],strng[:2])
    strng = str1 + " " + str2

    return strng



input_string1 = input("Enter first string::")
input_string2 = input("Enter second string::")
print(concat(input_string1,input_string2))
