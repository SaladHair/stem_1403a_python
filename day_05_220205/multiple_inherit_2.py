"""
multiple inheritance
ver: 2

which behavior?
"""


class ParentA:
    def sleep(self):
        print("short sleep behavior")


class ParentB:
    def sleep(self):
        print("long sleep behavior")


class Child(ParentA, ParentB):
    pass


class Child2(ParentB, ParentA):
    pass


# test in main
peter = Child()
peter.sleep()

jack = Child2()
jack.sleep()
