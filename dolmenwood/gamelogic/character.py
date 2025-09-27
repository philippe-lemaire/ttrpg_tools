from .dice import roll
from .abilities import abilities

MOD = {
    3: -3,
    4: -2,
    5: -2,
    6: -1,
    13: 1,
    14: 1,
    15: 1,
    16: 2,
    17: 2,
    18: 3,
}


class Character:
    def __init__(self):
        for ability in abilities:
            setattr(self, ability, roll("3d6"))

        for ability in abilities:
            setattr(self, f"{ability}_mod", MOD.get(getattr(self, ability), 0))

    def __repr__(self):
        scores = {ability: getattr(self, ability) for ability in abilities}
        return f"Character {scores}"


class Breggle(Character):
    kindred = "Breggle"
