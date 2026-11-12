# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their su

from money import Money

m1=Money(1,20)
m2=Money(1,30)


m3=m1.__add__(m2)
print(m3)