import numpy as np
import re

file= open('input_day2.txt', 'r').readlines()
file_array = np.array(file)

file_list = []
for sub in file_array:
    file_list.append(sub.replace("\n", ""))

## Part 1
    
sum=0  
for i in range(len(file_list)):
    file_list_split = re.split(r'[:;,]', file_list[i])[1:]
    game = re.split(r'[:;,]', file_list[i])[0]
    compare_to_no_elements = 0
    for j in range(len(file_list_split)):
        iter_b = re.finditer(r'\bblue\b|\bred\b|\bgreen\b', file_list_split[j])
        iter_d = re.finditer(r'\d+', file_list_split[j])
    
        next_b = next(iter_b, None)
        next_d = next(iter_d, None) 
        
        if ((next_b.group() == 'blue') and (float(next_d.group()) <= 14)) or ((next_b.group() == 'red') and (float(next_d.group()) <= 12)) or ((next_b.group() == 'green') and (float(next_d.group()) <= 13)):
            compare_to_no_elements += 1
    
    if compare_to_no_elements == len(file_list_split):
        sum +=  float(re.findall(r'\d+', game)[0]) 

print('Sum =', sum)

## Part 2 

sum=0  
for i in range(len(file_list)):
    file_list_split = re.split(r'[:;,]', file_list[i])[1:]
    no_blue = []
    no_red = []
    no_green = []
   
    for j in range(len(file_list_split)):
        iter_b = re.finditer(r'\bblue\b|\bred\b|\bgreen\b', file_list_split[j])
        iter_d = re.finditer(r'\d+', file_list_split[j])
    
        next_b = next(iter_b, None)
        next_d = next(iter_d, None) 
        
        if next_b.group() == 'blue':
            no_blue.append(float(next_d.group()))
            
        if next_b.group() == 'red':
            no_red.append(float(next_d.group()))

        if next_b.group() == 'green':
            no_green.append(float(next_d.group()))
            
    sum += np.max(np.array(no_blue)) * np.max(np.array(no_red)) * np.max(np.array(no_green))

print('Sum 2 =', sum)
