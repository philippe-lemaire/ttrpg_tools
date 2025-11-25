from random import choice, randint
from dataclasses import dataclass


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
        return f"{self.body.capitalize()} body, {self.size} size. {self.head.capitalize()} head carving. {self.hue.capitalize()} hue."


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
    char.details = get_character_detail_lithling()
    char.looks = gen_looks_lithling()
