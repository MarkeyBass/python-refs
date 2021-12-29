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

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y

        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other

        else:
            return NotImplemented

        return self

    def __add__(self, other):
        result = Point(self.x, self.y)
        result += other
        return result

    def __radd__(self, other):
        return self + other

    def distance(self, other):
        from math import sqrt
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


