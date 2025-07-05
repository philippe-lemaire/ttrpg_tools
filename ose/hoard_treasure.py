import random
import re

# Type A (18,000gp average)
type_a = (
    ("25%", "1d6 × 1,000 cp."),
    ("30%", "1d6 × 1,000 sp."),
    ("20%", "1d4 × 1,000 ep."),
    ("35%", "2d6 × 1,000 gp."),
    ("25%", "1d2 × 1,000 pp."),
    ("50%", "6d6 gems."),
    ("50%", "6d6 pieces of jewellery."),
    ("30%", "3 magic items."),
)

# Type B (2,000gp average)
type_b = (
    ("50%", "1d8 × 1,000 cp."),
    ("25%", "1d6 × 1,000 sp."),
    ("25%", "1d4 × 1,000 ep."),
    ("25%", "1d3 × 1,000 gp."),
    ("25%", "1d6 gems."),
    ("25%", "1d6 pieces of jewellery."),
    ("10%", "1 magic sword, suit of armour, or weapon."),
)

# Type C (1,000gp average)
type_c = (
    ("20%", "1d12 × 1,000 cp"),
    ("30%", "1d4 × 1,000 sp."),
    ("10%", "1d4 × 1,000 ep."),
    ("25%", "1d4 gems."),
    ("25%", "1d4 pieces of jewellery."),
    ("10%", "2 magic items."),
)

# Type D (3,900gp average)
type_d = (
    ("10%", "1d8 × 1,000 cp."),
    ("15%", "1d12 × 1,000 sp."),
    ("60%", "1d6 × 1,000 gp."),
    ("30%", "1d8 gems."),
    ("30%", "1d8 pieces of jewellery."),
    ("15%", "2 magic items plus 1 potion."),
)

# Type E (2,300gp average)
type_e = (
    ("5%:", "1d10 × 1,000 cp."),
    ("30%", "1d12 × 1,000 sp."),
    ("25%", "1d4 × 1,000 ep."),
    ("25%", "1d8 × 1,000 gp."),
    ("10%", "1d10 gems."),
    ("10%", "1d10 pieces of jewellery."),
    ("25%", "3 magic items plus 1 scroll."),
)

# Type F (7,700gp average)
type_f = (
    ("10%", "2d10 × 1,000 sp."),
    ("20%", "1d8 × 1,000 ep."),
    ("45%", "1d12 × 1,000 gp."),
    ("30%", "1d3 × 1,000 pp."),
    ("20%", "2d12 gems."),
    ("10%", "1d12 pieces of jewellery."),
    ("30%", "3 magic items (not weapons), plus 1 potion, plus 1 scroll."),
)

# Type G (23,000gp average)
type_g = (
    ("50%", "1d4 × 10,000 gp."),
    ("50%", "1d6 × 1,000 pp."),
    ("25%", "3d6 gems."),
    ("25%", "1d10 pieces of jewellery."),
    ("35%", "4 magic items plus 1 scroll."),
)

# Type H (60,000gp average)
type_h = (
    ("25%", "3d8 × 1,000 cp."),
    ("50%", "1d100 × 1,000 sp."),
    ("50%", "1d4 × 10,000 ep."),
    ("50%", "1d6 × 10,000 gp."),
    ("25%", "5d4 × 1,000 pp."),
    ("50%", "1d100 gems."),
    ("50%", "1d4 × 10 pieces of jewellery."),
    ("15%", "4 magic items, plus 1 potion, plus 1 scroll."),
)

# Type I (11,000gp average)
type_i = (
    ("30%", "1d8 × 1,000 pp."),
    ("50%", "2d6 gems."),
    ("50%", "2d6 pieces of jewellery."),
    ("15%", "1 magic item."),
)

# Type J (25gp average)
type_j = (
    ("25%", "1d4 × 1,000 cp."),
    ("10%", "1d3 × 1,000 sp."),
)

# Type K (180gp average)
type_k = (
    ("30%", "1d6 × 1,000 sp."),
    ("10%", "1d2 × 1,000 ep."),
)


# Type L (240gp average)
type_l = (("50%", "1d4 gems."),)

# Type M (50,000gp average)
type_m = (
    ("40%", "2d4 × 1,000 gp."),
    ("50%", "5d6 × 1,000 pp."),
    ("55%", "5d4 gems."),
    ("45%", "2d6 pieces of jewellery."),
)

# Type N (0gp average)
type_n = (("40%", "2d4 potions."),)

# Type O (0gp average)
type_o = (("50%", "1d4 scrolls."),)

# type p Type P (0.1gp average)
type_p = (("100%", "3d8 cp."),)

# Type Q (1gp average)

type_q = (("100%", "3d6 sp."),)


# Type R (3gp average)
type_r = (("100%", "2d6 ep."),)


# Type S (5gp average)
type_s = (("100%", "2d4 gp."),)

# Type T (17gp average)
type_t = (("100%", "1d6 pp."),)

# Group Treasure: U–V
"""Intelligent monsters: The group carries
this much treasure between them.
Unintelligent monsters: The treasure is
from the bodies of the monsters’ victims."""

# Type U (160gp average)
type_u = (
    ("10%", "1d100 cp."),
    ("10%", "1d100 sp."),
    ("5%", "1d100 gp."),
    ("5%", "1d4 gems."),
    ("5%", "1d4 pieces of jewellery."),
    ("2%", "1 magic item."),
)


# Type V (330gp average)
type_v = (
    ("10%", "1d100 sp."),
    ("5%", "1d100 ep."),
    ("10%", "1d100 gp."),
    ("5%", " 1d100 pp."),
    ("10%", "1d4 gems."),
    ("10%", "1d4 pieces of jewellery."),
    ("5%", "1 magic item."),
)

types = {
    "A": type_a,
    "B": type_b,
    "C": type_c,
    "D": type_d,
    "E": type_e,
    "F": type_f,
    "G": type_g,
    "H": type_h,
    "I": type_i,
    "J": type_j,
    "K": type_k,
    "L": type_l,
    "I": type_i,
    "J": type_j,
    "K": type_k,
    "L": type_l,
    "M": type_m,
    "N": type_n,
    "O": type_o,
    "P": type_p,
    "Q": type_q,
    "R": type_r,
    "S": type_s,
    "T": type_t,
    "U": type_u,
    "V": type_v,
}


def roll_percent(s):
    if s.endswith("%"):
        chance = int(s[:-1])
        roll = random.randint(1, 100)
        return roll <= chance

    return False


def roll(dice):
    """rolls ndx, where n is the number of dice (can be omitted) and x is the largest value on each die"""
    qty, size = dice.split("d")
    qty = int(qty) if qty else 1
    size = int(size)

    return sum([random.randint(1, size) for die in range(qty)])


def roll_hoard(type_):
    if types.get(type_):
        result = [t[1] for t in types.get(type_) if roll_percent(t[0])]
        if result:
            return result

    return ["Nothing"]


def get_closest_key(n, d):
    for key in d.keys():
        if key >= n:
            return d[key]
    return None


def roll_gems(s):
    values = {4: "10 gp", 9: "50 gp", 15: "100 gp", 19: "500 gp", 20: "1000 gp"}
    total = 0
    gems = []
    n, _ = s.split()
    for gem in range(int(n)):
        roll = random.randint(1, 20)
        value = get_closest_key(roll, values)
        amount, _ = value.split()
        total += int(amount)

        gems.append(f"1 gem worth {value}")

    gems_set = set(gems)
    cleaned_gems = []
    for item in gems_set:
        n = gems.count(item)
        cleaned_gems.append(f"{n} {item[2:]}")
    cleaned_gems.append(f"For a total value of {total} gp")
    cleaned_gems.insert(0, "Gems")
    return cleaned_gems


def roll_jewellery(s):
    n, *rest = s.split()
    n = int(n)

    total = 0
    jewels = []

    for piece in range(n):
        value = roll("3d6") * 100
        total += value
        jewels.append(f"1 piece of jewellery worth {value} gp.")

    jewel_sets = set(jewels)
    cleaned_jewels = []
    for item in jewel_sets:
        n = jewels.count(item)
        cleaned_jewels.append(f"{n} {item[2:]}")
    cleaned_jewels.append(f"For a total value of {total} gp")
    cleaned_jewels.insert(0, "Jewels")
    return cleaned_jewels


def roll_magic_item_type(level):
    if level <= 3:
        party_type = "basic"
    else:
        party_type = "expert"
    type_tables = {
        "basic": {
            10: "Armour or Shield",
            15: "Misc. Item",
            40: "Potion",
            45: "Ring",
            50: "Rod / Staff / Wand",
            70: "Scroll or Map",
            90: "Sword",
            100: "Weapon",
        },
        "expert": {
            10: "Armour or Shield",
            15: "Misc. Item",
            35: "Potion",
            40: "Ring",
            45: "Rod / Staff / Wand",
            75: "Scroll or Map",
            95: "Sword",
            100: "Weapon",
        },
    }
    roll = random.randint(1, 100)
    print(roll)
    return get_closest_key(roll, type_tables.get(party_type))


## armours and shields
def roll_armour_and_shield():
    armours_and_shields_table = {
        15: "Armour +1",
        25: "Armour +1, Shield +1",
        27: "Armour +1, Shield +2",
        28: "Armour +1, Shield +3",
        33: "Armour +2",
        36: "Armour +2, Shield +1",
        41: "Armour +2, Shield +2",
        42: "Armour +2, Shield +3",
        45: "Armour +3",
        46: "Armour +3, Shield +1",
        47: "Armour +3, Shield +2",
        48: "Armour +3, Shield +3",
        51: "Cursed Armour –1",
        53: "Cursed Armour –2",
        54: "Cursed Armour –2, Shield +1",
        56: "Cursed Armour, AC 9 [10]",
        62: "Cursed Shield –2",
        65: "Cursed Shield, AC 9 [10]",
        85: "Shield +1",
        95: "Shield +2",
        100: "Shield +3",
    }
    armour_types = {
        2: "Leather",
        6: "Chainmail",
        8: "Plate mail",
    }
    roll = random.randint(1, 100)
    raw_result = get_closest_key(roll, armours_and_shields_table)
    roll_armour_type = random.randint(1, 8)
    armour_type = get_closest_key(roll_armour_type, armour_types)
    result = raw_result.replace("Armour", f"{armour_type} Armour")
    return result


def roll_misc_item():
    table_1 = {
        2: "Alchemist's Beaker",
        3: "Amulet of Prot. Against Possession",
        6: "Amulet of Prot. Against Scrying",
        8: "Apparatus of the Crab",
        11: "Arrow of Location",
        12: "Bag of Devouring",
        17: "Bag of Holding",
        18: "Bag of Transformation",
        19: "Book of Foul Corruption",
        20: "Book of Infinite Spells",
        21: "Book of Sublime Holiness",
        22: "Boots of Dancing",
        27: "Boots of Levitation",
        31: "Boots of Speed",
        35: "Boots of Travelling and Leaping",
        50: "Bracers of Armour",
        52: "Bracers of Defencelessness",
        59: "Brooch of Shielding",
        64: "Broom of Flying",
        70: "Candle of Invocation",
        72: "Chime of Opening",
        73: "Chime of Ravening",
        85: "Cloak of Defence",
        95: "Cloak of Flight",
        97: "Cloak of Poison",
        100: "Cloak of the Manta Ray",
    }
    table_2 = {
        5: "Crystal Ball",
        7: "Crystal Ball with Clairaudience",
        8: "Crystal Ball with ESP",
        9: "Crystal Hypnosis Ball",
        11: "Cube of Force",
        13: "Cube of Frost Resistance",
        16: "Decanter of Endless Water",
        20: "Deck of Many Things",
        24: "Displacer Cloak",
        26: "Drums of Panic",
        27: "Drums of Thunder",
        33: "Dust of Appearance",
        39: "Dust of Disappearance",
        40: "Dust of Sneezing and Choking",
        41: "Efreeti Bottle",
        43: "Elem. Summoning Device: Air",
        45: "Elem. Summoning Device: Earth",
        47: "Elem. Summoning Device: Fire",
        49: "Elem. Summoning Device: Water",
        59: "Elven Cloak and Boots",
        60: "Eyes of Charming",
        62: "Eyes of Minuscule Sight",
        63: "Eyes of Petrification",
        65: "Eyes of the Eagle",
        80: "Feather Token",
        95: "Figurine of Wondrous Power",
        97: "Flying Carpet",
        98: "Folding Boat",
        100: "Gauntlets of Ogre Power",
    }
    table_3 = {
        1: "Gem of Brightness",
        2: "Gem of Monster Attraction",
        3: "Gem of Pristine Faceting",
        4: "Gem of Seeing",
        5: "Girdle of Giant Strength",
        7: "Gloves of Dexterity",
        10: "Gloves of Swimming and Climbing",
        12: "Helm of Alignment Changing",
        17: "Helm of Read Languages and Magic",
        19: "Helm of Telepathy",
        20: "Helm of Teleportation",
        21: "Horn of Blasting",
        22: "Horn of Cave-Ins",
        24: "Horn of Frothing",
        28: "Horn of the Tritons",
        35: "Horn of Valhalla",
        37: "Horseshoes of a Zephyr",
        40: "Horseshoes of Speed",
        45: "Incense of Meditation",
        46: "Incense of Obsession",
        48: "Instant Fortress",
        49: "Ioun Stones",
        51: "Iron Flask",
        53: "Jug of Endless Liquids",
        54: "Libram of Arcane Power",
        56: "Loadstone",
        58: "Luckstone",
        59: "Lyre of Building",
        61: "Marvellous Pigments",
        64: "Medallion of ESP 30’",
        66: "Medallion of ESP 90’",
        68: "Medallion of Thought Projection",
        69: "Mirror of Life Trapping",
        70: "Mirror of Mental Prowess",
        71: "Mirror of Opposition",
        74: "Necklace of Adaptation",
        78: "Necklace of Fireballs",
        80: "Necklace of Strangulation",
        84: "Net of Aquatic Snaring",
        87: "Net of Snaring",
        90: "Oil of Insubstantiality",
        93: "Oil of Slipperiness",
        95: "Pearl of Power",
        97: "Pearl of Wisdom",
        100: "Periapt of Foul Rotting",
    }
    table_4 = {
        2: "Periapt of Health",
        9: "Periapt of Proof Against Poison",
        13: "Periapt of Wound Closure",
        15: "Phylactery of Betrayal",
        21: "Phylactery of Faithfulness",
        25: "Phylactery of Longevity",
        33: "Pipes of the Sewers",
        34: "Portable Hole",
        36: "Purse of Plentiful Coin",
        44: "Restorative Ointment",
        51: "Robe of Blending",
        52: "Robe of Eyes",
        53: "Robe of Powerlessness",
        54: "Robe of Scintillating Colours",
        55: "Robe of the Archmagi",
        63: "Robe of Useful Items",
        69: "Rope of Climbing",
        73: "Rope of Entanglement",
        75: "Rope of Strangulation",
        76: "Rug of Suffocation",
        77: "Saw of Felling",
        79: "Scarab of Chaos",
        80: "Scarab of Death",
        86: "Scarab of Protection",
        89: "Scarab of Rage",
        90: "Spade of Mighty Digging",
        91: "Sphere of Annihilation",
        94: "Sweet Water",
        95: "Talisman of the Sphere",
        97: "Vacuous Grimoire",
        100: "Well of Many Worlds",
    }

    tables = (
        table_1,
        table_2,
        table_3,
        table_4,
    )

    table = random.choice(tables)
    roll = random.randint(1, 100)
    return get_closest_key(roll, table)


def roll_potion():
    potion_table = {
        3: "Clairaudience",
        7: "Clairvoyance",
        10: "Control Animal",
        13: "Control Dragon",
        16: "Control Giant",
        19: "Control Human",
        22: "Control Plant",
        25: "Control Undead",
        32: "Delusion",
        35: "Diminution",
        39: "ESP",
        43: "Fire Resistance",
        47: "Flying",
        51: "Gaseous Form",
        55: "Giant Strength",
        59: "Growth",
        63: "Healing",
        68: "Heroism",
        72: "Invisibility",
        76: "Invulnerability",
        80: "Levitation",
        84: "Longevity",
        86: "Poison",
        89: "Polymorph Self",
        97: "Speed",
        100: "Treasure Finding",
    }
    rolled = random.randint(1, 100)
    potion_effect = get_closest_key(rolled, potion_table)
    return f"Potion of {potion_effect}"


def roll_ring():
    rings_table = {
        5: "Control Animals",
        10: "Control Humans",
        16: "Control Plants",
        26: "Delusion",
        29: "Djinni Summoning",
        39: "Fire Resistance",
        50: "Invisibility",
        55: "Protection +1, 5’ radius",
        70: "Protection +1",
        72: "Regeneration",
        74: "Spell Storing",
        80: "Spell Turning",
        82: "Telekinesis",
        88: "Water Walking",
        94: "Weakness",
        96: "Wishes, 1–2",
        97: "Wishes, 1–3",
        98: "Wishes, 2–4",
        100: "X-Ray Vision",
    }
    rolled = random.randint(1, 100)
    result = get_closest_key(rolled, rings_table)

    if "Wishes" in result:
        mini, maxi = result.split("–")
        mini = mini[-1]
        n = random.randint(int(mini), int(maxi))
        result = f"Wishes, {n}"
    return f"Ring of {result}"


def roll_rod_staff_wand():
    rods_staves_wands_table = {
        2: "Immovable Rod",
        5: "Rod of Absorption",
        11: "Rod of Cancellation",
        12: "Rod of Captivation",
        14: "Rod of Lordly Might",
        15: "Rod of Parrying",
        16: "Rod of Resurrection",
        17: "Rod of Striking",
        18: "Staff of Commanding",
        20: "Staff of Dispelling",
        26: "Staff of Healing",
        27: "Staff of Power",
        30: "Staff of Snakes",
        33: "Staff of Striking",
        36: "Staff of Swarming Insects",
        38: "Staff of the Healer",
        40: "Staff of Withering",
        41: "Staff of Wizardry",
        44: "Staff of the Woodlands",
        47: "Wand of Cold",
        51: "Wand of Enemy Detection",
        54: "Wand of Fear",
        57: "Wand of Fire Balls",
        61: "Wand of Illusion",
        64: "Wand of Lightning Bolts",
        69: "Wand of Magic Detection",
        74: "Wand of Magic Missiles",
        79: "Wand of Metal Detection",
        84: "Wand of Negation",
        87: "Wand of Paralysation",
        90: "Wand of Polymorph",
        94: "Wand of Radiance",
        97: "Wand of Secret Door Detection",
        98: "Wand of Summoning",
        100: "Wand of Trap Detection",
    }
    rolled = random.randint(1, 100)
    result = get_closest_key(rolled, rods_staves_wands_table)

    if "Rod" in result:
        charges = roll(dice="1d10")
    elif result.startswith("Staff"):
        charges = roll(dice="3d10")
    else:
        charges = roll(dice="2d10")

    return f"{result}, {charges} charge(s)"


def roll_spell(s):
    n, _ = s.split()
    n = int(n)
    rolled = []
    spells = [
        "Acid Fog",
        "Air Breathing",
        "Animal Friendship",
        "Animate Dead",
        "Anti-Magic Shell",
        "Auditory Illusion",
        "Barkskin",
        "Blacklight",
        "Bless",
        "Blight",
        "Blindness / Deafness",
        "Blur",
        "Call Lightning",
        "Cause Disease",
        "Cause Fear",
        "Cause Light Wounds (C) ",
        "Cause Light Wounds (D) ",
        "Cause Ser. Wounds (C) ",
        "Cause Ser. Wounds (D) ",
        "Chaos",
        "Charm Monster",
        "Charm Person",
        "Chromatic Orb",
        "Clairvoyance",
        "Cloudkill",
        "Colour Spray",
        "Commune",
        "Commune with Nature ",
        "Confusion (I)",
        "Confusion (MU)",
        "Conjure Elemental",
        "Continual Light (MU) ",
        "Control Weather (D)",
        "Control Weather (MU) ",
        "Create Food",
        "Create Water (C)",
        "Create Water (D)",
        "Cure Disease",
        "Cure Light Wounds (C) ",
        "Cure Light Wounds (D) ",
        "Cure Ser. Wounds (C) ",
        "Cure Ser. Wounds (D) ",
        "Curse (C)",
        "Curse (MU)",
        "Dancing Lights",
        "Darkness (C)",
        "Darkness (I)",
        "Darkness (MU)",
        "Death Spell",
        "Demi-Shadow Monsters ",
        "Detect Danger",
        "Detect Evil (C)",
        "Detect Evil (MU)",
        "Detect Illusion",
        "Detect Invisible",
        "Detect Magic (C)",
        "Detect Magic (I)",
        "Detect Magic (MU)",
        "Dimension Door",
        "Disintegrate",
        "Dispel Evil",
        "Dispel Illusion",
        "Dispel Magic (D)",
        "Dispel Magic (I)",
        "Dispel Magic (MU)",
        "Dream Quest",
        "EmotionFascinate",
        "Fear",
        "Feeblemind",
        "Find Traps",
        "Finger of Death",
        "Fire Ball",
        "Flesh to Stone",
        "Floating Disc",
        "Fly",
        "Geas",
        "Glamour",
        "Growth of Animal",
        "Growth of Nature",
        "Growth of Plants",
        "Hallucin. Terrain (I)",
        "Hallucin. Terrain (MU) ",
        "Haste",
        "Heat Metal",
        "Hold Animal",
        "Hold Monster",
        "Hold Person (C)",
        "Hold Person (MU)",
        "Hold Portal",
        "Hypnotic Pattern",
        "Hypnotism",
        "Illusion",
        "Illusory Stamina",
        "Impersonation",
        "Improved Invisibility",
        "Impr. Phantasmal Force ",
        "Infravision",
        "Insect Plague",
        "Invis. 10’ Radius (I)",
        "Invis. 10’ Radius (MU) ",
        "Invisibility (I)",
        "Invisibility (MU)",
        "Contact Higher Plane",
        "Cont. Darkness (C)",
        "Cont. Darkness (MU)",
        "Continual Light (C)Entangle",
        "ESP",
        "Faerie Fire",
        "False Aura",
        "Invisibility to Animals ",
        "Invisible Stalker",
        "Knock",
        "Know Alignment",
        "Levitate",
        "Light (C)",
        "Light (I)",
        "Light (MU)",
        "Lightning Bolt",
        "Locate Object (C)",
        "Locate Object (MU)",
        "Locate Plant or Animal ",
        "Looking Glass",
        "Lower Water",
        "Magic Jar",
        "Magic Missile",
        "Magic Mouth",
        "Major Creation",
        "Manifest Dream",
        "Massmorph (I)",
        "Massmorph (MU)",
        "Mass Suggestion",
        "Maze of Mirrors",
        "Minor Creation",
        "Mirror Image (I)",
        "Mirror Image (MU)",
        "Mislead",
        "Move Earth",
        "Neutralize Poison",
        "Nondetection",
        "Obscuring Mist",
        "Paralysation",
        "Part Water",
        "Pass Plant",
        "Pass-Wall",
        "Permanent Illusion",
        "Phantasmal Force (I)",
        "Phantasmal Force (MU) ",
        "Phantasmal Killer",
        "Phantom Steed",
        "Polymorph Others",
        "Polymorph Self",
        "Predict Weather",
        "Produce Flame",
        "Projected Image (I)",
        "Projected Image (MU) ",
        "Protection from Poison ",
        "Prot. Evil 10’ Radius (C) ",
        "Prot. Evil 10’ Rad. (MU) ",
        "Prot. Fire and Lightning ",
        "Prot. from Evil (C)",
        "Prot. from Evil (MU) ",
        "Prot. Normal Missiles ",
        "Prot. Plants and Animals",
        "Purify Food and Water ",
        "Quasimorph",
        "Quest",
        "Rainbow Pattern",
        "Raise Dead",
        "Read Languages",
        "Read Magic (I)",
        "Read Magic (MU)",
        "Reincarnation",
        "Remove Curse (C)",
        "Remove Curse (MU)",
        "Remove Fear",
        "Remove Geas",
        "Remove Quest",
        "Resist Cold",
        "Resist Fire",
        "Rope Trick",
        "Seeming",
        "Shades",
        "Shadowcast",
        "Shadow Monsters",
        "Shadowy Transformation",
        "Shield",
        "Silence 15’ Radius",
        "Sleep",
        "Slow Poison",
        "Snake Charm",
        "Solid Fog",
        "Speak with Animals (C) ",
        "Speak with Animals (D) ",
        "Speak with Plants (C) ",
        "Speak with Plants (D) ",
        "Spectral Force",
        "Spook",
        "Sticks to Snakes",
        "Stone to Flesh",
        "Striking",
        "Suggestion",
        "Summon Animals",
        "Telekinesis",
        "Teleport",
        "Temperature Control ",
        "Thru the Looking Glass ",
        "Time Flow",
        "Trans. Mud–Rock (D) ",
        "Trans. Mud–Rock (MU) ",
        "Trans. Rock–Mud (D) ",
        "Trans. Rock–Mud (MU) ",
        "Tree Shape",
        "Triggered Illusion",
        "True Seeing",
        "Veil of Abandonment ",
        "Ventriloquism",
        "Vision",
        "Visitation",
        "Wall of Fire",
        "Wall of Fog",
        "Wall of Ice",
        "Wall of Stone",
        "Wall of Thorns",
        "Warp Wood",
        "Water Breathing (D)",
        "Water Breathing (MU) ",
        "Web",
        "Whispering Wind",
        "Wizard Eye",
        "Wizard Lock",
        "Wraithform",
    ]
    for _ in range(n):
        spell = random.choice(spells)
        rolled.append(f"Scroll of {spell}")
    rolled.insert(0, "Scrolls")
    return rolled


def roll_scroll_or_map():
    scroll_map_table = {
        1: "1 Spell",
        25: "2 Spells",
        31: "3 Spells",
        34: "5 Spells",
        35: "7 Spells",
        40: "Cursed Scroll",
        50: "Protection from Elementals",
        60: "Protection from Lycanthropes",
        65: "Protection from Magic",
        75: "Protection from Undead",
        78: "Treasure Map: I",
        80: "Treasure Map: II",
        82: "Treasure Map: III",
        83: "Treasure Map: IV",
        84: "Treasure Map: V",
        85: "Treasure Map: VI",
        86: "Treasure Map: VII",
        90: "Treasure Map: VIII",
        95: "Treasure Map: IX",
        96: "Treasure Map: X",
        98: "Treasure Map: XI",
        100: "Treasure Map: XII",
    }
    rolled = random.randint(1, 100)
    result = get_closest_key(rolled, scroll_map_table)
    if "Spell" in result:
        result = roll_spell(result)

    return result


def roll_sword():
    swords_table = {
        3: "Short Sword +2, Quickness",
        6: "Sword –1, Berserker (Cursed)",
        9: "Sword –1, Cursed",
        12: "Sword –2, Cursed",
        28: "Sword +1",
        31: "Sword +1, +2 vs Lycanthropes",
        34: "Sword +1, +2 vs Spell Users",
        37: "Sword +1, +3 vs Dragons",
        40: "Sword +1, +3 vs Enchanted Creatures",
        43: "Sword +1, +3 vs Regenerating Creatures",
        46: "Sword +1, +3 vs Reptiles",
        49: "Sword +1, +3 vs Shape Changers",
        52: "Sword +1, +3 vs Undead",
        55: "Sword +1, Dragon Slayer",
        56: "Sword +1, Energy Drain",
        59: "Sword +1, Flaming",
        61: "Sword +1, Frost Brand",
        64: "Sword +1, Giant Slayer",
        69: "Sword +1, Light",
        71: "Sword +1, Locate Objects",
        72: "Sword +1, Luck Blade",
        73: "Sword +1, Sharpness",
        78: "Sword +1, Sun Blade",
        79: "Sword +1, Wishes",
        80: "Sword +1, Wounding",
        85: "Sword +2",
        87: "Sword +2, Charm Person",
        88: "Sword +2, Dancing",
        89: "Sword +2, Nine Lives Stealer",
        94: "Sword +2, Venger",
        95: "Sword +2, Vorpal",
        98: "Sword +3",
        99: "Sword +3, Defender",
        100: "Sword +3, Holy Avenger",
    }

    rolled = roll("1d100")
    result = get_closest_key(rolled, swords_table)
    sword_type_roll = roll("1d6")
    sword_type_table = {2: "Short", 5: "Normal", 6: "Two-handed"}
    sword_type_result = get_closest_key(sword_type_roll, sword_type_table)
    if result.startswith("Sword"):
        result = f"{sword_type_result} {result}"
    return result


def roll_weapon():
    weapons_table = {
        1: "Arrow +1, Slaying",
        10: "Arrows +1 (2d6 arrows)",
        12: "Arrows +1 (3d10 arrows)",
        15: "Arrows +2 (1d6 arrows)",
        19: "Axe +1",
        21: "Axe +2",
        24: "Bow +1",
        25: "Crossbow +1, Distance",
        26: "Crossbow +1, Speed",
        27: "Crossbow +2, Accuracy",
        29: "Crossbow Bolts +1 (2d6 bolts)",
        31: "Crossbow Bolts +1 (3d10 bolts)",
        36: "Crossbow Bolts +2 (1d6 bolts)",
        39: "Dagger +1",
        40: "Dagger +1, Buckle",
        41: "Dagger +1, Throwing",
        42: "Dagger +1, Venomous",
        45: "Dagger +2, +3 vs orcs, goblins, and kobolds",
        46: "Dagger +2, Biter",
        50: "Javelin of Lightning (1d4+1 javelins)",
        54: "Javelin of Seeking (2d4 javelins)",
        58: "Mace +1",
        59: "Mace +1, Disrupting",
        62: "Mace +2",
        63: "Mace +3",
        68: "Sling +1",
        69: "Sling Bullet +1, Impact (1d4 bullets)",
        71: "Spear –1, Backbiter (Cursed)",
        75: "Spear +1",
        77: "Spear +2",
        78: "Spear +3",
        80: "Staff +1, Growing",
        82: "Trident –2, Yearning (Cursed)",
        87: "Trident +1, Fish Command",
        89: "Trident +1, Submission",
        93: "Trident +2, Warning",
        96: "War Hammer +1",
        98: "War Hammer +2",
        99: "War Hammer +3, Dwarven Thrower",
        100: "War Hammer +3, Thunderbolts",
    }

    rolled = roll("1d100")
    result = get_closest_key(rolled, weapons_table)
    return result


def roll_magic_items(s, level):
    n, *rest = s.split()
    n = int(n)
    items = []
    for item in range(n):
        type_ = roll_magic_item_type(level)
        items.append(type_)

    rolled_items = []
    for item in items:
        # armours
        if item == "Armour or Shield":
            rolled_items.append(roll_armour_and_shield())
        # Misc
        elif item == "Misc. Item":
            rolled_items.append(roll_misc_item())
        # Potion
        elif item == "Potion":
            rolled_items.append(roll_potion())
        elif item == "Ring":
            rolled_items.append(roll_ring())
        # Rods, staves, wands
        elif item == "Rod / Staff / Wand":
            rolled_items.append(roll_rod_staff_wand())
        # spells or maps
        elif item == "Scroll or Map":
            rolled_items.append(roll_scroll_or_map())
        elif item == "Sword":
            rolled_items.append(roll_sword())
        elif item == "Weapon":
            rolled_items.append(roll_weapon())
        else:
            rolled_items.append(item)
    rolled_items.insert(0, "Magic Items")
    return rolled_items


def expand_result(rolled_items, level):
    dice_expr = r"\dd\d"
    expanded_items = []
    for item in rolled_items:
        expanded_item = []
        splitted = item.split()
        for s in splitted:
            if re.match(dice_expr, s):
                num = roll(s)
                expanded_item.append(str(num))
            else:
                expanded_item.append(s)
        expanded_items.append(" ".join(expanded_item))

    # clean stupid n x 1000
    cleaned_items = []
    for item in expanded_items:
        if " × 1" in item:
            cleaned_items.append(item.replace(" × 1", ""))
        # roll gems if any
        elif "gems" in item:
            cleaned_items.append(roll_gems(item))
        # roll jewellery
        elif "jewellery" in item:
            cleaned_items.append(roll_jewellery(item))
        elif "magic item" in item:
            cleaned_items.append(roll_magic_items(item, level))
        else:
            cleaned_items.append(item)
    # make it an html ul list
    lis = []
    for item in cleaned_items:
        if isinstance(item, str):
            lis.append(f"<li>{item}</li>")
        elif isinstance(item, list):
            lis.append(f"<li>{item[0]}</li>")
            sublis = [f"<li>{k}</li>" for k in item[1:]]
            lis.append(f"<ul>{''.join(sublis)}</ul>")

    ul = "<ul>" + "".join(lis) + "</ul>"
    return ul
