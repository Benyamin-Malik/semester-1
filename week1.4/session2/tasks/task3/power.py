# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.

import math
def power(x, n):
    # complete your code here
    # base case
    if n==0:
     return 1
    recursive=(x*power(x,n-1))
    print(recursive)
    return recursive
# Once completed, make at least two function calls to test the power function
power(2,10))