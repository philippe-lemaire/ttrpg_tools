import random
from dataclasses import dataclass
from .hoard_treasure import *


def roll(dice):
    """rolls ndx, where n is the number of dice (can be omitted) and x is the largest value on each die"""
    qty, size = dice.split("d")
    qty = int(qty) if qty else 1
    size = int(size)

    return sum([random.randint(1, size) for die in range(qty)])


classes_hd = {
    "Acrobat": "1d4",
    "Assassin": "1d4",
    "Barbarian": "1d8",
    "Bard": "1d6",
    "Cleric": "1d6",
    "Drow": "1d6",
    "Druid": "1d6",
    "Duergar": "1d6",
    "Dwarf": "1d8",
    "Elf": "1d6",
    "Fighter": "1d8",
    "Gnome": "1d4",
    "Half-Elf": "1d6",
    "Halfling": "1d6",
    "Half-Orc": "1d6",
    "Illusionist": "1d4",
    "Knight": "1d8",
    "Magic-user": "1d4",
    "Paladin": "1d8",
    "Ranger": "1d8",
    "Svirfneblin": "1d6",
    "Thief": "1d4",
}


class Character:
    attributes = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    MOD = {
        3: -3,
        4: -2,
        5: -2,
        6: -1,
        13: 1,
        14: 1,
        15: 1,
        16: 2,
        17: 2,
        18: 3,
    }

    def __init__(self, class_, alignment, lvl=1):
        values = [roll("3d6") for attr in self.attributes]
        for attr, value in zip(self.attributes, values):
            setattr(self, attr, value)
        self.thaco = 19
        self.lvl = lvl
        self.class_ = class_
        self.hp = 0
        self.alignment = alignment
        self.treasure_type = "u"

        for attr in self.attributes:
            setattr(self, f"{attr}_MOD", self.MOD.get(getattr(self, attr), 0))
        self.ac = 10 + self.DEX_MOD

        leather_classes = ("Acrobat", "Assassin", "Druid", "Gnome", "Thief")
        chainmail_clases = ("Barbarian", "Bard", "Half-Orc", "Ranger")
        plate_classes = (
            "Cleric",
            "Drow",
            "Duergar",
            "Dwarf",
            "Elf",
            "Fighter",
            "Half-Elf",
            "Halfling",
            "Knight",
            "Paladin",
            "Svirfneblin",
        )
        armor_options = (
            ("Leather armor", 2),
            ("Chainmail armor", 4),
            ("Plate armor", 6),
        )
        if self.class_ in leather_classes:
            self.armor_type = "Leather armor"
            self.ac += 2
        elif self.class_ in chainmail_clases:
            choice = random.choice((0, 1))
            self.armor_type = armor_options[choice][0]
            self.ac += armor_options[choice][1]
        elif self.class_ in plate_classes:
            choice = random.choice((1, 2))
            self.armor_type = armor_options[choice][0]
            self.ac += armor_options[choice][1]

        for _ in range(self.lvl):
            # compute hp for this level
            hd = classes_hd.get(self.class_)
            rolled_hp = roll(hd) + self.CON_MOD
            if rolled_hp < 1:
                rolled_hp = 1
            self.hp += rolled_hp

            magic_item_types = [
                "Armour or Shield",
                "Misc. Item",
                "Potion",
                "Ring",
                "Rod / Staff / Wand",
                "Scroll or Map",
                "Sword",
                "Weapon",
            ]
            rolled_items = []
            threshold = 5 * self.lvl
            for item in magic_item_types:

                # armours
                if item == "Armour or Shield":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_armour_and_shield())
                # Misc
                elif item == "Misc. Item":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_misc_item())
                # Potion
                elif item == "Potion":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_potion())
                elif item == "Ring":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_ring())
                # Rods, staves, wands
                elif item == "Rod / Staff / Wand":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_rod_staff_wand())
                # spells or maps
                elif item == "Scroll or Map":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_scroll_or_map())
                elif item == "Sword":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_sword())
                elif item == "Weapon":
                    r = roll("1d100")
                    if r <= threshold:
                        rolled_items.append(roll_weapon())
                else:
                    rolled_items.append(item)
        if not rolled_items:
            self.magic_items = None
        else:
            self.magic_items = rolled_items

    def __repr__(self):
        return ",".join(
            [self.class_, f"Level {self.lvl}", f"HP: {self.hp}"]
            + [f"{attr}: {getattr(self, attr)}" for attr in self.attributes]
        )


def roll_adventuring_party(level):
    number = None
    max_level = 3
    alignment = random.choice(["Chaotic", "Neutral", "Lawful"])
    if level == "1":
        number = roll("1d4") + 4

    if level == "2":
        number = roll("1d6") + 6
        max_level = roll("1d6") + 3

    party = [
        Character(
            class_=random.choice(list(classes_hd.keys())),
            lvl=random.randint(1, max_level),
            alignment=alignment,
        )
        for _ in range(number)
    ]
    return party
