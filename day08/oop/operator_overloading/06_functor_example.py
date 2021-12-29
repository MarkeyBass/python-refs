class NumberSum:
    def __init__(self, *args):
        self.numbers = list(args)

    def __call__(self, *args):
        print(sum(self.numbers) + sum(args))


if __name__ == '__main__':
    ns = NumberSum(10, 20, 30)

    ns()  # 60

    ns(1, 700, 8000)  # 60 + 8701

    NumberSum(1, 2, 3)(7000)  # self execution due to implementation of __call__ method
    NumberSum(1, 2, 3)()
