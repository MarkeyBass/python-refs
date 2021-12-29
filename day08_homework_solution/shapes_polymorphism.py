import abc   # Used for defining Shape as an abstract class
import math  # For pi


# Due to duck-typing we don't really need a Shape class.
# But creating one can help identify a shared type e.g by using isinstance(x, Shape)
#
# Also, making the class abstract (inherit from ABC) will prevent creating an instance from this class
#
# Likewise, adding area and perimeter as abstract methods will force the inheritors to implement the methods,
# otherwise, they cannot be used to create instances.
#
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def __repr__(self):
        return "Rectangle(w={}, h={})".format(self.w, self.h)


class Square(Rectangle):
    def __init__(self, length):
        # Calling the parent's init is redundant but it calms the the code analyzer
        Rectangle.__init__(self, length, length)
        # super().__init__(length, length)
        self.length = length

    # We use properties so that any access to w,h or length gets redirected to __length:
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def w(self):
        return self.__length

    @w.setter
    def w(self, value):
        self.__length = value

    @property
    def h(self):
        return self.__length

    @h.setter
    def h(self, value):
        self.__length = value

    def __repr__(self):
        return "Square(length={})".format(self.length)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return "Circle(radius={})".format(self.radius)


if __name__ == '__main__':
    shapes = [Circle(2), Rectangle(2, 3), Square(4)]

    shapes[2].h = 3  # a test to show that changing h affects length

    # printing all the shapes and their area
    for shape in shapes:
        print('{} has an area of: {:.2f}'.format(shape, shape.area()))

    print()

    # finding the largest perimeter (see version 2 for a shorter code):
    max_perimeter = shapes[0].perimeter()

    for shape in shapes[1:]:
        p = shape.perimeter()
        if p > max_perimeter:
            max_perimeter = p

    print("largest perimeter found is: {:.2f}".format(max_perimeter))

    # finding the object with the largest perimeter (see version 2 for a shorter code):
    max_shape = shapes[0]

    for shape in shapes[1:]:
        if shape.perimeter() > max_shape.perimeter():
            max_shape = shape

    print("the shape with the largest perimeter ({:.2f}) is: {}".format(max_shape.perimeter(), max_shape))





