from .tor_dice_roller import gandalf, eye, SuccessDie
from random import choice, sample

blessings = {
    "AWE": "(ring, cloak, circlet, collar, belt, weapon sheath, staff, war-­horn)",
    "ENHEARTEN": "(ring, cloak, weapon sheath, staff, war-­horn)",
    "PERSUADE": "(ring, cloak, circlet, collar)",
    "ATHLETICS": "(rope, boots, shoes)",
    "TRAVEL": "(staff, belt, boots)",
    "STEALTH": "(ring, cloak, shoes)",
    "AWARENESS": "(ring, circlet, collar)",
    "INSIGHT": "(ring, circlet, collar)",
    "SCAN": "(ring, circlet, staff)",
    "HUNTING": "(belt, hunting horn, staff)",
    "HEALING": "(unusual, as potions and salves quickly lose their virtue)",
    "EXPLORE": "(boots, staff, coil of rope)",
    "COURTESY": "(ring, circlet, pair of studs)",
    "SONG": "(ring, musical instrument)",
    "RIDDLE": "(ring)",
    "CRAFT": "(ring, crafting tool)",
    "BATTLE": "(crown, ring, staff, war-horn - rare, as it usually pertains to weapons)",
    "LORE": "(mirror, book, seeing-­stone)",
}


class Blessing:
    def __init__(self, skill):
        self.skill = skill
        self.type = blessings.get(self.skill)


class MagicalTreasure:
    def __init__(self, die):
        self.nature = ""
        self.description = ""
        self.shadow = ""
        self.featdie = die

        if die.value in (gandalf, eye):
            sd = SuccessDie().value
            self.successdie = sd
            if sd <= 3:
                self.nature = "Marvellous Artefact"
                self.description = "An enchanted object graced by a Blessing"
                if die.value == eye:
                    self.shadow = "Gain 1 Shadow (Greed)"
                self.blessings = (Blessing(choice(list(blessings.keys()))),)
            elif sd <= 5:
                self.nature = "Wondrous Item"
                self.description = "An enchanted object possessing two Blessings"
                if die.value == eye:
                    self.shadow = "Gain 2 Shadow (Greed)"
                rolled_kills = sample(list(blessings.keys()), 2)
                self.blessings = (Blessing(s) for s in rolled_kills)
            else:
                self.nature = "Famous Weapon or Armour"
                self.description = "A Weapon or suit of armour of superior make"
                if die.value == eye:
                    self.shadow = "Gain 3 Shadow (Greed)"
                self.blessings = ("",)

    def __repr__(self):
        return self.nature
