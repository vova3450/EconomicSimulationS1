from ftplib import parse150, parse227


class Point:
    """
    Simple class to represent a point in 2D space.
    """
    def __init__(self, x, y):
        """
        Constructor for Point class.
        :param x: x coordinate of point
        :param y: y coordinate of point
        """
        self.x = x # x is a class attribute
        self.y = y
    def __str__(self):
        """
        String representation of Point class.
        :return: string representation of Point class
        """
        return f"P<{self.x}, {self.y})>"

    def __repr__(self):
        return self.__str__()


    def distance_origin(self):
        """
        Calculate the distance between point and origin
        :return: float, distance between point and origin
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, point):
        """
        Calculate the distance bewteen current point and another point
        :param point: the other point to calculate the distance to
        :return: float, distance between current point and another point
        """

        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    def __lt__(self,other):
        """
        Returns True is self is less than the other point.
        :param other: the other point to compare against
        :return: True or False
        """
        return self.distance_origin() < other.distance_origin()

if __name__ == "__main__": # protect the code from import runs!!
    p1 = Point(1,2)
    p2 = Point(3,4)

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print(p2)
    print(p1,p2)
    print(f"{p2} distance to origin is {p2.distance_origin()}")
    p3 = Point(12,5)
    print(f"{p3} distance to origin is {p3.distance_origin()}")
    p1 = Point(6, 10)
    p2 = Point(6, 16)
    print(f"distance between {p1} and {p2} is: {p1.distance_to(p1)}")
    p4 = Point(1, 1)
    points = [p1, p2, p3, p4]
    print(points)
    points.sort()
    print(points)
    print(points)