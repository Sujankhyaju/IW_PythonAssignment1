# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

list_items = ['abba','aba','1221','xyz','baab','2222']
count =0
for i in list_items:
    if len(i)>=2 and (i[0]==i[-1]):
        count +=1
print(count)