from random import choice
from dataclasses import dataclass


qualities = (
    "Ultraviolet",
    "Engraved",
    "Flexglass",
    "Crystalline",
    "Ceramic",
    "Polychrome",
    "Quicksilver",
    "Spiny",
    "Transparent",
    "Bejewelled",
    "Stone",
    "Plasteel",
    "Flowstone",
    "Luminous",
    "Golden",
    "Bronze",
    "Sky-Iron",
    "Azure",
    "Magnetised",
    "Lurid",
)

shapes = (
    "Cauldron",
    "Pot",
    "Skull",
    "Urn",
    "Vase",
    "Sphere",
    "Pyramid",
    "Helm",
    "Gourd",
    "Kettle",
    "Bottle",
    "Amphora",
    "Flagon",
    "Jug",
    "Teapot",
    "Chalice",
    "Barrel",
    "Cube",
    "Thermos",
    "Eyeball",
)


@dataclass
class Crucible:
    quality: str
    shape: str

    def __repr__(self):
        return f"<b>Alchemist’s Crucible</b>: {self.quality} {self.shape}"


def gen_crucible():
    quality = choice(qualities)
    shape = choice(shapes)
    return Crucible(quality=quality, shape=shape)
