from point import Point
class Line:
    """ Class representing a 2D line on a plane"""
    def __init__(self, in_a, in_b):
        """ constructor """
        self.a = in_a     
        self.b = in_b
        self.length = in_a.distance_to(in_b)

    def __str__(self):
        """ set output when object is printed """
        return f"({self.a}, {self.b})"