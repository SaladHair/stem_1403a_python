"""
directly accessing properties and methods of parent class

Parent (name, talk())
Child

main program/app
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("the parent talked")


class Child(Parent):
    pass


# main program
child = Child("Nolan")
print(child.name)
child.talk()