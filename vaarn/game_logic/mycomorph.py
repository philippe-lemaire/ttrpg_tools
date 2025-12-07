from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule

body_head_colour_texture_table = (
    (
        "Tall",
        "Classic Mushroom",
        "Milky",
        "Rubbery",
    ),
    (
        "Short ",
        "Frilled",
        "Cream",
        "Warty",
    ),
    (
        "Frail",
        "Spotted Sphere",
        "Ashen",
        "Slimy",
    ),
    (
        "Muscular",
        "Spires",
        "Blue",
        "Fuzzy",
    ),
    (
        "Fat",
        "Conical",
        "Coral",
        "Hairy",
    ),
    (
        "Thin",
        "Cup-like",
        "Crimson",
        "Velvet",
    ),
    (
        "Skeletal",
        "Skull-like",
        "Yellow",
        "Soft",
    ),
    (
        "Hunched",
        "Tendrils",
        "Orange",
        "Tree Bark",
    ),
    (
        "Lopsided",
        "Puffball",
        "Black",
        "Leather",
    ),
    (
        "Lithe",
        "Dandelion Fuzz",
        "Violet",
        "Jelly",
    ),
    (
        "Gnarled",
        "Mask-like",
        "Olive",
        "Burnt",
    ),
    (
        "Squat",
        "Eye Garden",
        "Lime",
        "Sponge",
    ),
    (
        "Bloated",
        "Riddled with Holes",
        "Rust",
        "Veined",
    ),
    (
        "Gangly",
        "Cauliflower",
        "Iron",
        "Downy",
    ),
    (
        "Child-like",
        "Bulbous Growths",
        "Gold",
        "Dry",
    ),
    (
        "Tanned",
        "Veil-like",
        "Bronze",
        "Damp",
    ),
    (
        "Gigantic",
        "Coral-like",
        "Indigo",
        "Pitted",
    ),
    (
        "Wiry",
        "Filaments",
        "Translucent",
        "Crusty",
    ),
    (
        "Stout",
        "Brain-like",
        "Iridescent",
        "Scaled",
    ),
    (
        "Visibly Dead",
        "Geometric",
        "Brindled",
        "Clay",
    ),
)

name_manner_corpse_table = (
    (
        "Dovenglass",
        "Abrasive",
        "Soldier",
    ),
    (
        "Oulbrier",
        "Arrogant",
        "Gladiator",
    ),
    (
        "Mockbridge",
        "Assertive",
        "Orphan",
    ),
    (
        "Headhill",
        "Charismatic",
        "Invalid",
    ),
    (
        "Tirrin",
        "Daring",
        "Convict",
    ),
    (
        "Yearns",
        "Decadent",
        "Explorer",
    ),
    (
        "Cerilgreay",
        "Eloquent",
        "Bandit",
    ),
    (
        "Rendmoor",
        "Extravagant",
        "Scholar",
    ),
    (
        "Eamont",
        "Hedonistic",
        "Mystic",
    ),
    (
        "Purplebeck",
        "Impulsive",
        "Priest",
    ),
    (
        "Arraby",
        "Irritable",
        "Nomad",
    ),
    (
        "Kabergill",
        "Melancholy",
        "Exile",
    ),
    (
        "Pearthika",
        "Paranoid",
        "King",
    ),
    (
        "Devandarsh",
        "Quiet",
        "Beggar",
    ),
    (
        "Coronam",
        "Religious",
        "Courtesan",
    ),
    (
        "Ashwine",
        "Romantic",
        "Musician",
    ),
    (
        "Ekramavati",
        "Scholarly",
        "Thief",
    ),
    (
        "Whitmon",
        "Stern",
        "Slave",
    ),
    (
        "Froswhirl",
        "Vain",
        "Plague Victim",
    ),
    (
        "Kirth",
        "Volatile",
        "Newborn",
    ),
)

spores_data = (
    (
        "Soporific Spores",
        "Targets EGO Save or fall asleep for d6 rounds",
    ),
    (
        "Berserk Spores",
        "Targets EGO save or become aggressive for d6 rounds, attacking their comrades.",
    ),
    ("Toxic Spores", "Targets CON save vs a D8 TOX attack."),
    ("Fellowship Spores", "Targets EGO save or become friendly for d6 rounds"),
    (
        "Leeching Spores",
        "Targets CON save vs d6 damage. You heal HP equal to damage dealt.",
    ),
)


@dataclass
class Spores:
    name: str
    effect: str

    def __repr__(self):
        return f"<b>{self.name}</b>: {self.effect}"


@dataclass
class MycomorphLooks:
    body: str
    head: str
    colour: str
    texture: str

    def __repr__(self):
        return f"{self.body} body, {self.head.lower()} head, {self.colour.lower()} colour, {self.texture.lower()} texture."


def get_mycomorph_looks():
    data = [choice(body_head_colour_texture_table)[k] for k in range(4)]
    return MycomorphLooks(*data)


@dataclass
class MycomorphDetails:
    manner: str
    corpse: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner, born from a {self.corpse.lower()} corpse."


def get_mycomorph_details():
    data = [choice(name_manner_corpse_table)[k] for k in range(1, 3)]
    return MycomorphDetails(*data)


special_rules_data = (
    (
        "Twice Born",
        "You are formed from fungus and the corpse of a human. You may make INT saves to recall information that your original body knew. This might include information that has otherwise been lost during the Great Collapse.",
    ),
    (
        "Detritivore",
        "You can consume organic matter in any state of decay and gain nourishment from it. You heal double HP from Short Rests if the meal you eat is rotting. You have ADV on all Saves vs poison and toxins.",
    ),
    (
        "Spores",
        "Make a CON when you release spores, which affect a number of Biological targets equal to your Level. If you fail your Save, you cannot release anymore spores that day. See spark table for details of your spores.",
    ),
)


def set_mycomorph_name_and_details(char):
    names = [row[0] for row in name_manner_corpse_table]
    char.name = choice(names)
    char.details = get_mycomorph_details()
    char.looks = get_mycomorph_looks()
    char.spore = Spores(*choice(spores_data))
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
