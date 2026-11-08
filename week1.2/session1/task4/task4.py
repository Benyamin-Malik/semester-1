# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#tomato.This is as its in both sets

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#it does this as it prints all the items in both sets expect the element,toamto,which is in both sets.

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("watermelon")

# Remove an item from vegetables
vegetables.remove("tomato")
# tomato is a fruit.

# Find and display symmetric difference of the two sets
symetric_diffirence=fruit.union(vegetables)-fruit.intersection(vegetables)
print(symetric_diffirence)
