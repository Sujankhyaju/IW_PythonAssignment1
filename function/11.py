# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

func1 = lambda x: x+15

add=func1(2)
print(add)

func2 = lambda x,y : x*y
mul = func2(2,4)
print(mul)

