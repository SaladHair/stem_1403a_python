"""
class member 2
"""


class Foo:
    attr1 = 123

    def method1(self):
        pass

    def __init__(self):
        self.attr2 = 234

    def method2(self):
        pass


# using class Foo
obj1 = Foo()
print(obj1.attr2)
obj1.method2()