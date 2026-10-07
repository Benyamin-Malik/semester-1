# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()
Maximum=max(numbers)
Minimum=min(numbers)
sorted_list=sorted(numbers)
list_length=int(len(numbers))

if list_length % 2 == 1:
    odd_median_index = int((((list_length +1)/2))-1)
    print(numbers[odd_median_index])
  
else: 
   list_length %2 == 0
   even_median_float = float(((((list_length/2)) +((list_length/2)+1))/2))
   #tommorow do emf-1 + emf=1 pull the values from the list add and then deviade to get median look at if print bit to get info on how to pull with index from list 
   #may need to make 2 variables +1 minus 1 tinker tommorow 
 