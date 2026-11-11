# Another bad class implementation

# What does the runtime error mean?
#the x co-ordinte doesnt point to its value in memory
#to fix it we simply refer to self,x_.Plus i need to chage the variables
#this is as ater in the code we have refernce to p.lx or the x=cordinate of p
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self,x,y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x= x
        self.y = y
p = Point(1.5, 2.0)
print(p.x)
print(p.y)
