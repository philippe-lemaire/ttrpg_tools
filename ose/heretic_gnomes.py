import random
from dataclasses import dataclass

from .hoard_treasure import roll

gnome_names = (
    "Ogbold",
    "Grimm",
    "Loki",
    "Dreblem",
    "Dorobold",
    "Migmir",
    "Fimir",
    "Batabsh",
    "Beb",
    "Moblim",
    "Gribbl",
    "Heribotte",
    "Lob",
    "Sob",
    "Meribolle",
    "Jandly",
    "Krob",
    "Grobe",
    "Horiddle",
    "Sagglow",
)

gnome_ages = (
    "Adult M",
    "Adult M",
    "Old M",
    "Adult M",
    "Adult M",
    "Old M",
    "Adult M",
    "Adult M",
    "Adult F",
    "Adult F",
    "Adult F",
    "Old F",
    "Adult F",
    "Adult F",
    "Old F",
    "Adult F",
    "Child M",
    "Child M",
    "Child F",
    "Child F",
)

gnome_traits = (
    "Smelly",
    "Leader",
    "Hunched",
    "Slovenly",
    "Cackles",
    "Brewer",
    "Butcher",
    "Fishbones",
    "Sneaky",
    "Obese",
    "Priestess",
    "Grinning",
    "Knives",
    "Mad",
    "Nostalgic",
    "Traitor",
    "Burpy",
    "Weepy",
    "Evil",
    "Kind",
)

under_hat = (
    "Pouch of 2d20sp",
    "Gem worth 2d100gp",
    "Ball of chunky red wool",
    "Flask of whiskey",
    "Rosy apple",
    "Map to ancestral warren",
    "Black pear, heals 1d3hp",
    "Cinnamon bun",
    "Gold nugget worth 75gp",
    "Pet mouse",
)

under_hat_random_list = [random.choice(under_hat) for _ in range(20)]


@dataclass
class Gnome:
    name: str
    age: str
    trait: str
    under_hat: str
    hp: int = 4


def get_gnomes():
    gnomes = [
        Gnome(name, age, trait, under_hat)
        for name, age, trait, under_hat in zip(
            gnome_names, gnome_ages, gnome_traits, under_hat_random_list
        )
    ]
    for gnome in gnomes:
        gnome.hp = roll("1d8")
    return gnomes
