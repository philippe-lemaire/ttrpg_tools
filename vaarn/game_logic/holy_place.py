from random import choice
from dataclasses import dataclass

holy_place_data = (
    (
        "Decrepit Keep",
        "Ancient Book",
        "Church of the Promised Sun",
        "Nobody",
    ),
    (
        "Sand-swallowed",
        "Holy Bee Hive",
        "Pale Faith of Amun-Oh",
        "Family of Tiny Cacogen",
    ),
    (
        "Petrified Trees",
        "Caged Bird",
        "The Thrice-Born Sage",
        "Sentient Plant",
    ),
    (
        "Ring of Stones",
        "Enormous Gemstone",
        "Seekers of Eyeless Wisdom",
        "Eunuch Priests",
    ),
    (
        "Rough Altar",
        "Beautiful Statue",
        "Church of Sevenscore Moons",
        "Chaste Priestesses",
    ),
    (
        "Underground Church",
        "Ancient Computer",
        "Temple of the Binary Devotion",
        "Automated Priests",
    ),
    (
        "Glass Pagoda",
        "Broken Statue",
        "Vaa, the Blue Goddess of Empty Places",
        "Lithling Monk",
    ),
    (
        "Ziggurat",
        "Crystal Skull",
        "Azathoth, the Daemon Sultan",
        "Blind Old Woman",
    ),
    (
        "Broken Temple",
        "Wooden Idol",
        "Cult of KRONOS",
        "Masked Mutes",
    ),
    (
        "Dried-up Oasis",
        "Polychrome Throne",
        "Cult of METIS",
        "Sentient Wasp Hive",
    ),
    (
        "Looming Statue",
        "Crystal Diadem",
        "Cult of MNEMOSYM",
        "Learned Monks",
    ),
    (
        "Ruined Village",
        "Ancient Shoe",
        "Cult of HYPERION",
        "Warrior Monks",
    ),
    (
        "Fungal Church",
        "Urn of Ashes",
        "Cult of GAEA",
        "Guardian Synth",
    ),
    (
        "Chrome Tower",
        "Mummified Jackal",
        "Cult of COEUS",
        "Pack of New-Jackals",
    ),
    (
        "Windy Hilltop",
        "Molten Statue",
        "Cult of THEMIS",
        "Paranoid Exiles",
    ),
    (
        "Hidden Cave",
        "Mummified Child",
        "Faa Nomad Ancestors",
        "Faa Nomads",
    ),
    (
        "Missile Silo",
        "Ancient Telescope",
        "A Solar Saint",
        "Cacogen Oracle",
    ),
    (
        "Wreck",
        "Levitating Orb",
        "A Fungal Saint",
        "Mycomorph Oracle",
    ),
    (
        "Settlement",
        "Synthetic Head",
        "A Void Saint",
        "Beggar Monks",
    ),
    (
        "Ruin",
        "Human Tooth",
        "Nameless, Forgotten God",
        "Monster Lair",
    ),
)


@dataclass
class HolyPlace:
    location: str
    focus_of_worship: str
    holy_to: str
    curated_by: str

    def __repr__(self):
        return f"""{self.location.capitalize()} with a  {self.focus_of_worship.lower()} as focus.
        <br>
        Holy to {self.holy_to.lower()} and curated by {self.curated_by.lower()}.
        """


def gen_holy_place():
    data = [choice(holy_place_data)[k] for k in range(4)]
    return HolyPlace(*data)
