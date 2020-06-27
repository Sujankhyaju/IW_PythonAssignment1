# Write a Python program to find intersection of two given arrays using Lambda.

lst1=[x for x in range(5)]
lst2=[x for x in range(2,10)]
inter = list(filter(lambda lst1: (lst1 in lst2),lst1))

print(inter)

# lst =[]
# for i in range(len(lst1)):
#     if lst1[i] in lst2:
#         lst.append(lst1[i])
# 
# print(lst)