"""

"""


class ParentA:
    # not accessed
    # the property name is not visible
    def __init__(self, name):
        print("ParentA __init__() called")
        self.name = name


class ParentB:
    # not accessed
    def __init__(self):
        print("ParentB __init__() called")


class Child(ParentA, ParentB):
    def __init__(self, gender):
        print("Child __init__() called")
        self.gender = gender


# main
child1 = Child("Male")
# child1 = Child("Male", "Peter")
print(child1.gender)
