# 14. Write a Python program to sort a list of dictionaries using Lambda.

lst = [{'name':'sujan','add':'Bkt'},{'name':'khyaju','add':'ktm'},{'name':'ab','add':'Ltr'}]

get_sorted_dict =lambda lst: sorted(lst,key=lambda lst: lst['name'])


print(get_sorted_dict(lst))