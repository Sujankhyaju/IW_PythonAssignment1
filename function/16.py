# Write a Python program to square and cube every number in a given list of integers using Lambda.

lst= [x for x in range(1,5)]

square , cube = list(map(lambda x: (x**2),lst)),list(map(lambda x: (x**3),lst))

print(square,cube)