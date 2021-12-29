# warning: super() might not work as expected with multiple inheritance
#
# for more information about using super in classes:
#
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={}, y={}".format(self.x, self.y)

    def sum_coordinates(self):
        return self.x + self.y


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return "Point3D(x={}, y={}, z={}".format(
            self.x, self.y, self.z)

    def sum_coordinates(self):
        # return self.x + self.y + self.z
        return super().sum_coordinates() + self.z


if __name__ == '__main__':
    p = Point3D(1, 2, 3)
    print(p)

    print(isinstance(p, Point3D))
    print(isinstance(p, Point))

    print(Point3D.sum_coordinates(p))
    print(p.sum_coordinates())
