class Point:
    """
    documentation for Point
    """
    count = 0

    def __init__(self, x=0, y=0):
        """
        documentation for Point.__init__
        """

        if type(x) not in (int, float):
            raise ValueError("x must be int or float")

        if type(y) not in (int, float):
            raise ValueError("y must be int or float")

        self.x = x
        self.y = y

        Point.count += 1

    def __del__(self):
        Point.count -= 1

    def show(self):
        print("({}, {})".format(self.x, self.y))


if __name__ == '__main__':
    p1 = Point(10, 20)
    p1.show()
    print("there are", Point.count, "points")

    p2 = Point(44, 55)
    p2.show()
    print("there are", Point.count, "points")

    p3 = p2
    print("there are", Point.count, "points")

    del p1
    print("there are", Point.count, "points")

    del p2
    print("there are", Point.count, "points")

    del p3
    print("there are", Point.count, "points")

    points = [
        Point(1, 1),
        Point(2, 2),
        Point(30, 40)
    ]

    print(len(points))