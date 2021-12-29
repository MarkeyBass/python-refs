

class MyRange:

    def __init__(self, start, end):
        # TODO:  check if start < end && that they are numbers (int, float)
        self.start = start
        self.end = end

    # the moment we implement __len__ and __getitem__ our obj becomes iterable
    # now we can convert it to list and tuple
    # because we can use iterator --> it = iter(r); next(it); next(it)...
    def __len__(self):
        return self.end - self.start + 1

    def __getitem__(self, item):

        result = self.start + item

        if result > self.end:
            raise IndexError("the index is out of range")

        return result


if __name__ == '__main__':
    r = MyRange(10, 20)
    print(r[0])
    print(r[10])
    # print(r[100])
    print(r[5])
    print(len(r))
    print(tuple(r))
    print(list(r))

    li = list(r)
    print(li[8:])

    for num in r:
        print(num)


