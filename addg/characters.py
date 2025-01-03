import random
from .roll import roll

stat_arrays = [
    (12, 9, 6),
    (12, 6, 9),
    (9, 12, 6),
    (9, 6, 12),
    (6, 12, 9),
    (6, 9, 12),
]

occupations = {
    "STR": [],
    "DEX": [],
    "INT": [],
}


class Character:
    def __init__(self, stat_array=None):
        if stat_array:
            self.STR, self.DEX, self.INT = stat_array
        else:
            self.STR, self.DEX, self.INT = random.choice(stat_arrays)

        self.defense = roll("1d6")
        self.violence = "d4"
        self.truths = []
