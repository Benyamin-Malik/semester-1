# A bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self,x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x_coordinate= x_coordinate
        self.y_coordinate= y_coordinate

    x_coordinate = [9.8,7,6,5,4,3,2,1,0]
    y_coordinate = [0,1,2,3,4,5,6,7,8,9]
print(Point.x_coordinate,Point.y_coordinate)