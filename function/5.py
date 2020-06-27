# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

num= int(input("Enter an integer::"))

print("The factorial of {} is {} ".format(num,fact(num)))