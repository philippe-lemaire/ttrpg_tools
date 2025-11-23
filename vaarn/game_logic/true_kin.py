from random import choice, randint
from dataclasses import dataclass


looks_table = (
    (
        "Tall",
        "Sallow",
        "Black",
        "Rags",
    ),
    (
        "Short",
        "Lively",
        "Brown",
        "Animal Skins",
    ),
    (
        "Frail",
        "Cruel",
        "Red",
        "Rough Tunic",
    ),
    (
        "Muscular",
        "Wrinkled",
        "Blonde",
        "Nomad Attire",
    ),
    (
        "Fat",
        "Scarred",
        "Grey",
        "Worker’s Attire",
    ),
    (
        "Thin",
        "Frowning",
        "White",
        "Herdsman’s Attire",
    ),
    (
        "Skeletal",
        "Pale",
        "Shaved",
        "Slave Clothing",
    ),
    (
        "Hunched",
        "Greasy",
        "Topknot",
        "Exultant’s Livery",
    ),
    (
        "Lopsided",
        "Wide",
        "Green",
        "Shabby Attire",
    ),
    (
        "Lithe",
        "Narrow",
        "Orange",
        "Colourful Attire",
    ),
    (
        "Gnarled",
        "Sharp",
        "Glowing",
        "Priest’s Robes",
    ),
    (
        "Squat",
        "Hungry",
        "Fungus",
        "Clerk’s Uniform",
    ),
    (
        "Bloated",
        "Haunted",
        "Purple",
        "Hegemony Garb",
    ),
    (
        "Gangly",
        "Jolly",
        "Yellow",
        "Soldier’s Clothing",
    ),
    (
        "Child-like",
        "Round",
        "Wispy",
        "Flamboyant Attire",
    ),
    (
        "Tanned",
        "Mournful",
        "Burnt",
        "Musician’s Attire",
    ),
    (
        "Gigantic",
        "Child-like",
        "Braided",
        "Veiled Attire",
    ),
    (
        "Wiry",
        "Peaceful",
        "Greasy",
        "Armiger's Clothing",
    ),
    (
        "Tattooed",
        "Sleepy",
        "Matted",
        "Exultant’s Clothing",
    ),
    (
        "Scarred",
        "Branded",
        "Long",
        "Expensive Clothing",
    ),
)


@dataclass
class TrueKinLooks:
    body: str
    face: str
    hair: str
    attire: str

    def __repr__(self):
        return f"{self.body.capitalize()} body. {self.face.capitalize()} face. {self.hair.capitalize()} hair. {self.attire}."


def gen_looks_true_kin():
    attributes = [looks_table[randint(0, 19)][i] for i in range(4)]
    return TrueKinLooks(*attributes)


name_manner_quirk_table = (
    (
        "Benjoe",
        "Amused",
        "Ritual Scars",
    ),
    (
        "Leif",
        "Bitter",
        "Face Tattoos",
    ),
    (
        "Xurm",
        "Morbid",
        "Slave Brand",
    ),
    (
        "Kazor",
        "Bony",
        "Heavy Jewellery",
    ),
    (
        "Essana",
        "Cheerful",
        "Synthetic Limb",
    ),
    (
        "Calista",
        "Cruel",
        "Strange Voice",
    ),
    (
        "Jinny",
        "Flamboyant",
        "Clone Brand",
    ),
    (
        "Vela",
        "Glowering",
        "Limp",
    ),
    (
        "Leksei",
        "Impish",
        "Strange Pet",
    ),
    (
        "Ippash",
        "Lanky",
        "Lacquered Teeth",
    ),
    (
        "Lagad",
        "Patrician",
        "Burn Scars",
    ),
    (
        "Myli",
        "Reckless",
        "Octarine Eyes",
    ),
    (
        "Nirid",
        "Rough",
        "Dyed Skin",
    ),
    (
        "Ardel",
        "Rude",
        "Golden Teeth",
    ),
    (
        "Senefer",
        "Sly",
        "Silver Tongue",
    ),
    (
        "Pharmon",
        "Sour",
        "Missing Limb",
    ),
    (
        "Mesu",
        "Stoic",
        "Missing Eye",
    ),
    (
        "Lenta",
        "Foolish",
        "Religious Apparel",
    ),
    (
        "Goza",
        "Warm",
        "Synthetic Eyes",
    ),
    (
        "Babl",
        "Wolfish",
        "Visibly Diseased",
    ),
)


castes = (
    "Servitor (labourer caste)",
    "Freeholder (merchant caste)",
    "Optimate (administrator caste)",
    "Armiger (warrior caste)",
    "Exultant (sacred aristocracy)",
)


@dataclass
class CharacterDetailsTrueKin:
    manner: str
    quirk: str
    caste: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. {self.quirk.capitalize()}. {self.caste.capitalize()}."


def get_character_detail_true_kin():
    manner = choice(name_manner_quirk_table)[1]
    quirk = choice(name_manner_quirk_table)[2]
    caste = choice(castes)
    return CharacterDetailsTrueKin(manner, quirk, caste)


def set_character_name_and_details_true_kin(char):
    char.name = choice(name_manner_quirk_table)[0]
    char.details = get_character_detail_true_kin()
