# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.

    
    """

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    Bond=[0,0,7]
    if Bond in intList :
        return True
    else:
        return False
   # delete pass to write your code
#python doesnt check for sublists.its going to be some sort of iteration thing where you check if at any starting point e.g 
#zerp there is a set of 3 intergers equal to set bond.you do this until the starting point of i is ewwual to the last index of 
#of intlist.Hopefully will have to time to implement something later
# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
