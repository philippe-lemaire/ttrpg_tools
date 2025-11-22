from .ancestries import ANCESTRIES
from .abilities import ABILITIES
from .dice import roll_stat
from .weapons import weapon_generator, rarities
from random import randint, choice


class Character:
    def __init__(self):
        self.ancestry = choice(ANCESTRIES)
        for ability in ABILITIES:
            setattr(self, ability, roll_stat())
        self.hp = randint(1, 8) + self.CON
        self.item_slots = 10 + self.CON
        self.inventory = ["3 rations of water", "3 rations of food"]
        # add 1 roll on basic weapon and armor tables
        self.inventory.append(weapon_generator(rarities[2]))
        # add 2 rolls on the explorer gear table

    def __repr__(self):
        return f"{self.ancestry} character with {self.CON} CON and {self.hp} Hit Points, equipped with {self.inventory}"
