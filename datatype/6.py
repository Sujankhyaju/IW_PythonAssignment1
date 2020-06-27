# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string

input_string = "The Lyrics is not that poor"
sens ="not"
sense = "poor"

if input_string.find(sens) < input_string.find(sense):
    ind = input_string.find(sens)
    input_string= input_string.replace(input_string[ind:],'good')

print(input_string)