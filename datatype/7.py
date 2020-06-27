# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.

words = []
length = []
len_list = int(input("Enter a length of a list:: "))
print("Insert words in the list::")
for i in range(len_list):
    i = input("")
    words.append(i)
    length.append(len(i))
words.sort()
length.sort()
print(words)
print("The length of longest word is {}".format(length[-1]))
