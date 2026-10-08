# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()
Maximum=max(numbers)
Minimum=min(numbers)
sorted_list=sorted(numbers)
list_length=int(len(sorted_list))

if list_length % 2 == 1:
    odd_median_index = int(list_length/2)
    print(sorted_list[odd_median_index])
  
else: 
   list_length %2 == 0
   middle_number_1 = int((list_length/2))
   middle_number_2 = int(((list_length/2)-1))
   even_median_value = ((sorted_list[middle_number_1] + sorted_list[middle_number_2])/2)
   print(even_median_value)
   

 