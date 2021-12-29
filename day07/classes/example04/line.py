from math import sqrt
from point import Point


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)

    def __str__(self):
        return "{} --> {}".format(self.a, self.b)

    def length(self):
        return self.a.distance(self.b)


if __name__ == '__main__':
    line1 = Line(10, 20, 30, 40)
    print("line1:", line1)
    print(line1.length())
