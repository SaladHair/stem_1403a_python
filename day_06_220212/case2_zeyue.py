"""
[Homework]
Date: 2022-02-12
Due date: 2022-02-19
1. programming practice
Rewrite the following cases without referring to the demo
case 2. overriding properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def function(self):
        print("parent function was called")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.name = "child" + name

    def function(self):
        print("child function was called")


parent = Parent("peter")
print(parent.name)
parent.function()
child = Child("peter")
print(child.name)
child.function()
