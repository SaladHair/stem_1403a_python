"""
[Homework]
Date: 2022-02-12
Due date: 2022-02-19
1. programming practice
Rewrite the following cases without referring to the demo
case 1. directly accessing properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def function(self):
        print("parent function was called")


class Child(Parent):
    pass


child = Child("Child")
print(child.name)
child.function()
