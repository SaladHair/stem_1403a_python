"""
[Homework]
Date: 2022-02-12
Due date: 2022-02-19
1. programming practice
Rewrite the following cases without referring to the demo
case 3. accessing methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def function(self):
        print("parent function was called")


class Child(Parent):
    def function_2(self):
        super().function()
        print("child function was called")


parent = Parent("peter")
parent.function()
child = Child("peter")
child.function_2()
