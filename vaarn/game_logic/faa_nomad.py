from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule


looks_table = (
    (
        "Azure",
        "Lively",
        "Tall",
        "None",
    ),
    (
        "Cerulean",
        "Cruel",
        "Short",
        "Cropped",
    ),
    (
        "Navy",
        "Wrinkled",
        "Frail",
        "Spiky",
    ),
    (
        "Cobalt",
        "Ritual Scars",
        "Muscular",
        "Coarse",
    ),
    (
        "Indigo",
        "Battle Scars",
        "Fat",
        "Thick",
    ),
    (
        "Sapphire",
        "Frowning",
        "Thin",
        "Balding",
    ),
    (
        "Teal",
        "Tattooed",
        "Skeletal",
        "Silky",
    ),
    (
        "Ultramarine",
        "Wide",
        "Hunched",
        "Topknot",
    ),
    (
        "Turquoise",
        "Narrow",
        "Lopsided",
        "Nearly Black",
    ),
    (
        "Cyan",
        "Sharp",
        "Lithe",
        "Stark White",
    ),
    (
        "Bruise",
        "Hungry",
        "Gnarled",
        "Cloud-like",
    ),
    (
        "Petrol",
        "Haunted",
        "Squat",
        "Tonsured",
    ),
    (
        "Midnight",
        "Jolly",
        "Bloated",
        "Fading to Purple",
    ),
    (
        "Cornflower",
        "Round",
        "Gangly",
        "Heavily Oiled",
    ),
    (
        "Lapis ",
        "Lazuli",
        "Mournful",
        "Towering",
        "Wispy",
    ),
    (
        "Periwinkle",
        "Child-like",
        "Child-like",
        "Burnt",
    ),
    (
        "Electric",
        "Peaceful",
        "Gigantic",
        "Braided",
    ),
    (
        "Aquamarine",
        "Sleepy",
        "Wiry",
        "Greasy",
    ),
    (
        "Royal",
        "Branded",
        "Stout",
        "Matted",
    ),
    (
        "Glaucous",
        "Pox-marked",
        "Injured",
        "Outrageous",
    ),
)


@dataclass
class FaaNomadLooks:
    blue: str
    body: str
    face: str
    hair: str

    def __repr__(self):
        return f"{self.body.capitalize()} body. {self.face.capitalize()} face. {self.hair.capitalize()} hair. {self.blue} blue skin."


def gen_looks_faa_nomad():
    attributes = [choice(looks_table)[i] for i in range(4)]
    return FaaNomadLooks(*attributes)


names = (
    "Kotesh",
    "Lakshi",
    "Atric",
    "Caroum",
    "Yanne",
    "Uvi",
    "Pidash",
    "Ravat",
    "Ayuki",
    "Kuraso",
    "Esuk",
    "Zenji",
    "Calban",
    "Paquiel",
    "Serrat",
    "Emila",
    "Dolf",
    "Ceilo",
    "Immacula",
    "Yudhi",
)

manners = (
    "Abrasive",
    "Arrogant",
    "Assertive",
    "Charismatic",
    "Daring",
    "Decadent",
    "Eloquent",
    "Extravagant",
    "Hedonistic",
    "Impulsive",
    "Irritable",
    "Melancholy",
    "Paranoid",
    "Quiet",
    "Religious",
    "Romantic",
    "Scholarly",
    "Stern",
    "Vain",
    "Volatile",
)

left_clan_reasons = (
    "Psychedelic Vision",
    "Stolen by Slavers as a Child",
    "Rite of Passage; Must Return with Wisdom",
    "Unhappy Love Affair ",
    "Conflict With Leaders",
    "Believed Cursed; Ostracised",
    "Lost Them In Sandstorm",
    "Estranged From Family",
    "Seeking Vengeance",
    "Shamed Clan; Must Make Amends",
)

quirks = (
    "Parasitic Twin In Chest",
    "Gambling Obsessive",
    "Insomniac",
    "Wooden Teeth",
    "Devoutly Religious",
    "Ritual Scarring",
    "Heavily Tattooed",
    "Unlucky In Love",
    "Awful Cook",
    "One Eye",
    "Glass Teeth",
    "Heavy Drinker",
    "Infamous Seducer",
    "Scorpion Expert",
    "Third Eye (Tattoo)",
    "Third Eye (Real)",
    "Cybernetic Limb",
    "Plagued by Nightmares",
    "Lovely Singing Voice",
    "Notorious Amongst Faa",
)

special_rules_data = (
    (
        "Desert Metabolism",
        "Your body is adapted to long periods without water. You can recycle the moisture from your own sweat. You become Deprived from thirst after three days without drinking, and it will be three weeks before you die.",
    ),
    (
        "Worm Rider",
        "When in the deep desert, you may summon a Sandworm (p.xx) by rhythmically dancing. It will arrive within an hour, with a 2-in-6 chance of being a juvenile (p.xx). Make a DEX save to mount and ride the worm. It will carry you for d6 days in a direction of your choice before tiring.",
    ),
)


@dataclass
class CharacterDetailsFaaNomad:
    manner: str
    quirk: str
    left: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. Left their clan because {self.left}. {self.quirk.capitalize()}."


def get_character_detail_faa_nomad():
    manner = choice(manners)
    quirk = choice(quirks)
    left = choice(left_clan_reasons)
    return CharacterDetailsFaaNomad(manner, quirk, left)


def set_character_name_and_details_faa_nomad(char):
    char.name = choice(names)
    char.details = get_character_detail_faa_nomad()
    char.looks = gen_looks_faa_nomad()
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
