from random import choice, randint
from dataclasses import dataclass


name_and_looks_table = (
    (
        "Abandon",
        "Natural",
        "None",
        "Communicate via Puppet",
    ),
    (
        "Anzah ",
        "Turquoise",
        "Child",
        "Squeaky Vox-box",
    ),
    (
        "Blackchapel",
        "Tan ",
        "Autarch",
        "Booming Vox-box",
    ),
    (
        "Critch",
        "Bronze",
        "Fool",
        "Muted Vox-box",
    ),
    (
        "Dolm",
        "Smoke",
        "Judge",
        "Synthetic Eyes",
    ),
    (
        "Faulkner",
        "White",
        "Knight",
        "Heavy Scarring",
    ),
    (
        "Fludd",
        "Black",
        "Sage",
        "Human Teeth Necklace",
    ),
    (
        "Havoc",
        "Azure",
        "Scholar",
        "Religious Paraphernalia",
    ),
    (
        "Hildebrand",
        "Emerald",
        "Maiden",
        "Ritual Scarring",
    ),
    (
        "Holk",
        "Rose",
        "Mother",
        "Heavily Tattooed",
    ),
    (
        "Jarl",
        "Orange",
        "Crone",
        "Regular Animal as Pet",
    ),
    (
        "Lurch",
        "Golden",
        "Mirrored",
        "Human Child as Pet",
    ),
    (
        "Obiah",
        "Silver",
        "Glitching",
        "Missing Limb",
    ),
    (
        "Plutarch",
        "Ochre",
        "Furious",
        "Gold Teeth",
    ),
    (
        "Sy",
        "Indigo",
        "Joyful",
        "Criminal Branding",
    ),
    (
        "Tarceny",
        "Violet",
        "Sorrowful",
        "Extensive Jewellery",
    ),
    (
        "Typhon",
        "Rust",
        "Alluring",
        "Hate Animal You Resemble",
    ),
    (
        "Vodalus",
        "Olive",
        "Cracked",
        "Love Animal You Resemble",
    ),
    (
        "Wellbeloved",
        "Lazulite",
        "Blank",
        "Won’t Wear Clothes",
    ),
    (
        "Wermouth",
        "Opalescent",
        "Patriarch",
        "Believe Yourself Human",
    ),
)


@dataclass
class NewBeastLooks:
    hue: str
    mask: str
    quirk: str

    def __repr__(self):
        return f"{self.hue} hue, {self.mask} mask. Quirk: {self.quirk}."


def get_newbeast_looks():
    data = [choice(name_and_looks_table)[k] for k in range(1, 4)]
    return NewBeastLooks(*data)


species_table = (
    "New-Aardvark",
    "New-Coyote",
    "New-Axoltyl",
    "New-Anemone",
    "New-Addax",
    "New-Skink",
    "New-Cat",
    "New-Centipede",
    "New-Leopard",
    "New-Gazelle",
    "New-Panther",
    "New-Python",
    "New-Lion",
    "New-Porcupine",
    "New-Hyena",
    "New-Tiger",
    "New-Worm",
    "New-Gecko",
    "New-Hog",
    "New-Rooster",
    "New-Hound",
    "New-Iguana",
    "New-Gibbon",
    "New-Hen",
    "New-Wolf",
    "New-Tortoise",
    "New-Scorpion",
    "New-Slug",
    "New-Badger",
    "New-Fox",
    "New-Spider",
    "New-Mongoose",
    "New-Bear",
    "New-Owl",
    "New-Locust",
    "New-Baboon",
    "New-Oryx",
    "New-Vulture",
    "New-Mantis",
    "New-Lynx",
    "New-Armadillo",
    "New-Ostrich",
    "New-Ape",
    "New-Shrew",
    "New-Camel",
    "New-Kangaroo",
    "New-Mandrill",
    "New-Duck",
    "New-Sheep",
    "New-Rattlesnake",
    "New-Gorilla",
    "New-Falcon",
    "New-Bat",
    "New-Frog",
    "New-Hawk",
    "New-Fennec",
    "New-Horse",
    "New-Crocodile",
    "New-Raven",
    "New-Weasel",
    "New-Goat",
    "New-Hippo",
    "New-Crow",
    "New-Rat",
    "New-Wren",
    "New-Elephant",
    "New-Ox",
    "New-Ferret",
    "New-Mouse",
    "New-Jackal",
    "New-Bull",
    "New-Orangutang",
    "New-Hare",
    "New-Ibis",
    "New-Mole",
    "New-Cobra",
    "New-Toad",
    "New-Flamingo",
    "New-Bison",
    "New-Scarab",
)


def set_newbeast_name_and_animal(char):
    names = [row[0] for row in name_and_looks_table]
    char.name = choice(names)
    char.ancestry = char.ancestry + f" ({choice(species_table)})"
