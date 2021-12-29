class Point:
    count = 0

    def __init__(self, x=0, y=None):
        self.x = int(x)

        if y is None:
            self.y = int(x)
        else:
            self.y = int(y)

        Point.count += 1

    def __del__(self):
        Point.count -= 1

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

    def distance(self, other):
        from math import sqrt
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(5, 6)

    print("p1:", p1)
    print("p2:", p2)
    print("p1 + p2:", p1 + p2)

    p3 = p1 + p2
    print("p3:", p3)
