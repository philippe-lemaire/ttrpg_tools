from random import choice, randint
from .dice import get_key
from dataclasses import dataclass

qualities = (
    "Shabby",
    "Decadent",
    "Ancestral",
    "Quicksilver",
    "Nano-weave",
    "Spiny",
    "Dazzling",
    "Tarnished",
    "Indigo",
    "Golden",
    "Symbiotic",
    "Biomechanical",
    "Occult",
    "Fungal",
    "Translucent",
    "Gaudy",
    "Sacred",
    "Iridescent",
    "Crystalline",
    "Ornate",
)

armor_types = {
    2: "Desert Robes (11 / 1 Slot)",
    4: "Hazard Wrap (12 / 3 Slots). ADV on Saves vs Radiation and Toxins",
    7: "War-Shirt (12 / 2 Slots)",
    12: "Brigandine (13 / 3 Slots)",
    15: "Cuirass (14 / 4 Slots)",
    18: "Chain-Mail (15 / 5 slots)",
    20: "Plate Armour (16 / 6 Slots). DIS when swimming or climbing.",
}


@dataclass
class Armor:
    quality: str
    armor_type: str

    def __repr__(self):
        return f"Armor: {self.quality} {self.armor_type}"


def gen_armor():
    quality = choice(qualities)
    armor_type = armor_types[get_key(randint(1, 20), armor_types)]
    return Armor(quality, armor_type)


helmets = (
    "Spiny Helm",
    "Dazzling Helm",
    "Ridiculous Helm",
    "Decadent Helm",
    "Ornate Helm",
    "Golden Helm",
    "Bone Helm",
    "Biomechanical Helm",
    "Occult Helm",
    "Fungal Helm",
    "Translucent Helm",
    "Gaudy Helm",
    "Sacred Helm",
    "Iridescent Helm",
    "Crystalline Helm",
)

shields = (
    "Wooden Shield",
    "Plastiglass Shield",
    "Nomad’s Shield",
    "Painted Shield",
    "Apeskin Shield",
    "Bone Shield",
    "Starburst Shield",
    "Gladiator’s Shield",
    "Fungal Shield",
    "Polychrome Shield",
    "Stone Shield",
    "Holy Fool’s Shield",
    "Temple-forged Shield",
    "Sickly Moon Shield",
    "Sun Flambeaux Shield",
)


def gen_helmet_and_shield():
    result = []
    r1 = randint(1, 20)
    if r1 > 5:
        result.append(helmets[r1 - 6])
    r2 = randint(1, 20)
    if r2 > 5:
        result.append(shields[r2 - 6])
    return result
