import numpy as np

## Part 1 

file= open('input_day1.txt', 'r').readlines()
file_array = np.array(file)

file_list = []
for sub in file_array:
    file_list.append(sub.replace("\n", ""))

sum = []
for i in range(len(file_list)):
    digits = []
    split = [*file_list[i]]
    for j in range(len(split)):
        if split[j].isalpha():
            continue
        else:
            digits.append(split[j])
    sum.append(digits[0] + digits[-1])
    sum[i] = float(sum[i])
    
total_sum = np.sum(sum)

print('Total =', total_sum)

## Part 2 

dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = str(np.arange(0,10,1))

sum=[]
for i in range(len(file_list)):
    idx_list = []
    numbers_list = []
    for w in values:
        start_index = 0
        for k in range(len(file_list[i])):
            idx = file_list[i].find(w, start_index)
            if idx!= -1:
                start_index += idx + 1 
                idx_list.append(idx)
                numbers_list.append(w)
    
    for z in numbers:
        start_index2 = 0
        for k in range(len(file_list[i])):
            idx2 = file_list[i].find(z, start_index2)
            if idx2 != -1:
                start_index2 += idx2 + 1
                idx_list.append(idx2)
                numbers_list.append(z)
            
    replaced_list = [dict.get(item, item) for item in numbers_list]   
    sort = np.argsort(np.array(idx_list))
    replaced_list_sort =  np.array(replaced_list)[sort]
    
    sum.append(replaced_list_sort[0] + replaced_list_sort[-1])
 
    sum[i] = float(sum[i])
    
total_sum = np.sum(sum)

print('Total 2=', total_sum)
    
   
    

