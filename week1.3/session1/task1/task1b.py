# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# fruit.pop removes the last element from the list.printing this displays it.with the last item removed the second to last item becomes the last.this goes on until the list is empty.
# What features of Python does it rely on?
#this relies on list methods and the while loop. the looop allows it to contionouslt remove items.