"""
M12. OOP
single inheritance
"""


# class Animal(object):
#     pass


class Animal:
    def __init__(self):
        self.name = "animal"
    # pass

    def run(self):
        print("animal runs by foot.")


class Bird:
    pass


class Dog(Animal):

    def bark(self):
        print("dog barks.")

    # pass


class Parot(Bird):
    pass


# main
dog1 = Dog()
print(dog1.name)
dog1.run()
dog1.bark()

#
a1 = Animal()
# a1.bark()
