from random import choice, randint
from dataclasses import dataclass
from .special_rules import SpecialRule


sizes = (
    "Child-like",
    "Small",
    "Moderate",
    "Large",
    "Imposing",
)


body_head_hue = (
    (
        "Dainty",
        "Sphere",
        "Rose",
    ),
    (
        "Tiny",
        "Owl",
        "Onyx",
    ),
    (
        "Boxy",
        "Serpent",
        "Azure",
    ),
    (
        "Voluptuous",
        "Oxen",
        "Silver",
    ),
    (
        "Squat",
        "Horse",
        "Indigo",
    ),
    (
        "Lithe",
        "Warrior",
        "Gold",
    ),
    (
        "Angular",
        "Maiden",
        "Violet",
    ),
    (
        "Craggy",
        "Locust",
        "Ruby",
    ),
    (
        "Elegant",
        "Jackal",
        "Orange",
    ),
    (
        "Bulbous",
        "Moon",
        "Topaz",
    ),
    (
        "Sharp",
        "Sun",
        "Jade",
    ),
    (
        "Rotund",
        "Pyramid",
        "Brass",
    ),
    (
        "Weathered",
        "Cat",
        "Copper",
    ),
    (
        "Monumental",
        "Trout",
        "Rust",
    ),
    (
        "Derelict",
        "Scholar",
        "Moss",
    ),
    (
        "Blocky",
        "Fool",
        "Ochre",
    ),
    (
        "Flaking",
        "Crone",
        "Steel",
    ),
    (
        "Smooth",
        "Mantis",
        "Sand",
    ),
    (
        "Pitted",
        "Ape",
        "Citrine",
    ),
    (
        "Fragmented",
        "Goat",
        "Emerald",
    ),
)


@dataclass
class LithlingLooks:
    size: str
    body: str
    head: str
    hue: str

    def __repr__(self):
        return f"{self.body.capitalize()} body, {self.size.lower()} size. {self.head.capitalize()} head carving. {self.hue.capitalize()} hue."


def gen_looks_lithling():
    attributes = [choice(body_head_hue)[i] for i in range(3)]
    attributes.insert(0, choice(sizes))
    return LithlingLooks(*attributes)


names_manners_study_quirk = (
    (
        "Aikin",
        "Logical",
        "Shellfish",
        "Engraved with Poem",
    ),
    (
        "Antimony",
        "Obsessive",
        "Ants",
        "Engraved with Curse",
    ),
    (
        "Bentor",
        "Naive",
        "Spirals",
        "Engraved with Map",
    ),
    (
        "Brokenhill",
        "Abrasive",
        "Cacti",
        "Engraved with Equation",
    ),
    (
        "Cabalzar",
        "Forgetful",
        "Birdsong",
        "Plants Grow From Head",
    ),
    (
        "Cairngorm",
        "Aloof",
        "Lizard Eggs",
        "Deep Crack in Face",
    ),
    (
        "Chalcedony",
        "Mellow",
        "Fingernails",
        "Covered in Moss",
    ),
    (
        "Diaspor",
        "Sentimental",
        "Shoes",
        "Covered in Dead Vines",
    ),
    (
        "Ephesi",
        "Amoral",
        "Wasps",
        "Hollow Chest",
    ),
    (
        "Heliotrope",
        "Impulsive",
        "Land Snails",
        "Hollow Head",
    ),
    (
        "Idrial",
        "Negative",
        "Tarantulas",
        "Eyes Glow in Dark",
    ),
    (
        "Indium",
        "Rigid",
        "Jackals",
        "Hand Missing",
    ),
    (
        "Jaros",
        "Patient",
        "Pottery",
        "Face Eroded Away",
    ),
    (
        "Khatyr",
        "Decisive",
        "Dance",
        "Leaking Dust",
    ),
    (
        "Meerschaum",
        "Gracious",
        "Lunar Cycles",
        "You Are Translucent",
    ),
    (
        "Okenit",
        "Assertive",
        "The Sun",
        "Chest Filled With Fluid",
    ),
    (
        "Qusong",
        "Unhurried",
        "Tides",
        "Hole Blasted in Flesh",
    ),
    (
        "Schori",
        "Vengeful",
        "Wind",
        "Second Face on Torso",
    ),
    (
        "Ulrich",
        "Graceless",
        "Rain",
        "Mirrored Flesh",
    ),
    (
        "Ziest",
        "Stern",
        "Silence",
        "Face Rotates",
    ),
)

special_rules_data = (
    (
        "Crystalline Flesh",
        "You are made from living crystal. Your base AV is 10 + your Level (maximum 20). You do not need to eat or drink. You do not take damage from fire, cold, poison, radiation, electricity, fungal spores, or suffocation. You suffer double damage from bludgeoning attacks.",
    ),
    (
        "Inevitable",
        "During character generation, roll 10d8. This number is your starting and maximum HP. (NB: already rolled above) You cannot heal lost HP through any means, and do not add to your maximum HP when you gain a level. When your HP tally reaches zero you crumble into iridescent dust, leaving behind a pebble-sized lithling seed.",
    ),
)


@dataclass
class CharacterDetailsLithling:
    manner: str
    field_of_study: str
    quirk: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. Studies {self.field_of_study.lower()}. Quirk: {self.quirk}."


def get_character_detail_lithling():
    manner = choice(names_manners_study_quirk)[1]
    field_of_study = choice(names_manners_study_quirk)[2]
    quirk = choice(names_manners_study_quirk)[3]
    return CharacterDetailsLithling(manner, field_of_study, quirk)


def set_character_name_and_details_lithling(char):
    char.name = choice(names_manners_study_quirk)[0]
    char.hp += sum(randint(1, 8) for _ in range(9))  # special hp rule
    char.details = get_character_detail_lithling()
    char.looks = gen_looks_lithling()
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
