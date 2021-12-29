class A:
    pass


class B:
    def f(self):
        print('f() from B')


class C:
    def f(self):
        print('f() from C')


class Child1(A, B):
    pass


class Grand(Child1, C):
    pass
# Grand will inherit B.f()
# It inherits due to M.R.O (Method Resolution Order)
# In other words: __mro__ holds the order of inheritance.


if __name__ == '__main__':
    print(Grand.__mro__)
    for x in Grand.__mro__:
        print(x)