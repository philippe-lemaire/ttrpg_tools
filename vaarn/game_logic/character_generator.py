from .ancestries import ANCESTRIES
from .abilities import ABILITIES
from .dice import roll_stat

from random import randint, choice


class Character:
    def __init__(self):
        self.ancestry = choice(ANCESTRIES)
        for ability in ABILITIES:
            setattr(self, ability, roll_stat())
        self.hp = randint(1, 8) + self.CON

    def __repr__(self):
        return (
            f"{self.ancestry} character with {self.CON} CON and {self.hp} Hit Points."
        )
