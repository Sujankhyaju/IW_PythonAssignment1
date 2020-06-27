# 3. Write a Python function to multiply all the numbers in a list.

def mul(sample_list):
    result=1
    for item in sample_list:
        result *= item
    return result

sample_list = [8, -2, 3, -1, 7]

print("Multiplication of all the numbers::",mul(sample_list))