# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)
"""
    this function checks each letter in a string for whether it is upper case or lowercase.it returns 2 numbers,
    the first reprersent the number of upper case letters and the 2nd represent the number of lowercase numbers.

    args string:string to check

    returns tuple with 2 values representing the number of lower and uppercase characters respectivly,
 """

# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func("X"))
# print(mystery_func("[2, 3]"))
