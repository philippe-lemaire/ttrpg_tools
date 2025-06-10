from .tor_dice_roller import gandalf, eye, SuccessDie


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
            elif sd <= 5:
                self.nature = "Wondrous Item"
                self.description = "An enchanted object possessing two Blessings"
                if die.value == eye:
                    self.shadow = "Gain 2 Shadow (Greed)"
            else:
                self.nature = "Famous Weapon or Armour"
                self.description = "A Weapon or suit of armour of superior make"
                if die.value == eye:
                    self.shadow = "Gain 3 Shadow (Greed)"

    def __repr__(self):
        return self.nature
