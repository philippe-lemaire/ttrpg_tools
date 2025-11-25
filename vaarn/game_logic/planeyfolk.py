from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule


looks_table = (
    (
        "Fractured",
        "Impressionistic",
        "Flickering",
        "Dark",
    ),
    (
        "Cloven",
        "Broken",
        "Insubstantial",
        "Unruly",
    ),
    (
        "Flimsy",
        "Lantern-like",
        "Curved",
        "Scholarly",
    ),
    (
        "Willowy",
        "Crescent Moon",
        "Voluminous",
        "Masked",
    ),
    (
        "CurvedFull ",
        "Moon",
        "Opalescent",
        "Wild",
    ),
    (
        "Elongated",
        "Luminous",
        "Shaven",
        "Polychromic",
    ),
    (
        "Staccato",
        "Angular",
        "Iridescent",
        "Fractal",
    ),
    (
        "Blurred",
        "Fractal",
        "Lurid",
        "Glitching",
    ),
    (
        "Ghostlike",
        "Hollow",
        "Fractal",
        "Gauzy",
    ),
    (
        "Draping",
        "Shimmering",
        "Polygonal",
        "Fragmented",
    ),
    (
        "Compressed",
        "Lurid",
        "Shard-like",
        "Mosaic-like",
    ),
    (
        "Cubic",
        "Lustrous",
        "Triangular",
        "Boxy",
    ),
    (
        "Smeared",
        "Rhomboid",
        "Splintering",
        "Flamboyant",
    ),
    (
        "Sharp",
        "Figment",
        "Dark",
        "Dour",
    ),
    (
        "Angular",
        "Wide",
        "Imposing",
        "Striped",
    ),
    (
        "Prismatic",
        "Elongated",
        "Pale",
        "Spotted",
    ),
    (
        "Hollow",
        "Helix",
        "Cubic",
        "Glass-like",
    ),
    (
        "Delicate",
        "Triangular",
        "Polychromic",
        "Concealing",
    ),
    (
        "Isometric",
        "Quadrilateral",
        "Drifting",
        "Barbaric",
    ),
    (
        "Imposing",
        "Fragmentary",
        "Fragmentary",
        "Outrageous",
    ),
)


@dataclass
class PlaneyFolkLooks:
    body: str
    head: str
    hair: str
    attire: str

    def __repr__(self):
        return f"{self.body.capitalize()} body. {self.head.capitalize()} head. {self.hair.capitalize()} hair. {self.attire}."


def gen_looks_planeyfolk():
    attributes = [choice(looks_table)[i] for i in range(4)]
    return PlaneyFolkLooks(*attributes)


names_manners_geometry = (
    (
        "Clotho",
        "Anxious",
        "Cast Two Shadows",
    ),
    (
        "Atropos",
        "Arrogant",
        "Never Cast Shadows",
    ),
    (
        "Osteria",
        "Assertive",
        "Move Like Stop-Motion Animation",
    ),
    (
        "Vanise",
        "Charismatic",
        "Your Face Appears Concave",
    ),
    (
        "Whervil",
        "Conceited",
        "Your Face Appears Convex",
    ),
    (
        "Laomer",
        "Decadent",
        "You Always Appear In Profile",
    ),
    (
        "Foxglory",
        "Eloquent",
        "You Always Face Away From Observers",
    ),
    (
        "Thelik",
        "Extravagant",
        "One Limb Is Enormously Long",
    ),
    (
        "Umbrie",
        "Hedonistic",
        "Viewed From Behind You Have No Skin",
    ),
    (
        "Salter",
        "Impulsive",
        "Interiors Are Visible, But Cannot be Touched",
    ),
    (
        "Atlassia",
        "Irritable",
        "Hands Fractal; Tiny Hands on Ends of Fingers",
    ),
    (
        "Eukelaris",
        "Meticulous ",
        "You Bleed Gory Cubes",
    ),
    (
        "Galas",
        "Persistent",
        "Your Body is Clearly Hollow",
    ),
    (
        "Tarvi",
        "Quiet",
        "Eyes Are Holes of Infinite Depth",
    ),
    (
        "Untermance",
        "Religious",
        "Voice Sounds As If You Are Far Away",
    ),
    (
        "Rassias",
        "Pugnacious ",
        "You Have No Back, Just Two Identical Fronts",
    ),
    (
        "Menomeo",
        "Scholarly ",
        "Head Looks Ten Times Larger Than Body",
    ),
    (
        "Ithari",
        "Stern",
        "Never Seem to Touch Anything",
    ),
    (
        "Canetonus",
        "Unruly",
        "Multiple Identical Faces",
    ),
    (
        "Trout",
        "Volatile",
        "You Never Match the Ambient Light",
    ),
)


flat_origins = (
    "Parents were Planeyfolk",
    "Parents were Planeyfolk",
    "Parents were Planeyfolk",
    "Parents were Planeyfolk",
    "Parents were Planeyfolk",
    "Exposed to hypergeometry in utero",
    "Exposed to hypergeometry in utero",
    "Cursed by Quantum Daemon",
    "Cursed by Quantum Daemon",
    "Malfunctioning hypergeometric gateway",
    "Malfunctioning hypergeometric gateway",
    "Accidentally ate hypergeometric food",
    "Accidentally ate hypergeometric food",
    "Planeyperson inducted you into their dimension",
    "Planeyperson inducted you into their dimension",
    "Meditated before a 4D tesseract",
    "Meditated before a 4D tesseract",
    "You were a hypergeometrician, there was an accident",
    "You were a hypergeometrician, there was an accident",
    "You were a hypergeometrician, there was an accident",
)

special_rules_data = (
    (
        "Flat",
        "You lack a third dimension, and resemble a living painting or paper doll. You can slip through cracks and under doors, and cannot be seen from the side. You take halved damage from bludgeoning attacks, and doubled damage from slashing or piercing attacks. ",
    ),
    (
        "Attune with Matter",
        "You struggle to hold 3D objects, and must make a DEX save to do so. However, with certain mental techniques you can draw 3D objects into your flattened reality. Given an hour of quiet concentration, you can attune yourself with an item and add it to your inventory.",
    ),
)


@dataclass
class CharacterDetailsPlaneyFolk:
    manner: str
    strange_geometry: str
    how_you_became_flat: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. {self.strange_geometry}. Became flat because {self.how_you_became_flat}."


def get_character_detail_planeyfolk():
    manner = choice(names_manners_geometry)[1]
    strange_geometry = choice(names_manners_geometry)[2]
    how_you_became_flat = choice(flat_origins)
    return CharacterDetailsPlaneyFolk(manner, strange_geometry, how_you_became_flat)


def set_character_name_and_details_planeyfolk(char):
    char.name = choice(names_manners_geometry)[0]
    char.details = get_character_detail_planeyfolk()
    char.looks = gen_looks_planeyfolk()
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
