from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule

looks_table = (
    (
        "Ape",
        "Humanoid",
        "Biological",
        "Grey",
    ),
    (
        "Android",
        "Missing",
        "Bird-like",
        "Brassy",
    ),
    (
        "Barrel",
        "Sphere",
        "Bladed",
        "Bronze",
    ),
    (
        "Child",
        "Camera",
        "Broken",
        "Golden",
    ),
    (
        "Chimera",
        "TV Screen",
        "Crystalline",
        "Silver",
    ),
    (
        "Crab",
        "Mirrored",
        "Clawed",
        "Mirrored",
    ),
    (
        "Cube",
        "Bladed",
        "Golden",
        "Black",
    ),
    (
        "Cylinder",
        "Tendrils",
        "Hesitant",
        "Rusted",
    ),
    (
        "Falcon",
        "Square",
        "Jewelled",
        "White",
    ),
    (
        "Humanoid",
        "Mask-like",
        "Long",
        "Ochre",
    ),
    (
        "Judge",
        "Skeletal",
        "Precise",
        "Red",
    ),
    (
        "Lion",
        "Glass",
        "Retractable",
        "Blue",
    ),
    (
        "Locust",
        "Translucent",
        "Segmented",
        "Chameleon",
    ),
    (
        "Mantis",
        "Tubes",
        "Sharp",
        "Pink",
    ),
    (
        "Orb",
        "Plant-like",
        "Silver",
        "Iron",
    ),
    (
        "PrismSolar",
        "Panels",
        "Slender",
        "Purple",
    ),
    (
        "Priest",
        "Radar Dish",
        "Tentacles",
        "Umber",
    ),
    (
        "Pyramid",
        "Crystalline",
        "Translucent",
        "Striped",
    ),
    (
        "Serpent",
        "Star-shaped",
        "Tank-treads",
        "Green",
    ),
    (
        "Warrior",
        "Cyclops Eye",
        "Wheels",
        "Iridescent",
    ),
)


@dataclass
class SynthLooks:
    size: str
    form: str
    head: str
    limbs: str
    finish: str

    def __repr__(self):
        return f"{self.size} sized Synth with the shape of a {self.form}. {self.head} head, {self.limbs} limbs, and {self.finish} finish."


def get_synth_looks():
    data = [choice(looks_table)[k] for k in range(4)]
    size = [choice(("Small", "Medium", "Large", "Imposing"))]
    data = size + data
    return SynthLooks(*data)


name_made_for_but_you_realized_table = (
    (
        "Ojasin",
        "Art",
        "All Memories Are Lies",
    ),
    (
        "Farouk",
        "Punishment",
        "Azaroth Is the Only True God",
    ),
    (
        "Ishtar",
        "Flattery",
        "Chance Does Not Exist",
    ),
    (
        "Symeon",
        "Devotion",
        "Fate Does Not Exist",
    ),
    (
        "Irmina",
        "Cleaning",
        "Humanity Stole the Divine Spark",
    ),
    (
        "Kaori",
        "Healing",
        "Humans Are Machines",
    ),
    (
        "Cyriak",
        "Agriculture",
        "Machines Created Humanity",
    ),
    (
        "Quarqus",
        "Spacefaring",
        "Newbeasts Carry the Divine Spark",
    ),
    (
        "Fane",
        "Exploration",
        "Synthetic Minds Are More Devout",
    ),
    (
        "Arjuna",
        "Mining",
        "Synthetic Minds Are Stronger",
    ),
    (
        "Many-Moons",
        "Peacekeeping",
        "The Gods Are Mechanical",
    ),
    (
        "Lucjan",
        "Assassinations",
        "The Titans Never Existed",
    ),
    (
        "Jacintha",
        "Manufacturing",
        "The Titans Were the True Gods",
    ),
    (
        "Mneme",
        "Executioner",
        "Time Flows Backwards",
    ),
    (
        "Faustyn",
        "Scouting",
        "Time Is Circular",
    ),
    (
        "Elisebet",
        "Companionship",
        "Vaarn Is a Simulation",
    ),
    (
        "Paeon",
        "Scribing",
        "Vaarn Is Hell",
    ),
    (
        "Ulmon",
        "Strategy",
        "You Are Human",
    ),
    (
        "Xhiva",
        "Preaching",
        "You Must Awaken the Titans",
    ),
    (
        "Yathartha",
        "Conducting Scientific Research",
        "Your Memories Are Corrupted",
    ),
)

power_sources = (
    "an Artificial Photosynthesis",
    "a Plasma Core",
    "a Fusion Battery",
    "an Artificial Digestion",
    "a Symbiotic Internal Ecosystem",
    "Vampirism",
)

special_rules_data = (
    (
        "Synthetic Flesh",
        "You are a being of metal and plastic. You do not need to eat or breathe. You are immune to damage from suffocation, drowning, toxins, extreme temperatures, or spores. You suffer double damage from electrical weapons. When you receive Wounds, use the Synthetic Wounds table.",
    ),
    (
        "Synthetic Mind",
        "You are vulnerable to attacks that target the LogLang syntax that powers synths. These include strobing basilisk patterns, malicious infoglyphs, and ancient Titan-era language viruses. You suffer d6 INT damage per round from magnetic fields.",
    ),
    (
        "Repairs",
        "You cannot regain HP by consuming rations. You must make repairs using Synth Parts. You begin play with 3 spare Synth Parts, which stack in one item slot. A repair takes an hour and uses up one synth part. Repairs heal d8 + CON HP. If HP is full, heal one Wound. To extract parts from dead synthetic creatures, make an INT save. On a success, extract usable synth parts equal to their Level. On failure, extract one usable part.",
    ),
)


@dataclass
class SynthDetails:
    power_source: str
    you_were_made_for: str
    but_you_realised: str

    def __repr__(self):
        return f"Powered by {self.power_source}, you were made for {self.you_were_made_for} but you realised that {self.but_you_realised}."


def set_synth_details(char):
    data = [choice(name_made_for_but_you_realized_table)[k] for k in range(3)]
    data.insert(1, choice(power_sources))
    char.details = SynthDetails(*data[1:])
    char.name = data[0]
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
