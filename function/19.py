# 19.Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce


fibo = lambda n : reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])  


# def fibo(n):
#     a,b=0,1
#     L=[a]
#     if n<1:
#         return "Invalid"
#     else:
#         for _ in range(1,n):
#             c = a+b
#             a=b
#             b=c
#             L.append(a)
#     return L

print(fibo(10))
