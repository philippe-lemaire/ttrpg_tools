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


core_encounter_tables = {
    "Grassland": {
        1: "A roc passes overhead and then divebombs the PCs",
        3: "A hunting smilodon prowls through the tall grass",
        5: " A baby mammoth flees a pack of 2d6 wolves",
        7: " A pale wizard in black robes stands silently on a tall rock",
        9: " 1d4 giant dung beetles roll manure toward a towering pile",
        11: "A whirling dust devil is actually an angry air elemental",
        13: "Dark, tall clouds roll in; a violent thunderstorm is imminent",
        15: "1d4 fierce griffons savagely tear apart a horse carcass",
        17: "3d6 kobolds pop out of prairie dog holes and fling rocks",
        19: "Smoke drifts on the wind; a growing wildfire rages nearby",
        21: "An earth elemental slurps around in a muddy geyser field",
        23: "1d4 wyverns sun themselves atop striated badlands hills",
        25: "2d6 rust-red velociraptors prowl the plains for slow prey",
        27: "Two hill giants trudge along with a horse under each arm",
        29: "A pack of 3d6 gnolls trails a rhino peppered with arrows",
        31: "An empty tower shell is covered in finger-painted runes",
        33: "The grass bends in an S shape; it's a roving giant snake",
        35: "A stampede of 2d6 mammoths thunders toward the PCs",
        37: "A lone orc sits inside a weathered henge of stones",
        39: "Rune-etched boulders seal off ancient burial cairns",
        41: "3d6 horse-riding berserkers crest over the horizon",
        43: "A wyvern swoops at a human backed up to a cliff edge",
        45: " Wedges on strings hold precarious boulders in place",
        47: " Two gnolls fight inside a ring of 2d4 chanting gnolls",
        49: " 1d4 wild boars drink at a thin, winding stream",
        53: "2d6 bandits on horses drive a herd of bison toward a cliff",
        55: "Cursed wind flutes on poles hypnotize with their sound",
        57: "A bandit chieftain (x2 LV and damage) demands a duel",
        59: "2d4 lions watch intently from the banks of a river",
        61: "2d20 nervous peasants stare from their circle of yurts",
        63: "A druid in a wolf cloak paints red symbols on dead bison",
        65: "2d4 pegasi wheel overhead, teaching 2 clumsy foals to fly",
        67: "A grass-woven effigy of a horse stands in an empty field",
        69: " An ochre basilisk basks on a rock and puffs its neck pouch",
        71: "An albino chimera sails out of a white, fluffy cloud",
        73: "1d4 ankhegs hiss and spit at a rampaging bulette",
        75: "A rival crawling party rides in a howdah on an elephant",
        77: "A fossilized tree teeters on top of an eroding mud pillar",
        79: "A T-Rex gallops along after a herd of panicked antelope",
        81: "2d6 gnolls creep below the tall grass line, spears ready",
        83: "A mammoth gently pats heads with its trunk: +1 luck token",
        85: " A mated pair of smilodons leaps down from grassy ridges",
        87: " A stone golem made of glittering gypsum guards a field",
        89: " A shadow ripples over the grass like a dark stain",
        91: "2d12 berserker hunters welcome guests to their camp",
        93: "A bull-headed shrine to a lost god repels roving beasts",
        95: "A sun-blind cave brute wildly lurches toward sounds",
        97: "The Wandering Merchant flees from a furious rhino",
        99: "Roll two encounters and combine the results (reroll this result if it comes up again)",
        100: "A principi angel strides from a storm cloud to gift a boon",
    }
}
