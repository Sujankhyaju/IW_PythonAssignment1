# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def Count(samp_string):
    count_C ,count_L = 0,0
    for i in samp_string:
        if i.isupper() == True:
            count_C += 1
        else:
            count_L += 1

    return count_C,count_L

samp_string = "The Quick Brown Fox Jumps onto The Lazy Lamb"

print("The number of upper and lower case letters are ::",Count(samp_string),"respectively")