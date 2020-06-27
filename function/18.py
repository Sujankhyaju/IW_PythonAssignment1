# 18. Write a Python program to check whether a given string is number or not using Lambda.
strn = input("Enter a string")

check = lambda s : s.isdigit()

print(check(strn))