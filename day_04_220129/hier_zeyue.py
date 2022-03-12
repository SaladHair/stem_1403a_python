"""
Inheritance type :  hierarchical inheritance
Description:
Animal (num_of_legs, height, width, move(), rest())
Dog (species, bark(), jump())
Cat (species, purr(), meow(), sleep())
A dog and a cat are types of animal.

# Modifications
Sleep -> Animal
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


class Cat(Animal):
    def __init__(self, num_of_legs, height, width, species):
        super().__init__(num_of_legs, height, width)
        self.species = species

    def purr(self):
        print("the dog purred")

    def meow(self):
        print("the cat meowed")

    def sleep(self):
        print("the cat slept")


# main program
animal = Animal(4, "0,5 meters", "1 meter")
print(animal.num_of_legs, animal.height, animal.width)
animal.move()
animal.rest()

dog = Dog(4, "0,5 meters", "0,7 meters", "Labrador Retriever")
print(dog.num_of_legs, dog.height, dog.width, dog.species)
dog.bark()
dog.jump()

cat = Cat(4, "0,5 meters", "1 meter", "Siamese")
print(cat.num_of_legs, cat.height, cat.width, cat.species)
cat.purr()
cat.meow()
cat.sleep()

