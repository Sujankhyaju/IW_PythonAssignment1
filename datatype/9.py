# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged


input_string = input("Enter a string::")

# output_string = input_string[-1] + input_string[1:-1] +input_string[0]


for i in range(len(input_string)):
    if i == 0:
        output_string = input_string[-1]
    elif i < (len(input_string)-1):
        output_string += input_string[i]
    else:
        output_string += input_string[0]
        

print(output_string)