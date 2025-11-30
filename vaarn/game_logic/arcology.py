from random import choice
from dataclasses import dataclass


arcology_data = (
    (
        "Broken",
        "Abandoned",
        "Meat",
        "Olives",
    ),
    (
        "Molten",
        "Abandoned",
        "Fresh Water",
        "Fish",
    ),
    (
        "Sand-swallowed",
        "Hermit",
        "Salt",
        "Beer",
    ),
    (
        "Dingy",
        "Mystic",
        "Guzzleline",
        "Men",
    ),
    (
        "Blackened",
        "Escaped Slaves",
        "Coffee",
        "Women",
    ),
    (
        "Self-Repairing",
        "Ghouls",
        "Wine",
        "Children",
    ),
    (
        "Barely Intact",
        "Hegemony Deserters",
        "Bread",
        "Music",
    ),
    (
        "Booby-trapped",
        "Newbeasts",
        "Jewellery",
        "Silence",
    ),
    (
        "Reinforced",
        "Semi-Feral Orphans",
        "Books",
        "Livestock",
    ),
    (
        "Functional",
        "Amnesiac Clones",
        "Fruit",
        "Books",
    ),
    (
        "Warlike",
        "Elderly Mutes",
        "Information",
        "Coffee",
    ),
    (
        "Delicate",
        "Conceptual Artists",
        "Bells",
        "Bread",
    ),
    (
        "Ornate",
        "Orchestra",
        "Drugs",
        "Spices",
    ),
    (
        "Welcoming",
        "Fungus Cultists",
        "Livestock",
        "Drugs",
    ),
    (
        "Garden-like",
        "Polygamous Church",
        "Skilled Labour",
        "Sanity",
    ),
    (
        "Elegant",
        "Lepers",
        "Musical Instruments",
        "Medicine",
    ),
    (
        "Devotional",
        "Warrior Monks",
        "Slaves",
        "Information",
    ),
    (
        "Flooded",
        "Psychic Choir",
        "Cheese",
        "New Blood",
    ),
    (
        "Geodesic",
        "Androids Pretending to be Human",
        "Weapons",
        "Machine Parts",
    ),
    (
        "Perfect",
        "Androids Pretending to be Human",
        "Exotica",
        "Clothing",
    ),
)


@dataclass
class Arcology:
    dome: str
    inhabitants: str
    abundance: str
    lack: str

    def __repr__(self):
        return f"{self.dome} Dome, inhabited by {self.inhabitants}.<br>An abundance of {self.abundance} but a lack of {self.lack}."


def gen_arcology():
    data = (choice(arcology_data)[k] for k in range(4))
    return Arcology(*data)
