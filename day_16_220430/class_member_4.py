"""
class member 4
changing class attributes
"""


class Foo:
    # class attribute
    # shared among instances
    attr1 = 123

    def init(self):
        # instance attribute
        self.attr2 = 234

    def method2(self):
        pass


# read
Foo.attr1 = 999
print(Foo.attr1)

obj1 = Foo()

# read 2 - not recommended
print(obj1.attr1)
print()

# read 3
print(obj1.__class__.attr1)
