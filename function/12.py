# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def mul(num):
    return num * 6

num = 2
print("the multiplication of {} with unknown number is ::{}".format(num,mul(num)))