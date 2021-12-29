class Person:
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, name, age):
        self.name = name
        self._age = age

        if not self.is_valid_age():
            raise ValueError("age must be between {} to {}".format(
                Person.MIN_AGE, Person.MAX_AGE
            ))

    def is_valid_age(self):
        return Person.MIN_AGE <= self._age <= Person.MAX_AGE

    def get_age(self):
        return self._age

    def set_age(self, new_value):
        if Person.MIN_AGE <= new_value <= Person.MAX_AGE:
            self._age = new_value
        else:
            raise ValueError("age must be between {} to {}".format(
                Person.MIN_AGE, Person.MAX_AGE
            ))


if __name__ == '__main__':
    p1 = Person("Moshe", 20)
    p2 = Person("David", 30)
    # p3 = Person("Shlomo", 400)

    # p1.age = 400
    p1._age = 400 # can be done but it is the user's choice to risk it.

    p1.set_age(55)
    # p1.set_age(400)   # wont work due to setter restriction

    print(p1.get_age())
    print(p1._age)  # will make PyCharm warning

