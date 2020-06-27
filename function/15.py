# 15. Write a Python program to filter a list of integers using Lambda.

lst =[1,'a',2,'b','e',0,3,'s']

filt = list(filter(lambda x: (type(x) is int),lst))
print(filt)


