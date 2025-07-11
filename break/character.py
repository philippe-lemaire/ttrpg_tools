from .callings import CALLINGS


class Character:
    def init_stats(self):
        self.might = self.calling.might
        self.deft = self.calling.deft
        self.grit = self.calling.grit
        self.insight = self.calling.insight
        self.aura = self.calling.aura
        self.attack_bonus = self.calling.attack_bonus
        self.hearts = self.calling.hearts
        self.defense = self.calling.defense
        self.abilities = self.calling.starting_abilities

    def __init__(self, calling_name):
        self.calling = CALLINGS.get(calling_name)
        self.init_stats()
