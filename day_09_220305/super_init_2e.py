"""

"""


class Parent:
    def __init__(self, name):
        print("Parent __init__() called")
        self.name = name


class Child(Parent):
    def __init__(self, age, name):
        print("Child __init__() called")
        self.age = age
        super().__init__(name)


# main
# wrong order of arguments
c1 = Child("Jack", 18)
print("age : ", c1.age)
print("name : ", c1.name)
