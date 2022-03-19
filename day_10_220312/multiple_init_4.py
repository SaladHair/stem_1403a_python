"""
by mro rules
child calls own init()
child calls ParentA init()
"""


class ParentA:
    # not accessed
    # the property name is not visible
    def __init__(self, age):
        print("ParentA __init__() called")
        self.age = age + " at parentA"


class ParentB:
    # not accessed
    def __init__(self, name):
        print("ParentB __init__() called")
        self.name = name + " at parentA"


class Child(ParentA, ParentB):
    def __init__(self, gender, name):
        print("Child __init__() called")
        self.gender = gender
        super().__init__(name)


# main
child1 = Child("gender:Male", "name:Peter")
print(child1.gender)

"""
print(child1.name)
# 'Child' object has no attribute 'name'
"""

print(child1.age)
