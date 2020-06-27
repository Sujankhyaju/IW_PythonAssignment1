# 13. Write a Python program to sort a list of tuples using Lambda.

sortTuple = lambda lst: sorted(lst,key=lambda ls: ls[0])

sample_list = [(1,2),(5,2),(0,2),(7,0),(2,1),(0,0)]

print(sortTuple(sample_list))


