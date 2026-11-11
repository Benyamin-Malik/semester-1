# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle


from geometry import Point
from geometry import Circle




p1=Point(1,2)
c1=Circle(10,p1)
c1_area= c1.circ_area()
c1_perimeter=c1.circ_perimeter()
print(c1_perimeter)
print(c1_area)


