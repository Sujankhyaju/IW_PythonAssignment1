# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.


list_items = [(5,2),(1,4),(9,5),(2,0),(3,1)]
output_items = []

print("List of items::",list_items)

for i in range(len(list_items)):
    list_items[i]=list_items[i][::-1]

list_items.sort()

for i in range(len(list_items)):
    output_items.append(list_items[i][::-1])

print("list of output::",output_items)