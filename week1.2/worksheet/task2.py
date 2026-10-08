# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys 
try:
    numbers = read_numbers()
    Minimum=min(numbers)
    Maximum=max(numbers)
    sorted_list=sorted(numbers)
    list_length=int(len(sorted_list))
    Mean=((sum(numbers)/list_length))
    print(f"Minimum = {Minimum}")
    print(f"Maximum = {Maximum}")
    print(f"Mean = {Mean}")
    if list_length % 2 == 1:
         odd_median_index = int(list_length/2)
         median = sorted_list[odd_median_index]
         print(f"Median = {median}")
    else: 
        list_length %2 == 0
        middle_number_1 = int((list_length/2))
        middle_number_2 = int(((list_length/2)-1))
        median = ((sorted_list[middle_number_1] + sorted_list[middle_number_2])/2)
        print(f"Median = {median}")
except:
    sys.exit("Error: no numbers provided")
 