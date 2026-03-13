from point import Point

class ColourPoint(Point):
    """
    Colour point class inheriting from Point class
    """
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """
        Overwrite this method to return a string representation of the point
        :return: string representation of the point
        """
        return f"{self.colour}: P<{self.x},{self.y}>"


p1 = ColourPoint(1,2,"red")
p2 = ColourPoint(3,4,"green")
p3 = ColourPoint(5,6,"blue")
p4 = ColourPoint(7,8,"yellow")
colour:points = [p1, p2, p3, p4]
print(colour_points)