"""
by mro rules
child calls own init()
child calls ParentA init()
"""


class ParentA:
    # not accessed
    # the property name is not visible
    def __init__(self, age, *args, **kwargs):
        print("ParentA __init__() called")
        self.age = str(age) + " at parentA"
        # using super to call ParentB init()
        super().__init__(*args, **kwargs)


class ParentB:
    # not accessed
    def __init__(self, name, *args, **kwargs):
        print("ParentB __init__() called")
        self.name = name + " at parentA"


class Child(ParentA, ParentB):
    def __init__(self, gender, name, age):
        print("Child __init__() called")
        self.gender = gender
        super().__init__(age, name)


# main
print(Child.__mro__)

child1 = Child("gender:Male", "name:Peter", 16)
print(child1.gender)
print(child1.name)
print(child1.age)
