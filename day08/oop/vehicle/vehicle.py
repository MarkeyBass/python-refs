from wheel import Wheel
import copy


class Vehicle:

    REQUIRED_WHEEL_COUNT = 4
    MINIMUM_WHEEL_AIR = 61

    def __init__(self):
        self.wheels = []

    def check_if_driveable(self):
        if len(self.wheels) != Vehicle.REQUIRED_WHEEL_COUNT:
            return False

        r = self.wheels[0].radius
        for wheel in self.wheels[1:]:
            if wheel.radius != r:
                return False

        for wheel in self.wheels:
            if wheel.is_punctured or wheel.air < Vehicle.MINIMUM_WHEEL_AIR:
                return False

        return True

    def add_wheel(self, w):
        self.wheels.append(copy.deepcopy(w))

    def del_wheel(self, index):
        self.wheels.pop(index)

    def drive(self, distance):
        distance_left = distance
        while self.check_if_driveable() and distance_left > 0:
            distance_left -= 1
            for wheel in self.wheels:
                wheel.air -= 1

        if distance_left == distance:
            print("could not drive")
        elif distance_left > 0:
            print("could only drive {} of the distance".format(
                distance - distance_left
            ))
        else:
            print("drove all of the distance successfully")




