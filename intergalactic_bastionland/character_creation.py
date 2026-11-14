from .game_logic import roll, male_fornames, surnames
from .planets import PLANETS
from random import sample, choice


class Character:
    def __init__(self):
        self.name = f"{choice(male_fornames)} {choice(surnames)}"
        self.guard = roll("d6")
        self.tees = roll("d6")
        self.born, self.made, self.broken = tuple(sample(PLANETS, 3))

        self.skills = {
            self.born.born_skill: roll("d6") + roll("d12"),
            self.made.made_skill: roll("d6") + roll("d12"),
            self.broken.broken_skill: roll("d6") + roll("d12"),
        }

        self.special = self.born.special
        self.equipment = "<br>".join(
            (self.made.made_equipment, self.broken.broken_equipment)
        )
