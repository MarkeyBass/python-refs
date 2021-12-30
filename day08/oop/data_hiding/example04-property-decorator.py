# Google search python builtin -> property()
# https://docs.python.org/3/library/functions.html#property

# https://www.programiz.com/python-programming/property


class Person:
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person(name={}, age={})'.format(
            repr(self.name), self.age
        )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if Person.MIN_AGE <= value <= Person.MAX_AGE:
            self.__age = value
        else:
            raise ValueError("age must be between {} to {}".format(
                Person.MIN_AGE, Person.MAX_AGE
            ))


if __name__ == '__main__':
    p1 = Person("Moshe", 20)
    p2 = Person("David", 30)
    # p3 = Person("Shlomo", 400)

    # p1.age = 400
    # p1._age = 400 # can be done but it is the user's choice to risk it.

    p1.age = 55
    print(p1)

    p1.age += 3
    print(p1)

    # will throw an exception
    p1.age += 100
    print(p1)

    # Also here we can be bad boys and bend the rules
    # print(p1._Person__age)
    # p1._Person__age += 100
    # print(p1._Person__age)




