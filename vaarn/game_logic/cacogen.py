from random import choice, randint
from dataclasses import dataclass
from .true_kin import looks_table, TrueKinLooks
from .special_rules import SpecialRule


class CacogenLooks(TrueKinLooks):
    pass


def gen_looks_cacogen():
    attributes = [looks_table[randint(0, 19)][i] for i in range(4)]
    return CacogenLooks(*attributes)


name_manner_misfortune_extrentricity_table = (
    (
        "Arda",
        "Abrasive",
        "Slave",
        "A Strange Hat",
    ),
    (
        "Bollo",
        "Arrogant",
        "Debtor",
        "Always Muttering",
    ),
    (
        "Breen",
        "Assertive",
        "Gambler",
        "Ascetic Diet",
    ),
    (
        "Conch",
        "Charismatic",
        "Clone",
        "Forgetful And Rude",
    ),
    (
        "Crab",
        "Daring",
        "Gladiator",
        "Gluttonous Diet",
    ),
    (
        "Dancer",
        "Decadent",
        "Memories Stolen",
        "Highly Formal",
    ),
    (
        "Doss",
        "Eloquent",
        "Forger",
        "Interrupts Constantly",
    ),
    (
        "Hust",
        "Extravagant",
        "Exiled",
        "Laugh At Own Jokes",
    ),
    (
        "Jal",
        "Hedonistic",
        "Cultist",
        "Married To A Knife",
    ),
    (
        "Lask",
        "Impulsive",
        "Thief",
        "Monocle",
    ),
    (
        "Lip",
        "Irritable",
        "Addicted",
        "Monotone Voice",
    ),
    (
        "Olm",
        "Melancholy",
        "Framed",
        "Only Sleeps Outdoors",
    ),
    (
        "Pirrip",
        "Paranoid",
        "Conned",
        "Only Wears Purple",
    ),
    (
        "Poucher",
        "Quiet",
        "Bankrupt",
        "Quotes Irrelevant Facts",
    ),
    (
        "Pree",
        "Religious",
        "Heretic",
        "Several Spouses",
    ),
    (
        "Uz",
        "Romantic",
        "Rejected",
        "Talks To Self",
    ),
    (
        "Whistler",
        "Scholarly",
        "Blackmailed",
        "Unwieldy Jewellery",
    ),
    (
        "Yaz",
        "Stern",
        "Cursed",
        "Usually Drunk",
    ),
    (
        "Yoss",
        "Vain",
        "Orphaned",
        "Always Wears Gloves",
    ),
    (
        "Zem",
        "Volatile",
        "Bereaved",
        "Won’t Look At Mirrors",
    ),
)


@dataclass
class CharacterDetailsCacogen:
    manner: str
    misfortune: str
    excentricity: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. {self.misfortune.capitalize()}. {self.excentricity.capitalize()}."


def get_character_details_cacogen():
    manner = choice(name_manner_misfortune_extrentricity_table)[1]
    misfortune = choice(name_manner_misfortune_extrentricity_table)[2]
    excentricity = choice(name_manner_misfortune_extrentricity_table)[3]
    return CharacterDetailsCacogen(manner, misfortune, excentricity)


special_rules_data = (
    (
        "Corrupted Blood",
        "During character creation, roll d100 three times for mutations (already rolled above). If the effects contradict one another, the more recent mutation takes precedence..",
    ),
    (
        "Proteus",
        "When you gain a Level you may roll for another mutation instead of increasing HP and ability scores. You have DIS on Saves to resist mutation and other metamorphic effects.",
    ),
)


def set_character_name_and_details_cacogen(char):
    char.name = choice(name_manner_misfortune_extrentricity_table)[0]
    char.details = get_character_details_cacogen()
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
