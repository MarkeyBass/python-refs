class Person:
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, name, age):
        self.name = name
        self.age = age

        if not self.is_valid_age():
            raise ValueError("age must be between {} to {}".format(
                Person.MIN_AGE, Person.MAX_AGE
            ))

    def is_valid_age(self):
        return Person.MIN_AGE <= self.age <= Person.MAX_AGE


if __name__ == '__main__':
    p1 = Person("Moshe", 20)
    p2 = Person("David", 30)
    # p3 = Person("Shlomo", 400)

    print(p1.age, p2.age)

    p1.age = 400  # the age attribute is not parameter in python
    #             # check next examples to see ways to semi protect it

    print(p1.age, p2.age)
