"""
Inheritance type :  single inheritance
Description:
Animal (num_of_legs, height, width, move(), rest())
Dog (species, bark(), jump())
A dog is a type of animal.

# Modifications
"""


class Animal:
    def __init__(self, num_of_legs, height, width):
        self.num_of_legs = num_of_legs
        self.height = height
        self.width = width

    def move(self):
        print("the animal is moving")

    def rest(self):
        print("the animal is resting")


class Dog(Animal):
    def __init__(self, num_of_legs, height, width, species):
        super().__init__(num_of_legs, height, width)
        self.species = species

    def bark(self):
        print("the dog barked")

    def jump(self):
        print("the dog jumped")


# main program
animal = Animal(4, "0,5 meters", "0,8 meters")
print(animal.num_of_legs, animal.height, animal.width)
animal.move()
animal.rest()

dog = Dog(4, "0,5 meters", "0,7 meters", "Labrador Retriever")
print(dog.num_of_legs, dog.height, dog.width, dog.species)
dog.bark()
dog.jump()
