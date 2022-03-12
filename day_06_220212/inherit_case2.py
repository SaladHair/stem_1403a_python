"""
case 2. overriding properties and methods of parent class

Parent (name, talk())
Child (name, talk())

main program/app

"""


class Parent:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("the parent talked")


class Child(Parent):
    def __init__(self, name):
        self.name = name + " at child"

    def talk(self):
        print("the child talked")


# main program
child = Child("Nolan")
print(child.name)
child.talk()