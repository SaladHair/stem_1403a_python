"""
multiple inheritance
ver: 2

application
RPG (Character, Doll)
Level

Rank I
Occupation (Warrior I, Magician I)

Rank II
Warrior I => MagicianWarrior II
melee(), holyshield()

Magician I => WarriorMagician II
fireball(), melee(sword)

"""


class Warrior:
    def melee(self):
        print("melee")


class Magician:
    def magic(self):
        print("magic")


class MagicianWarrior(Warrior, Magician):
    def holyshield(self):
        print("holyshield")


class WarriorMagician(Magician, Warrior):
    def fireball(self):
        print("fireball")


