from random import randint, choice
from dataclasses import dataclass


exotica_data = (
    (
        "A Fool’s Head",
        "The severed head of a synthetic jester. Not in great condition but can still remember some jokes.",
    ),
    (
        "Agoniser",
        "A barbaric relic. Silver needle that causes unbearable pain to organic creatures without leaving a mark.",
    ),
    (
        "All-Purpose Idol",
        "Imbued with powerful neuro-active programming. Observers always believe the idol represents the deity they worship.",
    ),
    (
        "Black Heart",
        "Repulsive twitching cyborg organ. Will slowly and painfully revive a single dead body.",
    ),
    (
        "Blasphemies of the Binary Demon",
        "A tablet engraved with a series of quantum-logical propositions. Poses little threat to organic life but can be deadly to sentient machines.",
    ),
    (
        "Chameleon Cloak",
        "Perfectly matches the colour of its surroundings",
    ),
    (
        "Desiccated Mycomorph",
        "Tiny dried out fungus-man. A drop of blood will revive him.",
    ),
    (
        "Dried Crypt Lotus",
        "Grim flower that sprouts from the forehead of corpses. Sometimes kept as a keepsake of a lost companion.",
    ),
    (
        "Flesh of the Honeyed Lamb",
        "Stolen from the Cult of the Honeyed Lamb; ancient meat imbued with a powerful medicinal psychedelic.",
    ),
    (
        "Midas Bomb",
        "Transforms organic matter into gold.",
    ),
    (
        "Mirror Ring",
        "Projects a hologram copy of the wearer that mimics their actions.",
    ),
    (
        "Nightmare Box",
        "Small cube of unbreakable, dark-tinted glass. Has one small peephole. Those that look inside are paralysed by horror.",
    ),
    (
        "Pale Blade of Amun-Oh",
        "Priests of Amun-Oh pledge never to take a life; their white knives will cut through anything except living flesh.",
    ),
    (
        "Sandworm Horn",
        "Blow outdoors to summon a sandworm, if you are bold enough.",
    ),
    (
        "Singing Crystal",
        "When struck, sings loudly and beautifully for up to an hour.",
    ),
    (
        "Sky-seeking Salve",
        "Reverses effect of gravity on object it coats.Take care when outdoors.",
    ),
    (
        "Ulfire Candle",
        "Ulfire is the ninth colour; its light has the unusual quality of shining through solid objects. It is blocked by lead.",
    ),
    (
        "Unbearable Wax",
        "Black wax that increases in weight one hundred times as it dries. Single dose.",
    ),
    (
        "Vial of ICE-9",
        "One dose of an alchemical substance that transforms all water it touches into un-meltable ice.",
    ),
    (
        "Visualiser Helm",
        "Golden bubble-helmet that projects imagery of the wearer’s thoughts, whether they want it to or not.",
    ),
)


@dataclass
class Exotica:
    name: str
    effect: str

    def __repr__(self):
        return f"Exotica: <b>{self.name}</b>. {self.effect}"


def gen_exotica():
    return Exotica(*choice(exotica_data))


def get_exotica_list():
    return [Exotica(*data) for data in exotica_data]
