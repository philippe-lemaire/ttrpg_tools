from random import choice, sample
from dataclasses import dataclass

oracle_sanctum_data = (
    (
        "Crooked Tower",
        "Blind, Mute",
        "Reads Entrails",
    ),
    (
        "Deep Cave",
        "Bug-eyed, Ranting",
        "Reads Tea Leaves",
    ),
    (
        "Meteor Crater",
        "Paints Themselves Blue",
        "Tastes Your Blood",
    ),
    (
        "House on Stilts",
        "Second Head of a Cacogen",
        "Bibliomancy",
    ),
    (
        "Beneath Crystal Dome",
        "Ostentatious Hat",
        "Prophetic Dreams",
    ),
    (
        "Telescope Array",
        "Too Much Jewellery",
        "Automatic Writing",
    ),
    (
        "Stranded Submarine",
        "Always In Bath",
        "Reads Smoke",
    ),
    (
        "Inside Hollow Statue",
        "Head Twisted Backwards",
        "Tarot Cards",
    ),
    (
        "Inside Petrified Tree",
        "Levitates, Wants to Stop",
        "Consults Computer",
    ),
    (
        "Fungal Grove",
        "Missing a Limb",
        "Casting Bones",
    ),
    (
        "Amidst Ruined Village",
        "Eyes Sewn Open",
        "Casting Dice",
    ),
    (
        "Ancient Battlefield",
        "Diamond-tipped Teeth",
        "Weaves Prophetic Rugs",
    ),
    (
        "Amidst Empty Graves",
        "Addicted to Drug (p.xx)",
        "Scrying (Black Mirror)",
    ),
    (
        "Within Crystal Walls",
        "Heavily Damaged Synth",
        "Scrying (Pond)",
    ),
    (
        "Decrepit Windmill",
        "Coughs Up Live Insects",
        "Scrying (Crystal)",
    ),
    (
        "Ancient Toll Booth",
        "Bored by their Visions",
        "Psychedelic Visions",
    ),
    (
        "Satellite Relay",
        "Comically Untrustworthy",
        "Reads Bird Flight",
    ),
    (
        "Beneath Rusting Colossus",
        "Taciturn and Grim",
        "Consults the Dead",
    ),
    (
        "Hypergeometric Building",
        "Three Hairless Sisters",
        "Reads Sacred Flame",
    ),
    (
        "Beside Oasis (p.xx)",
        "Eyes Replaced with Stones",
        "Captive Quantum Daemon (p.xx)",
    ),
)
wants = (
    "Rival Oracle Humiliated",
    "To Find Love (very picky)",
    "A Prophecy Fulfilled (looks bad otherwise)",
    "A Pet (p.xx) to keep them company",
    "Object Stolen from Distant Archive (p.xx)",
    "A Very Specific Meal (p.xx)",
    "An Escort to Dangerous Location",
    "Protection from Seeker Recruiters (p.xx)",
    "Protection from Darkling Sun",
    "Recruiters (p.xx) A Quantum Daemon (p.xx) Killed",
)


@dataclass
class OracleSanctum:
    location: str
    oracle: str
    divination_method: str
    they_want: str

    def __repr__(self):
        return f"""The sanctum is located in a {self.location.lower()}, the Oracle who dwells there can be described as {self.oracle.lower()}.
        <br>
        Their divination method is {self.divination_method.lower()}.
        <br>
        The want {self.they_want.lower()}.
        """


def gen_oracle_sanctum():
    location = choice([line[0] for line in oracle_sanctum_data])
    oracle = choice([line[1] for line in oracle_sanctum_data])
    divination_method = choice([line[2] for line in oracle_sanctum_data])
    they_want = choice(wants)

    return OracleSanctum(location, oracle, divination_method, they_want)
