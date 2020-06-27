# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique(lst):
    out_list=[]
    for i in lst:
        if i in out_list :
            continue
        else:
            out_list.append(i)
    
    return out_list 

sample_list = [1,2,3,3,4,3,3,4,5]

print(unique(sample_list))
