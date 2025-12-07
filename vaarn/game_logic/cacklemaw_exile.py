from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule

looks_table = (
    (
        "Dark and Coarse",
        "Yellow Daggers",
        "Raucous",
        "Human-Leather Jacket",
    ),
    (
        "Pale and Downy",
        "Little Brown Nubs",
        "Whispery",
        "Translucent Plastic",
    ),
    (
        "Riven with Scars",
        "White and Gleaming",
        "Machine-gun Barks",
        "Greasy Rags",
    ),
    (
        "Greasy Spikes",
        "Mostly Rotted Out",
        "Rusty Hinge",
        "Mock Wedding Clothes",
    ),
    (
        "Brindled",
        "One Gold Tooth",
        "Whooping",
        "Gaudy Shawl",
    ),
    (
        "Mostly Burnt Off",
        "Hooked and Grimy",
        "Coughing",
        "Mock Religious Attire",
    ),
    (
        "Long and Silky",
        "Chrome Implants",
        "Hissing Snicker",
        "Unsettling Mask",
    ),
    (
        "Short and Scratchy",
        "Needle Thin",
        "Breathless",
        "Harlequin’s Motley",
    ),
    (
        "Purest White",
        "Triple Row, Like a Shark",
        "Booming",
        "Bloodstained Bandages",
    ),
    (
        "Mottled Brown",
        "Diamond Hard Gnashers",
        "Hoarse and Strangled",
        "Sun-faded Scraps",
    ),
    (
        "Regal Silver",
        "Blunt and Black",
        "Maddening Gasps",
        "Plastic Bags",
    ),
    (
        "Concrete Grey",
        "Just One Left",
        "Wet Chuckles",
        "Iridescent Chains",
    ),
    (
        "Curly and Rancid",
        "Crooked Orange Spikes",
        "Turns into Hiccups",
        "Purple Silks",
    ),
    (
        "Dyed Blood Red",
        "Engraved with Pictures",
        "Starts Quiet and Rises",
        "Mock Hegemony Uniform",
    ),
    (
        "Shaved into Stripes",
        "Full of Holes",
        "Joyless Giggling",
        "A Rival’s Skin",
    ),
    (
        "Midnight Black",
        "Huge, Tusk-like",
        "Pained",
        "Spiked Shoulder-pads",
    ),
    (
        "Muddy Brown",
        "Giant Underbite",
        "Cold and Malevolent",
        "Soiled Hazmat Gear",
    ),
    (
        "Crawling with Parasites",
        "Ridiculous Overbite",
        "Childish and Cruel",
        "Peacock-Feather Cape",
    ),
    (
        "Thundercloud Blue",
        "Canted and Greying",
        "Could Wake the Dead",
        "Lizard-Skin Suit",
    ),
    (
        "Tigerish Stripes",
        "Weirdly Human",
        "Soundless but Horrid",
        "Nothing but Knives",
    ),
)


@dataclass
class CacklemawExileLooks:
    pelt: str
    teeth: str
    face: str
    hair: str

    def __repr__(self):
        return f"{self.teeth.capitalize()} teeth, {self.face.lower()} face, {self.hair.lower()} hair, {self.pelt.lower()} pelt."


def gen_looks_cacklemaw_exile():
    attributes = [choice(looks_table)[i] for i in range(4)]
    return CacklemawExileLooks(*attributes)


names = (
    "Bawlbray",
    "Bunny",
    "Darling",
    "Domino",
    "Fang",
    "Gidge",
    "Grot",
    "Jigsore",
    "Katanary",
    "Longsnout",
    "Nadir",
    "Natcher",
    "Palecrow",
    "Pinkeye",
    "Sabbat",
    "Snoutrout",
    "Sweetmeat",
    "Vileglory",
    "Wetshriek",
    "Zef",
)

manners = (
    "Cringing",
    "Jittery",
    "Sly",
    "Resentful",
    "Judgemental",
    "Pious",
    "Greedy",
    "Belligerent",
    "Sinister",
    "Repellent",
    "Jovial",
    "Bold",
    "Grouchy",
    "Treacherous",
    "Childish",
    "Extravagant",
    "Volatile",
    "Gullible",
    "Fickle",
    "Calculating",
)

exile_reasons = (
    "Born a Runt",
    "Showed Mercy",
    "Laugh Too Annoying",
    "Cowardice",
    "Asked Questions",
    "Insubordination",
    "Fought Alongside Humans",
    "Desecrated Ritual Puppet",
    "Shared Clan Secret",
    "Ridiculous Petty Reason",
)

laughs = (
    "Blood",
    "Guts",
    "Pain",
    "Beheadings",
    "Hangings",
    "Drownings",
    "Begging",
    "Pleading",
    "Weeping",
    "Arson",
    "Larceny",
    "Vandalism",
    "Screams",
    "Gunfights",
    "Speeding",
    "Explosions",
    "Throttling",
    "Biting People",
    "Chemical Warfare",
    "Puns",
)

special_rules_data = (
    (
        "No Quarter",
        " You must EGO save to show mercy to a defeated foe, or to retreat from a fight.",
    ),
    (
        "Biter",
        " If you successfully hit a foe with a melee attack, you may add an extra d6 of fang damage to the roll. ",
    ),
    (
        "More!",
        " When you kill a foe with a melee attack, you may immediately make another melee attack against a nearby target.",
    ),
)


@dataclass
class CharacterDetailsCackleMawExile:
    manner: str
    exile_reason: str
    makes_you_laugh: str

    def __repr__(self):
        return f"{self.manner.capitalize()} manner. Reason for exile: {self.exile_reason.lower()}. {self.makes_you_laugh} makes them laugh."


def get_character_detail_caklemaw_exile():
    manner = choice(manners)
    exile_reason = choice(exile_reasons)
    makes_you_laugh = choice(laughs)
    return CharacterDetailsCackleMawExile(manner, exile_reason, makes_you_laugh)


def set_character_name_and_details_cacklemaw_exile(char):
    char.name = choice(names)
    char.details = get_character_detail_caklemaw_exile()
    char.looks = gen_looks_cacklemaw_exile()
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)
