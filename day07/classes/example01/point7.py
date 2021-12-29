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

    def show(self):
        print("({}, {})".format(self.x, self.y))


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(5)
    p3 = Point(10, 20)

    p1.show()
    p2.show()
    p3.show()