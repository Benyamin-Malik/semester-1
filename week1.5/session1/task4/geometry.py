# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

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
    """
    This creates a circle with a radius and 2 co-ordinates at its centre.
    """

    def __init__(self,radius,x=0,y=0,):
    
   
     self.radius=radius
     self.centre=Point(x,y)

    def circ_area(self):
       """
       works out the area of the circle
       """

       return (math.pi *(self.radius*self.radius))

    def circ_perimeter(self):
       """
              works out the perimeter of the circle
       """
       return(math.pi*(2*self.radius))
