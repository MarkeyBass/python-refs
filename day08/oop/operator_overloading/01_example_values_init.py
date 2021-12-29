class T:
    def __init__(self, numbers=[]):
        # The empty project will create problems
        self.numbers = numbers


if __name__ == '__main__':
    t1 = T()
    t1.numbers.append(111)

    print(t1.numbers)

    t2 = T([10,20,30])
    print(t2.numbers)

    t3 = T()
    print(t3.numbers)

