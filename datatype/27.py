# 27. Write a Python program to replace the last element in a list with another list


Sample_data = [1, 3, 5, 7, 9, 10]
data= [2, 4, 6, 8]
sample = []

for i in range(len(Sample_data)):

    if i == (len(Sample_data)-1):

        for j in range(len(data)):

            sample.append(data[j])
            
        break
    
    sample.append(Sample_data[i])
    
print(sample)