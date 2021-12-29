
class Point:

    # special methods
    # "constructor"
    def __init__(self):
        self.x = 0
        self.y = 0


if __name__ == '__main__':

    p1 = Point()

    print(p1.x)
    p1.x = 5
    print(p1.x)

