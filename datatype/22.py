# 22. Write a Python program to remove duplicates from a list.

list_items= [1,'a',2,2,1,'a','b',3,4,5]
list_items=list(dict.fromkeys(list_items))
# list_items = list(set(list_items))


print(list_items)