"""
[Homework]
Date: 2022-02-12
Due date: 2022-02-19
1. programming practice
Rewrite the following cases without referring to the demo
case 5. defining __init__ method in child class
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def function(self):
        print("parent function was called")


class Child(Parent):
    def __init__(self):
        pass


child = Child()
print(child.name)
child.function()
