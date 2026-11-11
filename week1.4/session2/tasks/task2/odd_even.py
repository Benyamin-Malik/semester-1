# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """

    even_numbs=0
    odd_numbs=0
        
    for i in lstIntegers:
       if i%2==0:
        even_numbs+=1
       else:
           i%2==1
           odd_numbs+=1

    return [odd_numbs,even_numbs]

    

# Check if correct output is produced
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]
