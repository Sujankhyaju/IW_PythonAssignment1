# 17. Write a Python program to multiplies all the items in a list.

def mult(lst_item):
    output_multi =1
    for item in lst_item:
        output_multi *= item
    return output_multi

lst_item = []
for i in range(1,5):
    lst_item.append(i)
print(lst_item)
print("the multiplication of all list items is ::",mult(lst_item))