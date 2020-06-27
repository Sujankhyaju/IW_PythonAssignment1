# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.


list_item =[{'d':2,'c':1},{1,2},(0,1,2),{}]


print(list_item)

for i in range(len(list_item)):

    if isinstance(list_item[i], dict):

        if bool(list_item[i]) == True:
            print("False, all dictionaries in a list are not empty")
            break
        else:
            print("True,  all dictionaries in a list are empty")
            break
