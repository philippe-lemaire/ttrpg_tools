from random import choice, sample
from .dice_tools import get_closest_key, roll
from dataclasses import dataclass

distances = {1: "Close", 4: "Near", 6: "Far"}
activities = {
    4: "🏹 Hunting",
    6: "🍗 Eating",
    8: "🪹 Building/nesting",
    10: "🫂 Socializing/playing",
    11: "💂‍♂️ Guarding",
    12: "😴 Sleeping",
}
reactions = {
    6: "😡 Hostile",
    8: "🤨Suspicious",
    9: "😐 Neutral",
    11: "🤔 Curious",
    12: "🤗 Friendly",
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

regions = ("Kyzian Steppes",)
zones = ("Grass", "Path", "Water")

grass_zone = {
    1: "Beast",
    5: "Beast",
    6: "Elemental",
    8: "People",
}

path_zone = {
    1: "Beast",
    3: "Beast",
    4: "Elemental",
    8: "People",
}

water_zone = {
    1: "Aquatic",
    5: "Aquatic",
    6: "Beast",
    7: "Elemental",
    8: "People",
}

kyzian_steppes_zone_encounter_types = {
    z: t for z, t in zip(zones, (grass_zone, path_zone, water_zone))
}

steppe_encounters = {
    "Aquatic": (
        "Hippo",
        "Hydra (LV 8)",
        "Gt. anaconda",
        "Dire condor*",
        "Plesiosaurus",
        "Piranha swarm",
        "Crocodile",
        "Clay golem",
    ),
    "Beast": (
        "Elephant",
        "1d6 smilodons",
        "2d4 horses",
        "2d4 wolves",
        "Desert dragon",
        "1d4 scrag*",
        "1d6 lions",
        "Thunderbird*",
    ),
    "Elemental": (
        "Air (LV 6)",
        "Air (LV 9)",
        "Earth (LV 6)",
        "Earth (LV 9)",
        "Fire (LV 6)",
        "Fire (LV 9)",
        "Water (LV 6)",
        "Water (LV 9)",
    ),
    "People": (
        "2d4 Kyzians",
        "2d6 gnolls",
        "Hero",
        "3d6 orcs",
        "1d4 adepts*",
        "2d4 peasants",
        "1d4 Siruul*",
        "Caravan: 2d20 peasants (L) with 3d4 guards",
    ),
}

zones_per_region = {"Kyzian Steppes": kyzian_steppes_zone_encounter_types}
encounters_per_zone = {"Kyzian Steppes": steppe_encounters}
