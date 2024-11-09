import random
from math import ceil


def roll(dice):
    dice = dice.lower()
    if dice[0].isdigit():
        n, size = dice.split("d")
        n = int(n)
        size = int(size)
    elif dice[0] == "d":
        size = int(dice[1:])
        n = 1
    result = 0
    for _ in range(n):
        result += random.randint(1, size)
    return result


male_fornames = [
    "Augost",
    "Benedict",
    "Brin",
    "Chumwan",
    "Calahed",
    "Dorren",
    "Emmett",
    "Felix",
    "Fred",
    "Grobin",
    "Gizard",
    "Helroff",
    "Istan",
    "Ilmer",
    "Junas",
    "Katsun",
    "Lurpax",
    "Litton",
    "Munfud",
    "Narmun",
    "Orren",
    "Podder",
    "Peta",
    "Picklow",
    "Pipp",
    "Quinn",
    "Rosher",
    "Stellan",
    "Samford",
    "Tucker",
    "Teevan",
    "Urntin",
    "Varran",
    "Vanis",
    "Volta",
    "Weckster",
    "Yurnak",
    "Zarm",
]

female_forenames = [
    "Augosta",
    "Benedicta",
    "Breen",
    "Chumwel",
    "Calit",
    "Dorret",
    "Emma",
    "Felora",
    "Freda",
    "Grobina",
    "Giza",
    "Helriel",
    "Isti",
    "Ilda",
    "Julia",
    "Katsin",
    "Lunda",
    "Littona",
    "Munfi",
    "Nadya",
    "Orrena",
    "Poddin",
    "Peta",
    "Pickelle",
    "Pippita",
    "Quinn",
    "Roshel",
    "Stella",
    "Sambay",
    "Tuckis",
    "Teeva",
    "Urna",
    "Varin",
    "Vanissa",
    "Voltel",
    "Weckin",
    "Yurna",
    "Zarm",
]
surnames = [
    "Allane",
    "Bargroll",
    "Brunfield",
    "Chop",
    "Creed",
    "Dunbell",
    "Eggler",
    "Fox",
    "Farsee",
    "Gill",
    "Gullwin",
    "Huckle",
    "Horrican",
    "Ingle",
    "Jongler",
    "Kross",
    "Lix",
    "Lowbile",
    "Montane",
    "Nutbush",
    "Olifant",
    "Offenpot",
    "Ouze",
    "Phile",
    "Parfait",
    "Quigley",
    "Regal",
    "Stagger",
    "Shark",
    "Tumble",
    "Terrine",
    "Underhog",
    "Upperill",
    "Volfhole",
    "Vinifera",
    "Wickerspin",
    "Yarn",
    "Zarrack",
]

arcana = [
    "Gatekeeper’s Sigil",
    "Pierced Heart",
    "Pale Flame",
    "Soul Chain",
    "Gavel of the Unbreakable Seal",
    "Foul Censer",
    "Bleeding Stave",
    "Pain Idol",
    "Webbed Hands",
    "Sunblessed Bands",
    "Flesh-Tome of Babble",
    "Tyrant’s Rod",
    "Black Veil",
    "Strands of Suffering",
    "Heat Ray",
    "Miniaturisation Coil",
    "Frozen Cloud",
    "Many Phase Key",
    "Skull Magnet",
    "Transreal Mirror",
    "Gorger’s Mask",
    "Tomb Box",
    "Howling Lantern",
    "Rainbow Blade",
    "Hawk of Prosperity",
    "Inquisitor’s Hood",
    "Winter’s Sickle",
    "Grief Cup",
    "Victory Globe",
    "Moon Lens",
    "Fool’s Coin",
    "Chance Rose",
    "Homing Stick",
    "False Platter",
    "Gold Visor",
    "Infinity Icon",
]

starter_package_table = {
    9: [
        "Sword (d6), Pistol (d6), Modern Armour, <em>Sense nearby unearthly beings</em>",
        "Musket (d8 B), Sword (d6), Flashbang, <em>Sense nearby Arcana</em>",
        "Musket (d8 B), Club (d6), <em>Immunity to extreme heat and cold</em>",
        "Pistol (d6), Knife (d6), <em>Telepathy if target fails WIL Save</em>",
        "Blunderbuss (d8 B), Hatchet (d6), Mutt, <em>Dreams show your undiscovered surroundings</em>",
        "Musket (d8 B), Hatchet (d6), Flashbang, Arcanum, <em>Iron Limb</em>",
    ],
    10: [
        "Rifle (d8 B), Bayonet (d6), Lighter Boy, Arcanum",
        "Musket (d8 B), Hatchet (d6), Hawk, Arcanum",
        "Musket (d8 B), Protective Gloves, Arcanum",
        "Claymore (d8 B), Pistol (d6), 2 Acid Flasks, Arcanum",
        "Brace of Pistols (d8 B), Steel Wire, Grappling Hook, Arcanum",
        "Rifle (d8 B), Mace (d6), Eagle, Poison",
    ],
    11: [
        "Rifle (d8 B), Modern Armour, Hound, Arcanum",
        "Hatchet (d6), Pistol (d6), Bolt-Cutters, Arcanum",
        "Musket (d8 B), Mallet, Marbles, Fancy Hat, Arcanum",
        "Musket (d8 B), Bayonet (d6), Mutt with telepathic link",
        "Machete (d6), Brace of Pistols (d8 B), Talking Parrot, <em>Never Sleep</em>",
        "Club (d6), 3 Bombs, Rocket, <em>Darkvision</em>",
    ],
    12: [
        "Club (d6), Throwing Knives, Arcanum",
        "Musket (d8 B), Mule, Arcanum",
        "Pick-Axe (d6), Manacles, Arcanum",
        "Pistol (d6), Rocket, <em>Toxin-Immune</em>",
        "Harpoon Gun (d8 B), Baton (d6), Acid, <em>Slightly Magnetic</em>",
        "Maul (d8 B), Dagger (d6), Chain",
    ],
    13: [
        "Pistol (d6), Ether, Poison, Arcanum",
        "Sword (d6), Pistol (d6), Crude Armour",
        "Pistol (d6), Smoke-bomb, Mutt, Shovel",
        "Musket (d8 B), Portable Ram, Game Set",
        "Bolt-Cutters, Blunderbuss (d8 B), Fiddle",
        "Longaxe (d8 B), Rum, Bomb",
    ],
    14: [
        "Cane (d6), Acid, Spyglass, Arcanum",
        "Pistol (d6), Bell, Steel Wire, Smoke-bomb",
        "Longaxe (d8 B), Throwing Axes, Fire Oil",
        "Pistol (d6), Saw, Animal Trap, Spyglass",
        "Pistol (d6), Grease, Hand Drill, Drum",
        "Dagger (d6), Fire Oil, Mirror",
    ],
    15: [
        "Brace of Pistols (d8 B), Canary, Ether",
        "Longaxe (d8 B), Ferret, Fire Oil",
        "Club (d6), Ether, Crowbar, Flute",
        "Bow (d6 B), Knife (d6), Rocket, Fire Oil",
        "Sword & Dagger (d8 B), Magnifying Glass, <em>Lost Eye</em>",
        "Pistol (d6), Knife (d6), Bomb, Saw",
    ],
    16: [
        "Musket (d8 B), Pocket-watch, Bomb",
        "Staff (d6 B), Tongs, Glue",
        "Hatchet (d6), Net, Fire Oil, <em>Burnt Face</em>",
        "Pistol (d6), Whip (d6), Cigars, <em>Lost Eye</em>",
        "Pistol (d6), Acid, Animal Repellent, <em>Prosthetic Hand</em>",
        "Pistol (d6), Bomb, Shovel, <em>Glowing Eyes</em>",
    ],
    17: [
        "Halberd (d8 B), Fake Pistol, Artificial Lung",
        "Pistol (d6), Net, Trumpet, <em>Prosthetic Leg</em>",
        "Club (d6), Paint, Crowbar, <em>Loud Lungs</em>",
        "Musket (d8 B), Accordion, <em>No Nose/Scent</em>",
        "Sword (d6), Steel Wire, <em>Ugly Mutation</em>",
        "Staff (d6 B), Throwing Knives (d6)",
    ],
    18: [
        "Garotte (d6), Musket (d8 B), <em>Mute</em>",
        "Pistol (d6), Grease, Hacksaw, <em>One Arm</em>",
        "Pistol (d6), Cigars, Poison, <em>Fugitive</em>",
        "Sword (d6), Shield. Illiterate</em>",
        "Sword (d6), Ferret, Tattered Clothes. Debt (3G)</em>",
        "Mace (d6), Pigeon. Disfigured</em>",
    ],
}

mutant_starter_package_table = {
    10: [
        "mutation mutation mutation Crossbow (d6 B)",
        "mutation mutation Pistol (d6)",
        "mutation mutation Maul (d8 B)",
    ],
    13: [
        "mutation mutation mutation Mace (d6)",
        "mutation mutation Knife (d6)",
        "mutation mutation Bow (d6 B)",
    ],
    15: [
        "mutation mutation Longaxe (d8 B) Crude Armour",
        "mutation mutation Club (d6) Shield",
        "mutation mutation Mace (d6) Shield",
    ],
    17: [
        "mutation mutation Bow (d6 B) Acid",
        "mutation mutation Knife (d6) Poison",
        "mutation mutation Axe (d6) Hooch",
    ],
    19: [
        "mutation Club (d6) Wire",
        "mutation Staff (d6 B) Glue",
        "mutation Spear (d8 B) Lantern",
    ],
    20: ["mutation Brick (d6)", "mutation Spike (d6)", "mutation Rope"],
}

mutations = {
    1: "Giant Head",
    5: "Bone Claws (d6 Damage)",
    7: "Bat Wings",
    9: "Spit Acid (d8 Damage)",
    11: "Third Eye (sense clues about people)",
    13: "Covered in Barnacles",
    15: "Nature Kinship (talk to animals and plants)",
    17: "Illusionist (fool one person at a time)",
    19: "Chitinous Shell (Armour 1)",
    22: "Venom (d6 STR Loss on Critical Damage)",
    24: "Spider Climb",
    26: "Boneless",
    29: "Bloodsucker (regain lost STR when you feed)",
    33: "Compound Eyes (see all around you)",
    37: "Bug Wings",
    39: "Gills",
    41: "Toady Skin",
    43: "Glorious Mane",
    46: "Slug-Like",
    49: "Cyclops",
    53: "Constant Drooler",
    56: "Red-Gaze (d8 Damage)",
    59: "Ruster (touch rusts metal)",
    62: "Huge Jaws",
    65: "Cocoon (sleep in an Armour 2 shell)",
    69: "Prehensile Tail",
    73: "Echolocation",
    77: "Heat Vision (see heat signatures)",
    79: "Devourer (eat anything for nourishment)",
    82: "Living Hive (swarm of bugs live in you)",
    83: "Explosive (d12 Damage blast when you die)",
    85: "Spray Ink",
    87: "Morph (change face at will)",
    89: "Void (annihilate objects you grasp)",
    92: "Spores (choke opponents)",
    95: "Camouflage",
    97: "Psychedelic Skin",
    99: "Horns",
    100: "Hooves",
}


def get_closest_key(n, d):
    for key in d.keys():
        if key >= n:
            return d[key]
    return None


def get_name(gender):
    if gender == "Male":
        forename = random.choice(male_fornames)
    else:
        forename = random.choice(female_forenames)
    surname = random.choice(surnames)
    return f"{forename} {surname}"


class Character:
    def __init__(self):
        self.STR = roll("3D6")
        self.DEX = roll("3D6")
        self.WIL = roll("3D6")
        self.HP = roll("1D6")
        self.gender = random.choice(("Male", "Female"))
        self.name = get_name(self.gender)
        best_stat = max(self.STR, self.DEX, self.WIL)
        if best_stat < 9:
            best_stat = 9
        self.starter_package = starter_package_table.get(best_stat)[self.HP - 1].split(
            ", "
        )
        self.starter_package = [
            item.replace("Arcanum", f"Arcanum: {random.choice(arcana)}")
            for item in self.starter_package
        ]

    def __repr__(self):
        return f"{self.name}\n{self.gender}\nHP: {self.HP}\nSTR: {self.STR}\nDEX: {self.DEX}\nWIL {self.WIL}\n{self.starter_package}"


class MutantCharacter:
    def __init__(self):
        self.STR = roll("1d20")
        self.DEX = roll("1d20")
        self.WIL = roll("1d20")
        self.HP = roll("1D6")
        self.gender = random.choice(("Male", "Female"))

        self.name = get_name(self.gender)
        best_stat = max(self.STR, self.DEX, self.WIL)
        index = ceil(self.HP / 2) - 1
        package_list = get_closest_key(best_stat, mutant_starter_package_table)[
            index
        ].split(" ")
        # deal with mutations
        n_mutations = package_list.count("mutation")
        rolled_mutations = [
            get_closest_key(roll("1d100"), mutations) for mut in range(n_mutations)
        ]

        # self.starter_package = ", ".join(rolled_mutations + package_list[n_mutations:])
        self.starter_package = rolled_mutations + package_list[n_mutations:]

    def __repr__(self):
        return f"{self.name}\n{self.gender}\nHP: {self.HP}\nSTR: {self.STR}\nDEX: {self.DEX}\nWIL {self.WIL}\n{self.starter_package}"


unhuman_types_table = {
    2: "Stocky, beard, know everything about rocks.  Immune to poison, d12+6 STR. Axe.",
    4: "Small and pudgy, hide in tiny places, 2d6 STR, 2d6+6 WIL.  Dagger.",
    6: "Slender, unaging, immortal. Pass a WIL Save to perform subtle trickery that may appear as magic. 2d6+6 DEX. Sword and Bow.",
    8: "Ugly, animalistic features. d12+8 STR, d10 WIL.  Heavy two-handed chopper (d8).",
    10: "Tiny, green, sort of creepy looking. 2d6 STR and WIL, d12+6 DEX. Dagger.",
    11: "Scales, breath weapon (d8) and immunity based on colour. Red (Fire), Black/Green (Acid), Blue (Lightning), White (Cold). Sword.",
    13: "Tiny, bald, know everything about machines, talk to burrowing animals. 2d6 STR. Musket.",
    14: "Made of living wood and stone. Immune to anything that would affect living tissue. Rifle.",
    16: "Intelligent Ape. d12+6 DEX. Musket.",
    17: "Wings, beak, and talons. Fly quite well. d6+3 STR. Musket.",
    18: "Grey skin, white hair, talk to bugs, see perfectly in darkness.  Sword and Poison.",
    20: "Twice normal size. d6+14 STR, d10 DEX. Weapons specially made for you are bumped up to the next size die. Hand Weapons cause d8, Field Weapons cause d10 etc. Maul (d10).",
}

unhuman_starter_packages = {
    2: "Arcanum, Cult Symbol",
    3: "Arcanum, Poison",
    4: "Hound",
    5: "Arcanum, Ether",
    6: "Staff (d6 B), Raven",
    7: "Pistol Brace (d8)",
    8: "Arcanum, Shackles",
    9: "Fancy Sword (d8)",
    10: "Elaborate Clothes",
    11: "Fancy Pistol (d8)",
    12: "Pistol, Incredible Hat",
    13: "Blunderbuss (d8)",
    14: "Greatsword (d8)",
    15: "Shield, Sword (d6)",
    16: "Cult Symbol",
}

human_perceptions = [
    "No idea you exist.",
    "You're just a rumour.",
    "Word is starting to spread.",
    "One bad example is publicly known.",
    "One good example is publicly known.",
    "Lots of stories, but you're still hidden.",
    "You went into hiding a few years ago.",
    "They think you’re from the Golden Lands (you’re not).",
    "They think you’re a mutant from the Underground (you're not).",
    "They think you’re from space (you’re not).",
    "They want you dead!",
    "Incredibly stereotyped, generally bad.",
    "Incredibly stereotyped, generally good.",
    "Generally a good reputation.",
    "Generally a bad reputation.",
    "Good history, but things are turning sour.",
    "Bad history, but things are generally okay now.",
    "You work closely with them.",
    "They don't care.",
    "They think you're great.",
]


class UnhumanCharacter(Character):
    def __init__(self):
        super().__init__()
        self.unhuman_type = get_closest_key(roll("1d20"), unhuman_types_table)
        if self.unhuman_type.startswith("Stocky"):
            self.STR = roll("d12") + 6
            self.starter_package = "Axe"
        elif self.unhuman_type.startswith("Small"):
            self.STR = roll("2d6")
            self.WIL = roll("2d6") + 6
            self.starter_package = "Dagger"
        elif self.unhuman_type.startswith("Slender"):
            self.DEX = roll("2d6") + 6
            self.starter_package = "Sword and Bow"
        elif self.unhuman_type.startswith("Ugly"):
            self.STR = roll("d12") + 8
            self.WIL = roll("d10")
            self.starter_package = "Heavy two-handed chooper (d8)"
        elif self.unhuman_type.startswith("Tiny, green"):
            self.STR = roll("2d6")
            self.DEX = roll("2d6") + 6
            self.WILL = roll("2d6")
            self.starter_package = "Dagger"
        elif self.unhuman_type.startswith("Tiny, bald"):
            self.STR = roll("2d6")
            self.starter_package = "Musket"
        elif self.unhuman_type.startswith("Scales"):
            self.starter_package = "Sword"
        elif self.unhuman_type.startswith("Intelligent Ape"):
            self.DEX = roll("d12") + 6
            self.starter_package = "Musket"
        elif self.unhuman_type.startswith("Wings"):
            self.STR = roll("d6") + 3
            self.starter_package = "Musket"
        elif self.unhuman_type.startswith("Twice"):
            self.STR = roll("d6") + 14
            self.DEX = roll("d10")
            self.starter_package = "Maul (d10)"
        elif self.unhuman_type.startswith("Grey skin"):
            self.starter_package = "Sword and Poison"
        elif self.unhuman_type.startswith("Made of living"):
            self.starter_package = "Rifle"
        self.starter_package += (
            f", {unhuman_starter_packages.get(self.HP + roll('1d10'))}"
        )
        self.starter_package = self.starter_package.replace(
            "Arcanum", f"Arcanum: {random.choice(arcana)}"
        )
        self.starter_package = self.starter_package.split(", ")
        self.human_perception = random.choice(human_perceptions)


simple_folk_starter_package_table = {
    7: [
        "Bow (d6 B), Crude Armour Trinket Trinket Trinket",
        "Rod (d6), Eyepatch Trinket Trinket Trinket",
        "Sling (d6), One Leg Trinket Trinket Trinket",
    ],
    8: [
        "Bow (d6 B), Trinket Trinket",
        "Shield, Trinket Trinket",
        "Whistle, Trinket Trinket",
    ],
    9: [
        "Shield Hammer (d6), Trinket Trinket",
        "Hatchet (d6), One Ear, Trinket",
        "Stick (d6), Extra Ear, Trinket",
    ],
    10: [
        "Flail (d8 B), Trinket Trinket",
        "Shield, Trinket",
        "Bow (d6 B), Trinket",
    ],
    11: [
        "Crude Armour, Trinket Trinket",
        "Bow (d6), Trinket",
        "Shovel (d6), Trinket",
    ],
    12: [
        "Hatchet (d6), Trinket Trinket",
        "Crude Armour, Trinket",
        "Drum, Trinket",
    ],
    13: [
        "Club (d6), Crude Armour, Trinket Trinket",
        "Machete (d6), No Nose, Trinket",
        "Spike (d6), Mute, Trinket",
    ],
    14: [
        "Crossbow (d6 B), Trinket Trinket",
        "Greataxe (d8 B), Trinket",
        "Maul (d8 B), Trinket",
    ],
    15: [
        "Sword (d6), Shield, Trinket",
        "Axe (d6), Shield, Trinket",
        "Bow (d6 B), Hawk, Trinket",
    ],
    16: [
        "Lantern, Trinket",
        "Spear (d8 B), Trinket",
        "Axe (d6), Trinket",
    ],
    17: [
        "Wine, Trinket",
        "Mallet (d6), Trinket",
        "Sling (d6), Trinket",
    ],
    18: [
        "Broken Nose, Trinket",
        "Hanging Jaw, Trinket",
        "Flat Head, Trinket",
    ],
}

trinkets_table = {
    1: "Fighting Rooster (2d6hp)",
    5: "Devil Mask",
    7: "Eternally Smelly Hat",
    9: "Horse Skull Helmet",
    11: "Donkey",
    13: "Bag of Flour",
    15: "Very Fat Dog",
    17: "Bell on a Stick",
    19: "Explorer's Sabre (d6)",
    22: "An Actual Rifle! (d8 B, no ammo)",
    24: "Potato Sack",
    26: "Wagon Wheel",
    29: "Dowsing Rods",
    33: "Scythe (d6 B)",
    37: "Cage Full of Crickets",
    39: "Unbreakable Conker",
    41: "Ornate Shovel (d6)",
    43: "Old Military Uniform",
    46: "Bag of Really Heavy Rocks",
    49: "Wooden Locket",
    53: "Brick on a Rope",
    56: "Cloth Monkey",
    59: "Huge Candle",
    62: "Bat on a String",
    65: "Lucky Frog",
    69: "Board with Nail (d6)",
    73: "Noose",
    77: "Fake Pistol",
    79: "Rude Shaped Turnip",
    82: "Cannonball",
    83: "Fire Oil",
    85: "Gigantic Pumpkin",
    87: "Bomb (no fuse)",
    89: "Turnip Wine",
    92: "Magic Beans (not magic)",
    95: "Prize Cow",
    97: "Small, Blind, Old Dog",
    99: "Pointy Star Hat",
    100: "Arcanum",
}


class SimpleFolkCharacter(Character):
    def __init__(self):
        super().__init__()
        self.STR = roll("1d12") + 6
        self.DEX = roll("1d12") + 6
        self.WIL = roll("2d6")
        self.starter_package = "Dagger, Torch, Quaint clothes, "
        index = ceil(self.HP / 2) - 1
        self.starter_package += simple_folk_starter_package_table.get(self.STR)[index]
        n_trinkets = self.starter_package.count("Trinket")
        rolled_trinkets = [
            get_closest_key(roll("1d100"), trinkets_table) for _ in range(n_trinkets)
        ]
        self.starter_package = self.starter_package.replace("Trinket", "") + ", ".join(
            rolled_trinkets
        )
        self.starter_package = self.starter_package.split(", ")


class Companion:
    def __init__(self):
        self.STR = roll("3D6")
        self.DEX = roll("3D6")
        self.WIL = roll("3D6")
        self.HP = 1
        self.gender = random.choice(("Male", "Female"))
        self.name = get_name(self.gender)
        WEAPON_CHOICES = ["Dagger", "Club", "Pistol", "Hammer", "Sword"]
        self.starter_package = f"{random.choice(WEAPON_CHOICES)} (d6)"

    def __repr__(self):
        return f"{self.name}\n{self.gender}\nHP: {self.HP}\nSTR: {self.STR}\nDEX: {self.DEX}\nWIL {self.WIL}\n{self.starter_package}"


class NPC:
    def __init__(self):
        manners = [
            "Attractive Dullard",
            "Big Fat Glutton",
            "Beaky Bore",
            "Creaky Elder",
            "Childlike",
            "Dashing Young Gun",
            "Ethereal Beauty",
            "Fails at Flirtatious",
            "Flamboyant Charmer",
            "Great Speaker",
            "Greasy Toad",
            "Gentle Giant",
            "Hulking Brute",
            "Hunchback",
            "Harmless Dope",
            "Intensely Creepy",
            "Ill-Coloured and Thin",
            "Jolly and Fat",
            "Loads of Jewellery",
            "Lots of Scars",
            "No Nose",
            "Nice but Dim",
            "Naive Teenager",
            "Old Sleaze",
            "Pig-Faced",
            "Plucky Little Thing",
            "Powdered Wig",
            "Quite Ugly",
            "Rough as a Dog",
            "Stocky Grunter",
            "Stunted Growth",
            "Straight-Laced",
            "Towering Klutz",
            "Unwashed Slob",
            "Vapid Fashionista",
            "Very Long Hair",
            "Well-Bred Snob",
            "Waif",
            "Weird Head",
        ]
        connections = [
            "Aunt/Uncle",
            "Sibling",
            "Best Friend",
            "Owes Money",
            "Old Friend",
            "Common ancestry",
            "Platonic Love",
            "Admiration",
            "Parent",
            "Owed Money",
            "Acquaintance",
            "Common Benefactor",
            "Hatred",
            "Irritation",
            "Twin",
            "Spouse",
            "Guardian",
            "Lover",
            "Mentor",
            "Abuser",
            "Lust",
            "Distaste",
            "House-Share",
            "Former Colleagues",
            "School Friends",
            "Adopted Parent",
            "Unrequited Love",
            "Planning Murder",
            "Knows Secret",
            "One Night Stand",
            "Rivals",
            "Backhand Deal",
            "Criminal Enterprise",
            "Shared Trauma",
            "Jealousy",
            "Violent Hate",
            "Engaged",
            "Protector",
            "Playful Rivalry",
        ]
        events = [
            "Arrested Wrongfully for Minor Crime",
            "Arrested Rightfully for Major Crime",
            "Became Addicted to an Exotic Drug",
            "Contracted a Terrible Disease",
            "Debt Collectors are Applying Pressure",
            "Died in an Uprising",
            "Died in Industrial Accident",
            "Found Long-Lost Relative",
            "Found (new) Love",
            "Found a Major Arcanum",
            "Found a Lesser Arcanum",
            "Getting (Re)Married",
            "Joined a Star Cult",
            "Joined a New Revolutionary Group",
            "House Collapsed",
            "Lost at Sea",
            "Lost Everything",
            "Lamp-Lighter Burnt Down House",
            "Left Bastion for the Deep Country",
            "Left Bastion for a Lesser City",
            "Murdered in the Street",
            "Murdered in their Bed",
            "Nice person has given them some juicy work",
            "Press-Ganged into Military",
            "Rumours of Criminal Activity",
            "Rumours of personal Depravity",
            "Saw weird things in the sky",
            "Saw horrible beasts in the street",
            "Saw a murder nearby",
            "Taken up Military Service",
            "Taken in an Orphan",
            "The Watch are harassing them",
            "Underground Weirdos Abducted Them",
            "Vanished in a Burst of Light",
            "Wandered into Underground, now missing",
            "Won a fortune by gambling",
            "Witnessed an Abduction into the night sky",
            "Went on a drinking binge",
            "Recklessly leapt into a Doomed Romance",
        ]
        occupations = [
            "Actor",
            "Barge Pilot",
            "Butler",
            "Coffee House Host",
            "Coal Miner",
            "Dog Breeder",
            "Engine Cleaner",
            "Fist Fighter",
            "Fishmonger",
            "Gull-Catcher",
            "Glue maker",
            "Gunsmith",
            "Gin-Maker",
            "Hog-Slaughterer",
            "Ivory Worker",
            "Jeweler",
            "Lower-Politician",
            "Life Servant",
            "Lamp-Lighter",
            "Lesser-Noble",
            "Mercenary",
            "Newspaper Vendor",
            "Octopus-Catcher",
            "Oyster Seller",
            "Perfumer",
            "Professor",
            "Prison Guard",
            "Pie-Smith",
            "Road Sweeper",
            "Salt Farmer",
            "Sweet-Maker",
            "Trinket-Merchant",
            "Tax Collector",
            "Tunnel Digger",
            "Whaler",
            "Watchmaker",
            "Watchman",
            "Writer",
            "Wigmaker",
        ]
        capabilities = [
            "Anal-Retentive",
            "Boringly Dependable",
            "Best in the City",
            "Cheap and Dirty",
            "Charming and Oily",
            "Dabbler",
            "Expensive and Flashy",
            "Fair and Down to Earth",
            "Filthy but very cheap",
            "Great, but hated for it",
            "Good but Annoying",
            "Highly Artistic",
            "Hardly trained",
            "Inherited Family Trade",
            "Interested in new career",
            "Imposter",
            "Jealous of Better Rival",
            "Learning, still.",
            "Loves the job",
            "Lazy and Greedy",
            "Money-Grabbing",
            "Moral, but not that good",
            "Only serves friends",
            "Old-Master-Trained",
            "Perfectionist",
            "Paragon of the Job",
            "Poor from bad business",
            "Retired from Injury",
            "Ruthless",
            "Sworn into Profession",
            "Silently dutiful",
            "Trained from Birth",
            "Trapped in Job",
            "Uncaring",
            "Unreliable Genius",
            "Wedded into Career",
            "Wasted Talent",
            "Warm and Friendly",
            "Wealthy with Success",
        ]

        self.manner = random.choice(manners)
        self.connection = random.choice(connections)
        self.occupation = random.choice(occupations)
        self.capability = random.choice(capabilities)
        self.event = random.choice(events)
        self.gender = random.choice(("Male", "Female"))
        self.name = get_name(self.gender)

    def __repr__(self):
        return f"{self.name}\n{self.gender}\nTheir manner: {self.manner}\nTheir connection to a PC: {self.connection}\nWhat happened to them? {self.event}"


class Street:
    def __init__(self):
        points_of_interest = [
            "Brewery",
            "Meeting Fountain",
            "Restaurant",
            "Sunken Pit",
            "Bar",
            "Fighting Den",
            "Castle",
            "City Wall",
            "Huge Factory",
            "Coal Heap",
            "Poorhouse",
            "Public Baths",
            "Observatory",
            "University",
            "Building Site",
            "Winding Alleyways",
            "Shop Row",
            "Residential Terrace",
            "Botanical Garden",
            "Cult Temple",
            "Docks",
            "Warehouses",
            "Underground Shelter",
            "School",
            "Ironworks",
            "Canal Dock",
            "Amusement Complex",
            "Specialist Shops",
            "Bridge",
            "Manor",
            "Guild House",
            "Army Barracks",
            "Shopping Arcade",
            "Watchtower",
            "City Watch Station",
            "Hospital",
            "Cult Cathedral",
            "Shrine",
        ]
        atmospheres = [
            "Welcoming",
            "Dark",
            "Smoggy",
            "Abandoned",
            "Bustling",
            "Brightly Lit",
            "Creepy",
            "Drafty",
            "Sinister",
            "Comforting",
            "Rat-Infested",
            "Expensive",
            "In Poverty",
            "Dusty",
            "Freshly Built",
            "Ruined",
            "Burnt",
            "On Fire!",
            "Overrun by Rioters",
            "Bird Infested",
            "Falling Down",
            "Ancient",
            "Artistic",
            "Eccentric",
            "Physics-Defying",
            "Underground",
            "Overgrown",
            "Hidden",
            "Criminal",
            "Council-Sanctioned",
            "Rebellious",
            "Protesting",
            "Cult-Linked",
            "Dangerous",
            "Filthy",
            "Overrun by Orphans",
            "Fearful",
            "Nonsensical",
        ]
        links = [
            "No",
            "Probably in the next road down",
            "No, and why are you so interested?",
            "No, we don't want Weirdos coming up",
            "No, it's too dangerous to leave them open",
            "Sure! Oh, wait, it's gone",
            "Yes, but the tunnels are too hot to survive",
            "No, soldiers came and sealed it up",
            "Yes, but it leads straight into an acid pool",
            "Nobody wants to talk about the Underground",
            "We dug this one quite recently",
            "An escape tunnel out of town",
            "Yeah, an old trapdoor",
            "A wine cellar leads somewhere horrible",
            "This tunnel goes right across town",
            "A particularly disgusting sewer",
            "An old bank vault",
            "Smugglers have set up tunnels around here",
            "They all got sealed up years ago",
            "There's a tunnel in plain sight",
            "Hidden stairway indoors",
            "A hole opened up last week",
            "Nasty things burst from the ground here",
            "An old vault entrance",
            "Emergency shelter nearby",
            "Just a chute straight down",
            "Spiral staircase ornately decorated",
            "An overgrown natural cave",
            "Tunnel at the bottom of a pond",
            "Open sewer",
            "An old well",
            "Rusty ladder down a chute",
            "It caved in recently",
            "An old elevator",
            "A newly fitted elevator",
            "The hole where they throw their rubbish",
            "Huge pit into the darkness",
            "Tunnel at the bottom of the river",
            "Natural cave in somebody's cellar",
        ]

        self.point_of_interest = random.choice(points_of_interest)
        self.atmosphere = random.choice(atmospheres)
        self.link = random.choice(links)

    def __repr__(self):
        return f"Street with a {self.point_of_interest} and a {self.atmosphere} atmosphere.\nLink to the underground: {self.link}"


class Council:
    def __init__(self):
        council_actions = [
            "All Arcana must be registered",
            "War with all other cities",
            "Major cult is outlawed",
            "Entire borough to be flattened",
            "Army conscription",
            "New council-sanctioned cult",
            "Animal census",
            "All prisoners to be executed",
            "All prisoners to be released",
            "Launching a cosmic rocket",
            "Double taxes",
            "Random mass eviction",
            "Total lockdown",
            "Inquisition into possible rebellion",
            "Entire council executed and replaced",
            "Exodus to the Golden Lands",
            "Underground crusade",
            "Guns outlawed",
            "Alcohol prohibited",
            "Martial law",
        ]
        public_reaction = [
            "“Riots!”",
            "“Tomorrow we launch an uprising!”",
            "“Someone should do something!”",
            "“Don’t care”",
            "“They probably have a good reason...”",
            "“Well it’s about time!”",
        ]

        self.action = random.choice(council_actions)
        self.public_reaction = random.choice(public_reaction)

    def __repr__(self):
        return f"The Council decided “{self.action}”.\nThe general public's reaction was {self.public_reaction}"


class Route:
    def __init__(self):
        routes = [
            "Crawl-Tunnel",
            "Funicular",
            "Horse Carriage",
            "Underground Carriageway",
            "Canal Boat",
            "Underground Canal",
            "Shady Alleyways",
            "Straight Through the Park",
            "Along the Docks",
            "Rooftop Walkway",
            "Down the High Street",
            "Through a Riot",
            "Underground Tramway",
            "Tunnel with Toll Booth",
            "Hired Carriage",
            "Through an Abandoned Warehouse",
            "Through a Working Factory",
            "Through the Slums",
            "Through the Rich Neighbourhoods",
            "Along the City Walls",
            "Steamboat Down the River",
            "Rickshaw",
            "Underground Tunnels",
            "Through the Market",
            "The Wine Cellar Network",
            "Catacombs",
            "Through the Old Town",
            "Urgh, Sewers",
            "Through the Bad End of Town",
            "Across University Campus",
            "Through the Botanical Gardens",
            "Along the Canals",
            "Over a Ruined Castle",
            "Through the Graveyard Quarter",
            "Up the Hill, then back down",
            "Right Through the Crazy Part of Town",
            "Through a Cult Temple",
            "Past the Army Barracks",
            "Through the Smuggler Tunnels",
        ]
        self.shortest = random.choice(routes)
        self.alternative = random.choice(routes)

    def __repr__(self):
        return f"The shortest route to that part of town is {self.shortest}\nAn alternative is {self.alternative}"


class Business:
    def __init__(self):
        businesses = [
            "Cage-Brand Steam Generators",
            "Pickem's Enterprise Loans",
            "Anise Sisters Security Wire",
            "Gasman Spice & Soap",
            "Prospective Telecoms",
            "The Lady's Sugar and Coffeehouse",
            "Yesser's Wool and Meat",
            "Secure Properties and Jails",
            "Consolidated Bookmakers",
            "Commercial Voice Printed Press",
            "Gallow, Sniff, & Pine Medical Research",
            "Claymore Bank & Private Military",
            "Broken Compass Offshore Acquisitions",
            "Baker Arms & Munitions",
            "Cohen Mass Nutrition Solutions",
            "Footman Stills Spirits & Tonics",
            "Braker's Streetlamp and Halberd",
            "Black Horse Hospitals and Asylums",
            "Bastio-Goldish Coal, Oil, and Ore",
            "Confectioner's Village Foods & Homes",
            "Red Ghost Roads & Carriages",
            "Freeman Brewers & Bakers",
            "Drake Ships & Sails",
            "Shooman Boots & Tonics",
            "Bates' Smoke Farms",
            "Great Underground Disposal Company",
            "Clock's Shippage & Canals",
            "Hightower Hats & Canes",
            "Territorial Tea & Wine",
            "Outlander's Exotic Down & Fur",
            "Furrupp's Brick & Mortar",
            "Bitter & Snatch Jewellery",
            "Werner's Industrial Machinery",
            "Silvermountain Private Security",
            "Aria Mines",
            "Miracle Factory Ice & Salt",
            "Metropolitan Tramway",
            "Sunfair Gold Holdings",
        ]
        self.name = random.choice(businesses)

    def __repr__(self):
        return self.name


class WeirdCreature:
    def __init__(self):
        natures = [
            "Solid-Smoke",
            "Skeletal",
            "Decaying",
            "Luxurious",
            "Bio-Machine",
            "Living Construct",
            "Reptilian",
            "Slime Covered",
            "Glassy",
            "Liquid Metal",
            "Ceramic",
            "Living Rock",
            "Scabs and Sores",
            "Hyper-Robotic",
            "Spiny",
            "Stinking Filth",
            "Shadow-Cloaked",
            "Eerily Beautiful",
            "Mechanical Suit",
            "Sapient and Armoured",
            "Baroque Excess",
            "Leathery",
            "Feathered",
            "Pale and Bald",
            "Ghostly",
            "Holographic",
            "Hardlight",
            "Acid Dripping",
            "Shaggy Hair",
            "Mirrored Metal",
            "Damp Clay",
            "Colossal",
            "Bare Musculature",
            "All-Brain",
            "Plasmic",
            "Chitin",
            "Rusted Shell",
            "Bionic Parts",
        ]
        forms = [
            "Cube",
            "Tripod",
            "Swarm",
            "Disembodied Hand",
            "Worm",
            "Sphere",
            "Hound",
            "Great Cat",
            "Snake",
            "Crustacean",
            "Squat Biped",
            "Slender Biped",
            "Insect",
            "Obese Biped",
            "Towering Biped",
            "Baby Bird",
            "Slug",
            "Snail",
            "Hawk",
            "Terror-Bird",
            "Bull",
            "Shark",
            "Spider",
            "Blob",
            "Spiral",
            "Pyramid",
            "Sheet",
            "Wasp",
            "Maggot",
            "Tadpole",
            "Jellyfish",
            "Bat",
            "Octopus",
            "Pike",
            "Sea Urchin",
            "Cannon",
            "Fly",
            "Fetal",
        ]
        twists = [
            "Mastery of Magnetism",
            "Grasps with Extra Limbs",
            "Phases Through Matter",
            "Chimera (roll additional Form)",
            "Reads Minds",
            "Colossal Size",
            "Drains Life",
            "Sprays Acid",
            "Creates Black-Holes",
            "Teleports Self",
            "Teleports Others",
            "Shifts Shape",
            "Breathes Smoke",
            "Creates Electric Charge",
            "Sees Future",
            "Controls Others",
            "Cloaking Device",
            "Conjures Illusions",
            "Infects with Disease",
            "Kills with Venom",
            "Hunts Arcana",
            "Fires Bullets",
            "Freeze Matter",
            "Heat/Melt Matter",
            "Implants with Egg/Parasite",
            "Paralyzes with Touch",
            "Fires Death Rays",
            "Manipulates Living Tissue Telekinetically",
            "Manipulates Objects Telekinetically",
            "Sees Distant Places",
            "Regenerates from any harm",
            "Reflects harm onto attacker",
            "Absorbs victims into Body",
            "Turns victims into non-living matter",
            "Launch explosives",
            "Cause intense pain at touch",
            "Heal any harm with a touch",
            "Sense distant objects",
        ]
        self.nature = random.choice(natures)
        self.form = random.choice(forms)
        self.twist = random.choice(twists)

    def __str__(self):
        return f"{self.nature} {self.form} but it {self.twist.lower()}"


class AstralCult:
    def __init__(self):
        collectives = [
            "Library",
            "Children",
            "Fortress",
            "Heralds",
            "Keepers",
            "Temple",
            "Betrayers",
            "Hunters",
            "Union",
            "School",
            "Seekers",
            "Knights",
            "Order",
            "Drinkers",
            "Choir",
            "Sons",
            "Daughters",
            "Servants",
            "Society",
            "Army",
            "Wanderers",
            "Pilgrims",
            "Contemplators",
            "Movement",
            "Preachers",
            "Revolution",
            "Mercy-Givers",
            "Council",
            "Tower",
            "Worshipers",
            "Observers",
            "Beggars",
            "Witnesses",
            "Centre",
            "Garrison",
            "Engineers",
            "Family",
            "Chanters",
        ]
        descriptions = [
            "Devouring",
            "Kindly",
            "Dreaming",
            "Infinite",
            "Glowing",
            "Dead",
            "Rotting",
            "Raging",
            "Golden",
            "Unborn",
            "Blessed",
            "Chained",
            "Sunken",
            "Broken",
            "Stirring",
            "Newborn",
            "Golden",
            "Bloodied",
            "Half",
            "Forgotten",
            "Underground",
            "Twisted",
            "Glorious",
            "Vengeful",
            "Laughing",
            "Elder",
            "Loving",
            "Undefeatable",
            "Timeless",
            "Striking",
            "Roaring",
            "Inevitable",
            "Bright",
            "Jade",
            "Iron",
            "Bone",
            "Silent",
            "Pure",
        ]
        symbols = [
            "Sword",
            "Snake",
            "Child",
            "Egg",
            "Cloud",
            "Light",
            "Star",
            "Father",
            "Maw",
            "Song",
            "Colour",
            "Gate",
            "Ship",
            "Death",
            "Sea",
            "Shadow",
            "Giants",
            "General",
            "Truth",
            "Lie",
            "King",
            "Queen",
            "Force",
            "Swarm",
            "Fleet",
            "Horror",
            "Beauty",
            "Spire",
            "Crystals",
            "Pantheon",
            "Throne",
            "Web",
            "Eye",
            "Hand",
            "Shield",
            "Skull",
            "Weed",
            "Mist",
        ]
        standings = [
            "Hated",
            "Hidden",
            "Disgraced",
            "Bankrupt",
            "Disgusting",
            "Outlawed",
            "Enemies of another Cult",
            "Tiny",
            "Weak",
            "Fake",
            "Forgotten",
            "Nobody Cares",
            "Mocked",
            "Discouraged",
            "Hunted",
            "Weakened",
            "Underground",
            "Unknown",
            "Hardly Known",
            "Feared",
            "Taboo",
            "Too Old to Criticise",
            "Too Big to Fail",
            "Somewhat Liked",
            "Charitable",
            "Tolerated",
            "Wealthy",
            "Sprawling",
            "Allies of another Cult",
            "Respected",
            "Front for a Business",
            "Actively Recruiting",
            "Fashionable",
            "Strong",
            "Powerful",
            "Legendary",
            "Beloved",
            "Council-Sanctioned",
        ]

        self.collective = random.choice(collectives)
        self.description = random.choice(descriptions)
        self.symbol = random.choice(symbols)
        self.standing = random.choice(standings)

    def __repr__(self):
        return f"{self.description} cult of {self.collective}. Their symbol is a {self.symbol}. They are {self.standing}"


class Beyond:
    def __init__(self):
        features = [
            "Weird Generator",
            "Corpse Pit",
            "Abyssal Chasm",
            "Labyrinth",
            "Murder Shrine",
            "Flowing Filth",
            "Sealed Vault",
            "Bunker",
            "Dirt Hole",
            "Crumbling Chapel",
            "Art Gallery",
            "Forge",
            "Office",
            "Torture Chamber",
            "Feast Hall",
            "Military Tomb",
            "Ancient Barrow",
            "Cult Catacomb",
            "Fighting Pit",
            "Well",
            "Drinking Hole",
            "Crystal Cave",
            "Prison",
            "Natural Spring",
            "Open Vault",
            "Flooded Sewer",
            "Abandoned Tramway",
            "Gun Workshop",
            "Gunpowder Store",
            "Dog Pit",
            "Alchemy Lab",
            "Printing Press",
            "Metal Sphere",
            "Underground Lake",
            "Throne Room",
            "Armoury",
            "Swimming Pool",
            "Observatory",
        ]
        hazards = [
            "Bell Alarm",
            "Searing Hot Walls",
            "Glass Snakes",
            "Crawling Eyes",
            "Acid Puddles",
            "Tunnel Shark",
            "Crushing Walls",
            "Taunting Voices",
            "Hidden Spikes",
            "Slime Drones",
            "Carnivorous Birds",
            "Insane Babbling",
            "Insane Soldier",
            "Deafening Siren",
            "Devouring Maw",
            "Grasping Tentacles",
            "Questioning Brain",
            "Huge Beast",
            "Collapsing Floor",
            "Shifting Illusions",
            "Stone Automatons",
            "Incineration Pit",
            "Living Chains",
            "Cursing Hag",
            "Frightened Cat",
            "Holographic Spiders",
            "Gusts of Wind",
            "Ghostly Hands",
            "Dust Tornadoes",
            "Acidic Ooze",
            "Freeze-Rays",
            "Shifting Blocks",
            "All-Seeing Eye",
            "Mechanical Judge",
            "Angry Mutants",
            "Rival Explorers",
            "Impenetrable Shadow",
            "Blinding Lights",
        ]
        spoils = [
            "Gilded Throne (30G)",
            "Locked Chest (10G)",
            "Glowing Rod (inanimate, 10S)",
            "d6 Crocodile Eggs",
            "Diamond Ring (2S)",
            "Looking Glass",
            "Town Crier Bell",
            "Unnaturally Bright Lantern",
            "Opal Brooch (2S)",
            "Black Gem (1G)",
            "Telescope",
            "Sack of Coal",
            "Symbolic Dagger",
            "Astral Pistol",
            "Musket",
            "Wicker Ball",
            "Hammers and other Tools",
            "Feathered Headband",
            "Leather Bracers (falling apart)",
            "Flute (silver, 50S)",
            "Huge Drum",
            "Blood Soaked Rags",
            "Hand Mirror",
            "Audacious Painting",
            "Metal Staff",
            "Set of Modern Armour",
            "Modern Armour",
            "Crude Armour",
            "White Boulder",
            "Drinking Horn",
            "Beast Tusk (50S)",
            "Glowing Sword (ignores Armour)",
            "Stone Tablet (gibberish)",
            "Engine Parts",
            "Anvil",
            "Dice (twelve-sided)",
            "Glass Chains (oddly warm)",
            "Cannon (in need of repair)",
            "Dead Dog",
        ]
        self.feature = random.choice(features)
        self.hazard = random.choice(hazards)
        self.spoil = random.choice(spoils)

    def __repr__(self):
        return f"{self.feature}\nHazard: {self.hazard}\nSpoil: {self.spoil}"


class Island:
    def __init__(self):
        landmarks = [
            "Smoking Volcano",
            "Huge Waterfall",
            "Ice-Capped Peak",
            "Glittering Lake",
            "Colourful Lights",
            "Red Forests",
            "Black Sands",
            "Rock Fortress",
            "Abandoned Fleet",
            "Salt Beach",
            "Crystal Shards",
            "Absolutely Flat",
            "Thorny Jungle",
            "Ice All Over",
            "Blasted Waste",
            "Long and Thin",
            "Creeping Moss",
            "Steel Spires",
            "Blooded Bushes",
            "Spiral Mountain",
            "Hot and Dry",
            "Misty",
            "Grand Canyon",
            "Delicious Fruit",
            "Ruined Temple",
            "High Walls",
            "Glass Towers",
            "Lone Mountain",
            "Blue Grass",
            "Yellow Rock",
            "Piles of Skulls",
            "Oversized Fungus",
            "Dense Cacti",
            "Choking Fog",
            "Gusts of Wind",
            "Tiny Trees",
            "Elephant Herds",
            "Underwater",
        ]
        twists = [
            "Island is Intelligent",
            "Sweltering Heat",
            "Covered by Metal Dome",
            "Nobody Can Die Here",
            "Sinking",
            "Recently Resurfaced",
            "Toxic Air",
            "Utterly Silent",
            "Plants Grow Visibly",
            "Eternal Night",
            "Completely Abandoned",
            "Expedition Gone Native",
            "Giant Killer Frogs",
            "Whispering Wind",
            "Monkeys with Guns",
            "Shipwrecked Explorers",
            "Metal Skeletons",
            "Sand Wraiths",
            "Huge Spiders",
            "Harmless, Cute Piggies",
            "Advanced Fish-People",
            "Terrible Lizard Eggs",
            "Silver Statues",
            "Meteor Armour",
            "Doomsday Device",
            "Time Machine",
            "Crashed Sky-Boat",
            "New Energy Source",
            "Font of Immortality",
            "Ghost Army",
            "Ruby-Growing Tree",
            "Astral Vessel",
            "Island is Giant Turtle",
            "It's Always Growing",
            "It's all a Hologram",
            "No Time Passes Here",
            "Steel Dinosaurs",
            "Slime Volcano",
        ]
        self.landmark = random.choice(landmarks)
        self.twist = random.choice(twists)

    def __repr__(self):
        return f"{self.landmark} but {self.twist}"


def eat_the_stuff():
    outcomes = [
        "Delici...argh! STR Save or your guts explode.",
        "Delicious! Fruity. Quite satisfying.",
        "Tastes meaty. You regain any lost STR.",
        "Your insides feel cold, and liquid metal coats your bones. You always have Armour 1.",
        "Tastes pickled. You get real drunk.",
        "Woah. Hallucinations for d6 hours.",
        "Blech! Vomit now and for d6 hours.",
        "Tastes inky. You can read books instantly by waving your hand over them.",
        "Urgh... so salty. It's gross.",
        "Literally liquid gold. Lose d6 STR.",
        "Hot! Breathe Fire (d10) at whoever is right in front of you.",
        "Roll a Mutation (see p137).",
        "Turn Invisible for d6 minutes.",
        "Horrible pain for d6 minutes.",
        "Bready. You need never eat or drink again.",
        "Like liquid fish. Quite stirring.",
        "Blind for d6 hours!",
        "Awful poison. Lose 2d6 STR.",
        "Lose 2d6 DEX. Turn to stone at DEX 0.",
        "Lose 2d6 WIL. Turn into an insane monster at WIL 0.",
        "It's okay I guess, for slime.",
        "Gain an evil voice in your head forever.",
        "Gain a helpful voice in your head forever.",
        "It's the best! You crave more.\nLose 1 WIL each day until you eat some more.",
        "Invigorating! Gain 1d6 STR for d6 hours.",
        "Mind-Opening. Gain 1d6 WIL for d6 hours.",
        "Zippy! Move at double pace for d6 hours.",
        "First taste is gross. Second is delicious.",
        "Your mouth seals shut for d6 hours.",
        "Go on a rampage for d6 turns.",
        "Your voice now echoes.",
        "Your voice is permanently higher pitched.",
        "Rapid hair growth, permanently.",
        "Like Honey! Heals any ailment.",
    ]
    return random.choice(outcomes)


class Thing:
    def __init__(self):
        forms = [
            "Throne",
            "Chest",
            "Rod",
            "Wand",
            "Ring",
            "Cube",
            "Bell",
            "Lantern",
            "Brooch",
            "Gem",
            "Telescope",
            "Lens",
            "Dagger",
            "Pistol",
            "Musket",
            "Sphere",
            "Hammer",
            "Headband",
            "Bracers",
            "Flute",
            "Drum",
            "Huge Machine",
            "Mirror",
            "Painting",
            "Staff",
            "Helmet",
            "Breastplate",
            "Rock",
            "Boulder",
            "Horn",
            "Tusk",
            "Sword",
            "Tablet",
            "Engine",
            "Anvil",
            "Dice",
            "Chains",
            "Cannon",
        ]

        arcana = [
            "Nope!",
            "No, but valuable!",
            "Just weird.",
            "Just bait for a trap.",
            "No but still deadly.",
            "The thing itself is a trap!",
            "Actually really boring.",
            "No, but some value.",
            "Yes! Wait... no.",
            "Quite techy, but no.",
            "Obviously not.",
            "Find an expert and roll again!",
            "No.",
            "Otherworldly, but no.",
            "A fake.",
            "Just arty.",
            "Just incredibly old.",
            "Yes! But it's trapped.",
            "Absolutely.",
            "Sure, but it's really ugly.",
            "Yeah, but it smells so bad.",
            "Sure is!",
            "Yes, and valuable anyway!",
            "Unsettling, but yes.",
            "Yes, but caked in dust.",
            "Sure, but not working now.",
            "It might be... it is!",
            "Yes, and you've heard of it.",
            "Yes! Just like in the story!",
            "Yes, and safe to use too.",
            "Very much so.",
            "Yep!",
            "Obviously.",
            "Sure, but looks so dangerous.",
            "Yes!",
            "Yes, but needs attention.",
            "Yes, but not obviously.",
            "No... wait! No.. WAIT! YES!",
        ]

        powers = [
            "Cosmic Travel",
            "Time Distortion",
            "Cosmic Summoning",
            "Astral-Transcendence",
            "Telekinesis",
            "Elemental Blast",
            "Slow Painful Death",
            "Disintegration",
            "Flight",
            "Size Distortion",
            "Plant Control",
            "Mass-Creation",
            "Energy-Creation",
            "Thing go BOOM!",
            "Unlock Primal Rage",
            "Persuasion",
            "Auditory Illusions",
            "Visual Illusions",
            "Liquify Matter",
            "Blast Minds",
            "Read Thoughts",
            "Create Deadly Traps",
            "Summon the Dead",
            "Hypnotic Music",
            "Dull Senses",
            "Venom Ray",
            "Great Knowledge",
            "Communicate Great Distances",
            "Arm the Masses",
            "Destroy Structures",
            "Unnatural Slumber",
            "Spread Insanity",
            "Possession",
            "Create Servants",
            "Release Unstoppable Creature",
            "Release Benevolent Spirit",
            "Swap Materials",
            "Sensory Overload",
        ]

        self.form = random.choice(forms)
        self.arcanum = random.choice(arcana)
        self.power = random.choice(powers)

    def __repr__(self):
        return f"{self.form} {self.arcanum} {self.power}"
