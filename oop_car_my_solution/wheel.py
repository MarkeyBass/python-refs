from random import randint


class Wheel:
    MAX_AIR = 100

    def __init__(self, air=None, is_punctured=False, radius=15):
        self.is_punctured = is_punctured
        self.radius = radius
        if (air is None) or (air > 100) or (air < 0):
            self.air = randint(85, 95)
        else:
            self.air = air

    def __str__(self):
        return 'Wheel: air_percentage={}, radius={}, {}punctured'.format(
            self.air,
            self.radius,
            "" if self.is_punctured else "Not ",
        )

    def __repr__(self):
        return 'Wheel(air={}, is_punctured={}, radius={})'.format(
            self.air,
            self.is_punctured,
            self.radius,
        )

    def inflate(self, new_air):
        try:
            new_air = int(new_air)
        except ValueError:
            print("ValueError air value must be an int. Wheel haven't been inflated")

        if type(new_air) is int:
            self.air += new_air
            if self.air > Wheel.MAX_AIR:
                self.air = Wheel.MAX_AIR


if __name__ == '__main__':
    w1 = Wheel()
    w2 = Wheel(65, True, 20)
    w3 = Wheel(11, True, 20)
    print(w1)
    print(w2)
    w3.inflate('d')
    print(w3)
