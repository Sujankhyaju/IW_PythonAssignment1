# 16. Write a Python program to sum all the items in a list.


def total(lst_item):
    
    return sum(lst_item)

lst_item =[]

for i in range(10):
    lst_item.append(i)


print(lst_item)
print("The sum of all list item is ::",sum(lst_item))