# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width:int, height:int):
        """
        Creates a Rectangle, given values for width and height.
        """
        self.width=width
        self.height=height
        if not isinstance(width,int):
            raise TypeError("width must be an integer")
        if width <=0 :
            raise ValueError("width must be greaterthan or equal to zero")
        if not isinstance(height,int):
                    raise TypeError("height must be an integer")
        if height <=0 :
            raise ValueError("height must be greater than or equal to zero")

    def is_square(self):
            """
            returns true if rectangle is a square,otherwise returns false"""
            if self.width==self.height:
                  return True
            else:
                  return False
    def area(self):
             """
             returns the area of a square
             """
             return self.width*self.height

    def perimeter(self):
             """"
             returns squares perimmeter
             """
             return ((2*self.width)+(2*self.height))


#identation is very annoying.
      
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
       

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
