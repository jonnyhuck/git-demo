from math import hypot, degrees, atan2, sin, cos, radians

class Point:
    """ Class representing a 2D point on a plane"""

    def __init__(self, in_x, in_y):
        """ constructor """
        self.x = in_x
        self.y = in_y

    def __str__(self):
        """ set output when object is printed """
        return f"({self.x}, {self.y})"
    
    def distance_to(self, target):
        """ compute distance between this point and another along a plane """
        return hypot(self.x - target.x, self.y - target.y)

    def direction_to(self, target):
        """ compute direction between this point and another along a plane """
        return (180 + degrees(atan2(self.y - target.y, self.x - target.x)) + 360) % 360

    def offset_by(self, distance, direction):
        """ compute the location of a point at a given distance and direction from this point along a plane """
        return Point(self.x + cos(radians(direction)) * distance, self.y + sin(radians(direction)) * distance)

# comment...