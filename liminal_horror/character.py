from .roll import roll
from .archetypes import ARCHETYPES
from random import choice


class Character:
    def __init__(self, background=None):
        self.STR = roll("3d6")
        self.DEX = roll("3d6")
        self.CTRL = roll("3d6")
        self.HP = roll("d6")
        self.archetype = choice(ARCHETYPES)
        self.common_gear = ["Smartphone", f"${roll('1d6')*100}.00"]
        self.gear = self.common_gear + self.archetype.take
        self.age = roll("2d10") + 20
