from .ancestries import ANCESTRIES
from .abilities import ABILITIES
from .dice import roll_stat
from .weapons import weapon_generator, rarities
from .boons import BOONS
from random import randint, choice


class Character:
    def __init__(self):
        self.ancestry = choice(ANCESTRIES)
        for ability in ABILITIES:
            setattr(self, ability, roll_stat())
        self.healing_rate = randint(1, 8) + self.CON
        self.hp = randint(1, 8)
        self.item_slots = 10 + self.CON
        self.inventory = ["3 rations of water", "3 rations of food"]
        self.boon = choice(BOONS)
        # add 1 roll on basic weapon and armor tables
        r = 1 if self.boon == "Advanced Weapon" else 0
        self.inventory.append(weapon_generator(rarities[r]))
        # TODO add 2 rolls on the explorer gear table
        # TODO add additional rolls for the other boons
        # TODO add all the traits for each 10 ancestries gasp

    def __repr__(self):
        return f"{self.ancestry} character with {self.CON} CON and {self.hp} Hit Points, equipped with {self.inventory}"
