# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self,distance,distance_to):
    # Add distance() method here
     self.distance= distance
     
    # Add distance_to() method here
     self.distance_to=distance_to
    # (This will need a parameter representing another point)
     distance=[100,200,300]
     distance_to=[300,200,100]


# Finally, add code here to demonstrate use of Point
print(Point(distance,distance_to))