from abc import ABC


class Shape(ABC):
    pass


class Rectangle(Shape):
    def __init__(self, width, height=None):
        if height is None:
            height = width
        if (
                not isinstance(width, (int, float))
                or not isinstance(height, (int, float))
        ):
            raise TypeError('Values must be integers or floats')
        else:
            self.width = width
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side)
        self.side = side

    def __repr__(self):
        return "Square(side={})".format(self.side)


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Value must be an Integer or a float')
        else:
            self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2

    def get_perimeter(self):
        return 3.14 * (2 * self.radius)

    def __repr__(self):
        return "Circle(radius={})".format(self.radius)


if __name__ == '__main__':
    r1 = Rectangle(4, 5)
    r2 = Rectangle(4)
    s1 = Square(8)
    c1 = Circle(6)

    print(r1)
    print(f"perimeter={r1.get_perimeter()}, aria={r1.get_area()}")
    print(r2)
    print(f"perimeter={r2.get_perimeter()}, aria={r2.get_area()}")
    print(s1)
    print(f"perimeter={s1.get_perimeter()}, aria={s1.get_area()}")
    print(c1)
    print(f"perimeter={c1.get_perimeter()}, aria={c1.get_area()}")

