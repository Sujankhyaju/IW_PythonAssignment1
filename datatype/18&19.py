# 18. Write a Python program to get the largest number from a list.
# 19. Write a Python program to get the smallest number from a list.


lst_items= [12,2,3,56,12,25]

lst_items.sort(reverse=True)
print("The largest number of the list is::{}\n The smallest number of the list is::{}".format(lst_items[0],lst_items[-1]))