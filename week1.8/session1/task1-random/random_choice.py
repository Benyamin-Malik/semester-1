import random

# Read names from a file

with open("week1.8/session1/task1-random/names.txt") as infile:
    names = [ line.strip() for line in infile ]

numb=int(input("please enter an integer"))
random_list=random.sample(names,numb, counts=None)
for i in random_list:
    print(i)
# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
