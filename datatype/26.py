# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.


sample_string = "item"
sample_list = list( str(x) for x in range(3) )
output=[]
for i in sample_list:
    output += sample_string


print(output)