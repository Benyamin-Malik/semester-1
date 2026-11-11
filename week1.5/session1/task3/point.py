# Week 1.5, Session 1: Task 3

 
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

    def distance(self):
        """
        Return the distance from this point to the origin (0, 0).
        """
        return math.sqrt((self.x*self.x) +(self.y*self.y))

    def distance_to(self, other):
        """
        Return the distance from this point to another Point.
        """
        x_difference = other.x - self.x
        y_difference = other.y - self.y

        return math.sqrt((x_difference*x_difference) +(y_difference*(y_difference)))

p1=Point(3,4)
print(p1.distance())
p2=Point(5,10)
print(p1.distance_to(p2))
