# 11. Write a Python program to count the occurrences of each word in a given
# sentence.


input_string = input("Enter a sentence")
input_string = input_string.split()

output = {}

for i in input_string:
    count = input_string.count(i)
    output.update({i:count})

print(output)