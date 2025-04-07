from .roll import roll
from random import choice
from .archetypes import ARCHETYPES


class Character:
    def __init__(self, module):
        self.STR = roll("3d6")
        self.DEX = roll("3d6")
        self.CTRL = roll("3d6")
        self.HP = roll("d6")
        self.archetype = choice(ARCHETYPES[module])
        self.common_gear = ["Smartphone", f"${roll('1d6')*100}.00"]
        self.gear = self.common_gear + self.archetype.take
        self.age = roll("2d10") + 20
