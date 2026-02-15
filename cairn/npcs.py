from random import choice, randint
from dataclasses import dataclass

name1_name2_name3_quirk = (
    (
        "Alaric",
        "Ainsley",
        "Alder",
        "Alert",
    ),
    (
        "Carver",
        "Azura",
        "Alistair",
        "Bald",
    ),
    (
        "Cleaver",
        "Brave",
        "Caius",
        "Bright Eyes",
    ),
    (
        "Darnel",
        "Callan",
        "Dain",
        "Broad Face",
    ),
    (
        "Eoin",
        "Cedric",
        "Dax",
        "Crooked Teeth",
    ),
    (
        "Evander",
        "Crow",
        "Dorian",
        "Gaunt",
    ),
    (
        "Glyph",
        "Finch",
        "Godric",
        "Good Posture",
    ),
    (
        "Hemlock",
        "Gunnar",
        "Harkin",
        "Grimy",
    ),
    (
        "Herald",
        "Harper",
        "Hildred",
        "Harsh Voice",
    ),
    (
        "Lisbeth",
        "Liora",
        "Kael",
        "Heavy Brow",
    ),
    (
        "Lucian",
        "Lira",
        "Kavi",
        "Limps",
    ),
    (
        "Luna",
        "Lorelai",
        "Mariner",
        "Missing Ear",
    ),
    (
        "Lysander",
        "Lysandra",
        "Nazira",
        "Muscular",
    ),
    (
        "Marius",
        "Marcellus",
        "Onyx",
        "Notable Hair",
    ),
    (
        "Mend",
        "Shade",
        "Rolan",
        "Pleasant Voice",
    ),
    (
        "Milo",
        "Shroud",
        "Rush",
        "Squints",
    ),
    (
        "Neria",
        "Spade",
        "Sky",
        "Strong",
    ),
    (
        "Pan",
        "Spike",
        "Storm",
        "Thick Eyebrows",
    ),
    (
        "Quill",
        "Tanner",
        "Taros",
        "Tired",
    ),
    (
        "Seraphine",
        "Thyme",
        "Thaddeus",
        "Young",
    ),
)


background_goal_virtue_vice = (
    (
        "Academic",
        "Ascension",
        "Cautious",
        "Aloof",
    ),
    (
        "Assassin",
        "Cleansing",
        "Compassionate",
        "Corrupt",
    ),
    (
        "Blacksmith",
        "Conservation",
        "Connected",
        "Craven",
    ),
    (
        "Farmer",
        "Defense",
        "Courageous",
        "Cruel",
    ),
    (
        "General",
        "Domination",
        "Disciplined",
        "Cynical",
    ),
    (
        "Gravedigger",
        "Enrichment",
        "Discreet",
        "Deceptive",
    ),
    (
        "Guard",
        "Expansion",
        "Honest",
        "Greedy",
    ),
    (
        "Healer",
        "Freedom",
        "Intelligent",
        "Impulsive",
    ),
    (
        "Jailer",
        "Healing",
        "Judicious",
        "Incompetent",
    ),
    (
        "Laborer",
        "Integration",
        "Loyal",
        "Inflexible",
    ),
    (
        "Lord",
        "Justice",
        "Methodical",
        "Manipulative",
    ),
    (
        "Merchant",
        "Peace",
        "Meticulous",
        "Mercurial",
    ),
    (
        "Monk",
        "Power",
        "Polite",
        "Naive",
    ),
    (
        "Mystic",
        "Preservation",
        "Popular",
        "Pedantic",
    ),
    (
        "Outlander",
        "Purification",
        "Pragmatic",
        "Ruthless",
    ),
    (
        "Peddler",
        "Redemption",
        "Resourceful",
        "Sarcastic",
    ),
    (
        "Politician",
        "Revenge",
        "Suave",
        "Selfish",
    ),
    (
        "Spy",
        "Survival",
        "Shrewd",
        "Stubborn",
    ),
    (
        "Thief",
        "Unity",
        "Tenacious",
        "Vain",
    ),
    (
        "Thug",
        "Wealth",
        "Witty",
        "Xenophobic",
    ),
)


@dataclass
class NPC:
    name: str
    quirk: str
    background: str
    goal: str
    virtue: str
    vice: str


def gen_cairn_npc():
    name_table_index = randint(0, 2)
    name = choice(name1_name2_name3_quirk)[name_table_index]
    quirk = choice(name1_name2_name3_quirk)[-1]
    background, goal, virtue, vice = (
        choice(background_goal_virtue_vice)[k] for k in range(4)
    )
    return NPC(
        name=name,
        quirk=quirk,
        background=background,
        goal=goal,
        virtue=virtue,
        vice=vice,
    )
