"""
This version writes the Square properties in a shorter way. see lines 50-63
Also, the code for finding the max shape have changed into one-liners. see lines 92-100
"""

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

    # Under the hood a property is a class variable ("static") and all our properties
    # do the same thing (redirect to __length). So we can set the others as class variables
    # that alias the same property object instead of writing property code for each of them.
    #
    w = h = length

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

    shapes[2].h = 3

    # printing all the shapes and their area
    for shape in shapes:
        print('{} has an area of: {:.2f}'.format(shape, shape.area()))

    print()

    # finding the largest perimeter:  <comprehension generator>
    max_perimeter = max(shape.perimeter() for shape in shapes)
    print("largest perimeter found is: {:.2f}".format(max_perimeter))

    # Finding the object with the largest perimeter:
    #
    # The expression `lambda x: x.perimeter()` creates a nameless function that takes an argument `x` and
    # calls the method `perimeter()` for it. max then uses that function to sort and find the maximum
    #
    max_shape = max(shapes, key=lambda x: x.perimeter())
    print("the shape with the largest perimeter ({:.2f}) is: {}".format(max_shape.perimeter(), max_shape))






