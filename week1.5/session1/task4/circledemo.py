# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Create a Point with the given x and y coordinates.
        """
        self.x = x
        self.y = y

class Circle :

    def __init__(self,x,y,radius):
    
   
     self.radius=radius
     self.centre=Point(x,y)

    def circ_area(self):

       return (3.14159 *(self.radius*self.radius))

    def circ_perimeter(self):
       return(3.141592*(2*self.radius))


