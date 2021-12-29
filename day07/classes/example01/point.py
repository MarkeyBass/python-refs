
class Point:
    pass


if __name__ == '__main__':

    p1 = Point()

    p1.a = 100
    p1.b = 200

    print(p1.a)
    print(p1.b)

    del p1.a

    print(p1.a)
