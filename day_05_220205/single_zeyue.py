"""
Inheritance type :  single inheritance
Description:
Weapon (length, weight, one_handed, attack())
Bow (curve_strength, string_length, arrow_type, fire_arrow())
A bow is a type of weapon.

"""


class Weapon:
    def __init__(self, length, weight, one_handed):
        self.length = length
        self.weight = weight
        self.one_handed = one_handed

    def attack(self):
        print("the weapon is attacking")


class Bow(Weapon):
    def __init__(self, length, weight, one_handed, curve_strength, string_length, arrow_type):
        super().__init__(length, weight, one_handed)
        self.curve_strength = curve_strength
        self.string_length = string_length
        self.arrow_type = arrow_type

    def fire_arrow(self):
        print("the bow fired an arrow")


# main program
weapon = Weapon("0,5 meters", "15kg", "yes")
print(weapon.length, weapon.weight, weapon.one_handed)
weapon.attack()

bow = Bow("0,5 meters", "10 kg", "no", "45 degrees", "0,45 meters", "plain arrow")
print(bow.length, bow.weight, bow.one_handed, bow.curve_strength, bow.string_length, bow.arrow_type)
bow.attack()
bow.fire_arrow()
