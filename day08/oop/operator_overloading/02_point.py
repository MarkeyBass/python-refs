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

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(x=self.x+other.x, y=self.y + other.y)

        elif isinstance(other, (int, float)):
            return Point(x=self.x + other, y=self.y + other)

        else:
            return NotImplemented

    #  inner_add --> this will make: p1 = p2; p1 += 5; p1 is p2 --> True
    def __radd__(self, other):
        return self + other

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

    def distance(self, other):
        from math import sqrt
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


