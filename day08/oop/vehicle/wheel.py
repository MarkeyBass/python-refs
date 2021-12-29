import random


class Wheel:
    MAX_AIR = 100

    def __init__(self, radius, is_punctured=False, air=None):
        self.is_punctured = is_punctured
        self.radius = radius

        if air is None:
            self.air = random.randint(85, 95)
        else:
            self.air = air

    # returned a string representation for the user (programmer)
    # can usually be used to construct a copy
    # can be called explicitly using the repr() function
    def __repr__(self):
        return "Wheel(radius={}, is_punctured={}, air={})".format(
            self.radius,
            self.is_punctured,
            self.air,
        )

    # returns a string representation for the end-user (the one using the program)
    # if not defined, __repr__ is used instead.
    #
    '''
    def __str__(self):
        return "Wheel: radius={}, air={}{}".format(
            self.radius,
            self.air,
            " Punctured" if self.is_punctured else "",
        )
    '''

    def inflate(self, air_to_add):
        # type(air_to_add) is int
        # air_to_add = int(air_to_add)
        if type(air_to_add) is not int:
            raise ValueError("air_to_add must be an int")

        if air_to_add < 0:
            raise ValueError("air_to_add must be 0 or higher")

        self.air += air_to_add

        if self.air > Wheel.MAX_AIR:
            self.air = Wheel.MAX_AIR


if __name__ == '__main__':
    w = Wheel(10)
    print(w)

    w2 = Wheel(20, True, 55)
    print(w2)

    w2.inflate(30)
    print(w2)


