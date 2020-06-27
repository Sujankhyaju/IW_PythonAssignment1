# 10. Write a Python program to print the even numbers from a given list.

def even(lst):
    output_list =[]
    for i in lst:
        if i % 2 == 0:
            output_list.append(i)
        else:
            continue
    
    return output_list
            

sample_list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even(sample_list))
