"""
[Homework]
Date: 2022-02-12
Due date: 2022-02-19
1. programming practice
Rewrite the following cases without referring to the demo
case 4. forcely accessing private properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.__name = name

    def __function(self):
        print("parent function was called")


class Child(Parent):
    def function_2(self):
        super()._Parent__function()


child = Child("peter")
print(child._Parent__name)
child.function_2()
