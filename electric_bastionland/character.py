from .failed_careers import failed_carreers
from into_the_odd.game_logic import roll
from random import choice


class Character:
    def __init__(self):
        for attr in ["STR", "DEX", "CHA"]:
            setattr(self, attr, roll("3d6"))
        for attr in ["pounds", "HP"]:
            setattr(self, attr, roll("1d6"))
        self.failed_career = choice(list(failed_carreers.values()))
        self.name = choice(self.failed_career.get("sample_names")).capitalize()
        self.answer_pound = (
            self.failed_career.get("pound").get("answers").get(self.pounds)
        )
        self.answer_hp = self.failed_career.get("hp").get("answers").get(self.HP)

    def __repr__(self):
        return f"{self.name}, a former {self.failed_career['name']}"
