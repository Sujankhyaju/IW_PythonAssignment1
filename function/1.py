# 1. Write a Python function to find the Max of three numbers.

def Greatest(num1,num2,num3):
    if num1<num2:
        return num3 if num2<num3 else num2
    elif num2<num3:
        return num1 if num3 < num1 else num3
    else:
        return num3 if num1<num3 else num1

print("----------Finding Greatest Number----------------")
num1,num2,num3= int(input("Enter 1st numbers::")),int(input("Enter 2nd numbers::")),int(input("Enter 3rd numbers::"))

print("The greatest number is::",Greatest(num1,num2,num3))



