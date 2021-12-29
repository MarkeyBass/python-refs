from math import sqrt
from point import Point


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)

    def show(self):
        print("({}, {}) --> ({}, {})".format(self.a.x, self.a.y, self.b.x, self.b.y))

    def length(self):
        return self.a.distance(self.b)


if __name__ == '__main__':
    line1 = Line(10, 20, 30, 40)
    line1.show()
    print(line1.length())
