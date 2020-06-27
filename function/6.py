# 6. Write a Python function to check whether a number is in a given range.

def rang(num):
    return True if num in range(9) else False

num = int(input("enter a number::"))

print(f"Is {num} in given range 0-8?::",rang(num))