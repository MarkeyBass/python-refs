from wheel import Wheel
from copy import deepcopy


class Vehicle:
    def __init__(self, wheels=None):
        self.wheels = wheels
        if wheels is None:
            self.wheels = []
        else:
            if not isinstance(wheels, list):
                raise ValueError("wheels mast be list of wheel objects")

            for w in wheels:
                if not isinstance(w, Wheel):
                    raise ValueError("wheels mast be a list of wheel objects")
            self.wheels = deepcopy(wheels)

        self.drivable = self.check_if_drivable()

    def check_if_drivable(self):
        if len(self.wheels) != 4:
            return False
        radius = self.wheels[0].radius
        for w in self.wheels:
            if w.radius != radius or w.air < 60 or w.is_punctured is True:
                return False
        return True

    def drive(self, km):
        if not self.drivable:
            print('car could not drive AT FIRST PLACE due to technical issues')
            return
        # get min_air_wheel && get wheels_air_list
        min_air_wheel = 100
        wheels_air_list = []
        for w in self.wheels:
            if w.air < min_air_wheel:
                min_air_wheel = w.air
            wheels_air_list.append(w.air)
        # update air
        if min_air_wheel - km > 60:
            for index, a in enumerate(wheels_air_list):
                a -= km
                self.wheels[index].air = a
        else:
            for index, a in enumerate(wheels_air_list):
                if a == min_air_wheel:
                    a = 60
                else:
                    a -= km
                self.wheels[index].air = a

        if not self.check_if_drivable():
            print(f'Car Stop after {min_air_wheel - 60} km! Not enough air in wheels')

    def drive_shmuel(self, km):
        distance_left = km
        while (self.check_if_drivable()) and (distance_left > 0):
            distance_left -= 1
            for w in self.wheels:
                w.air -= 1

        # if len(self.wheels) < 4 and (isinstance(Wheel, w)):
    def add_wheel(self, w):
        self.wheels.append(deepcopy(w))
        self.drivable = self.check_if_drivable()

    def del_wheel(self, index=-1):
        if (len(self.wheels) > 0
                and isinstance(index, int)
                and (0 >= index >= 3)):
            self.wheels.pop(index)
        self.drivable = self.check_if_drivable()


if __name__ == '__main__':
    v1 = Vehicle([Wheel(), Wheel(), Wheel(), Wheel()])
    print("v1 drivable: ", v1.check_if_drivable())
    v1.drive(15)
    print("v1 drivable: ", v1.check_if_drivable())
