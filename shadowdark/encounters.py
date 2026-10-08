from random import choice, sample
from .dice_tools import get_closest_key, roll
from dataclasses import dataclass

distances = {1: "Close", 4: "Near", 6: "Far"}
activities = {
    4: "Hunting",
    6: "Eating",
    8: "Building/nesting",
    10: "Socializing/playing",
    11: "Guarding",
    12: "Sleeping",
}
reactions = {
    6: "Hostile",
    8: "Suspicious",
    9: "Neutral",
    11: "Curious",
    12: "Friendly",
}


@dataclass
class Encounter:
    distance: str
    activity: str
    reaction: str
    treasure: bool


def gen_encounter(charisma_mod=0):
    distance = get_closest_key(roll("1d6"), distances)
    activity = get_closest_key(roll("2d6"), activities)
    reaction = get_closest_key(roll("2d6") + charisma_mod, reactions)
    treasure = choice((True, False))
    return Encounter(distance, activity, reaction, treasure)


if __name__ == "__main__":
    print(gen_encounter())
