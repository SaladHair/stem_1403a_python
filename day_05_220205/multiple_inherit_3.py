"""
multiple inheritance
ver: 2

which behavior?
"""


class ParentA:
    def sing(self):
        print("sing()")


class ParentB:
    def painting(self):
        print("painting()")


class Child(ParentA, ParentB):
    pass


# test in main
peter = Child()
peter.sing()
peter.painting()
