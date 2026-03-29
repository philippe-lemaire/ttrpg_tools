from .loot_tables import (
    books_and_maps,
    gear,
    stuff,
    magic,
    treasure_and_valuables_1,
    treasure_and_valuables_2,
)
from dataclasses import dataclass


@dataclass
class LootSubTable:
    title: str
    roll: str
    extraheaders: list
    anchor_name: str
    content: dict


books_and_maps_subtable = LootSubTable(
    title=books_and_maps,
    roll="3d6",
    extraheaders=["Value", "Inv"],
    anchor_name=books_and_maps.replace(" ", "-").lower(),
    content={
        3: ("Accurate map of dungeon level or region", "X", "pack 1"),
        4: ("Accurate map of a small region or set of rooms", "X", "pack 1"),
        5: ("Accurate map of a single, nearby area or room", "X", "pack 1"),
        6: (
            "Correspondence between an adversary and their ally (note letter’s language)",
            "X",
            "pack 1",
        ),
        7: ("Monograph containing prophesy in an ancient tongue", "X", "pack 1"),
        8: ("Dwarven chronicle of a lost settlement", "X", "pack 1"),
        9: (
            "Detailed description of a monster's Nature written by a forgotten philosopher",
            "X",
            "pack 1",
        ),
        10: ("Cyclopedia", "3D", "pack 2"),
        11: ("Book of myths", "2D", "pack 1"),
        12: ("Bestiary", "3D", "pack 2"),
        13: ("Romance", "2D", "pack 1"),
        14: ("Puzzle book that reveals the location of a secret", "X", "pack 2"),
        15: ("Map of location of a tomb containing a magical artifact", "X", "pack 1"),
        16: ("Map of location of a crypt containing lost treasures", "X", "pack 2"),
        17: ("Tome of ancient lore in a forgotten tongue", "X", "pack 3"),
        18: (
            "Lost spell book(s): containing 2d3 spells of circles 2 through 4 (game master’s choice)",
            "X",
            "pack 2",
        ),
    },
)

gear_subtable = LootSubTable(
    title=gear,
    roll="3d6",
    extraheaders=[],
    anchor_name=gear.replace(" ", "-").lower(),
    content={
        3: ("Hidden valuables. Roll on Treasure & Valuables 2",),
        4: (
            "Rare item. Roll 1d6: 1: thieves’ tools, 2: ladder, 3: holy water, 4: wolfsbane, 5: musical instrument, 6: grappling hook",
        ),
        5: ("Battle regalia. Helmet or shield, game master chooses",),
        6: (
            "Sacks and such. Roll 1d6: 1: large sack, 2: small sack, 3: purse, 4: satchel, 5: backpack, 6: chest",
        ),
        7: (
            "Fortunate food. Roll 1d3 amount and 1d6 type: 1: forage, 2: game, 3: fresh rations, 4: preserved rations, 5: garlic, 6: salt block (pack 1)",
        ),
        8: (
            "Equipment. Roll 1d6: 1: iron spikes, 2: hammer, 3: pry bar, 4: chalk, 5: rope, 6: tinderbox",
        ),
        9: (
            "Light source. Roll 1d3 for amount and 1d6 for type: 1-4: candles, 5: torches, 6: flasks of oil",
        ),
        10: (
            "Supplies. Roll 1d6: 1-4: skill supplies, 5: spell materials, 6: sacramentals",
        ),
        11: (
            "Clothing. Roll 1d6: 1: cloak, 2: hat, 3: wool sweater, 4: shoes, 5: belt or bandolier, 6: boots",
        ),
        12: (
            "Bottles and barrels. Roll 1d6: 1: waterskin, 2: clay pot, 3: wooden canteen, 4: bottle, 5: jug, 6: barrel",
        ),
        13: (
            "Weapon. Either a weapon used by the opponent encountered or roll on the Weapons subtable",
        ),
        14: ("Tools. Skill gear or tools, game master chooses",),
        15: ("Armor. Roll 1d6 for type: 1-4: leather, 5: chain, 6: plate",),
        16: ("Animal. Dog, mule, cat or starved horse, game master chooses",),
        17: ("Hidden dwarven or elven weapon. Roll on Weapons subtable for type",),
        18: (
            "Hidden dwarven or elven armor. Roll 1d6 for type: 1-4: leather, 5: chain, 6: plate",
        ),
    },
)

stuff_subtable = LootSubTable(
    title=stuff,
    roll="3d6",
    extraheaders=[],
    anchor_name=stuff.replace(" ", "-").lower(),
    content={
        3: ("Vile cult symbols",),
        4: ("Bag of rocks",),
        5: ("Bones",),
        6: ("String",),
        7: ("Dried leaves",),
        8: ("Some teeth",),
        9: ("Lint",),
        10: ("Worthless coins of unknown provenance",),
        11: ("Indecipherable notes",),
        12: ("Rusty keys",),
        13: ("An idol for an unknown religion",),
        14: ("A child’s dolly or puppet",),
        15: ("A tool of unknown use",),
        16: ("Dice",),
        17: ("A rusty nail",),
        18: ("A chipped bowl or cup",),
    },
)

tome_of_ancient_lore_subtable = LootSubTable(
    title="Tome of Ancient Lore",
    roll="1d6",
    extraheaders=["Inventory"],
    anchor_name="Tome of Ancient Lore".replace(" ", "-").lower(),
    content={
        1: ("Recipes for magical potions", "pack 3"),
        2: (
            "Characteristics of enchanted items",
            "pack 3",
        ),
        3: (
            "Dweomers of spells (+1D Arcanist gear)",
            "pack 3",
        ),
        4: (
            "Pantheons of Immortals (+1D Theologian gear)",
            "pack 3",
        ),
        5: (
            "Nature of living things (+1D Lore Master and Healer gear)",
            "pack 3",
        ),
        6: (
            "Structure and components for a heretofore unknown spell",
            "pack 3",
        ),
    },
)


magic_subtable = LootSubTable(
    roll="2d6",
    title="Magic Subtable",
    extraheaders=[],
    anchor_name="Magic Subtable".replace(" ", "-").lower(),
    content={
        2: ("Cursed item. Roll again on the Cursed Item subtable",),
        3: (
            "Wards and charms. Roll 1d6: 1-2: Drowner’s Friend, 3-4: Jade Ward, 5: Amulet of Stars, 6: Aegis Bracers",
        ),
        4: (
            "Staves and wands. Roll 1d6: 1-2: Wizard’s Staff, 3-4: Wand of Unbinding, 5-6: Dowsing Rod",
        ),
        5: ("Spell book: 1d3 circles of spells (game master’s choice)",),
        6: (
            "Enchanted clothing. Roll 1d6: 1: cloak, 2: hat, 3: wool sweater, 4: shoes, 5: belt or bandolier, 6: boots",
        ),
        7: ("Potion. Roll on Potions subtable",),
        8: (
            "Scroll. Roll 1d6: 1-2: 1st circle, 3-4: 2nd circle, 5: 3rd circle, 6: 4th circle",
        ),
        9: ("Relic. Roll 1d6: 1-4: minor, 5: named relic, 6: great relic",),
        10: (
            "Magical gear. Roll 1d6: 1: Horn of Drenge, 2: Burglar’s Gloves, 3: Elven Rope, 4: Girdle of Troll Might, 5: Haversack of Holding, 6: Elven Cloak",
        ),
        11: (
            "Enchanted weapon. Roll 1d6: 1: Mind Sword, 2-3: Blood-Seeking Sword, 4: Celestial Mace, 5: Slaughterer’s Friend, 6: elven or dwarven weapon (see the entry below the Gear subtable)",
        ),
        12: (
            "Enchanted armor. Roll 1d6: 1: shield, 2: helmet, 3: leather, 4: chain, 5: plate, 6: Forge Mask",
        ),
    },
)


weapons_subtable = LootSubTable(
    roll="3d6",
    title="Weapons Subtable",
    extraheaders=[],
    anchor_name="weapons-subtable",
    content={
        3: ("Crossbow",),
        4: ("Bow",),
        5: ("Battle axe",),
        6: ("Dagger",),
        7: ("Flail",),
        8: ("Mace",),
        9: ("Shield",),
        10: ("Staff",),
        11: ("Hand axe",),
        12: ("Spear",),
        13: ("Sword",),
        14: ("Sling",),
        15: ("Polearm",),
        16: ("Halberd",),
        17: ("Great sword",),
        18: ("Staff",),
    },
)

potion_subtable = LootSubTable(
    roll="2d6",
    title="Potions Subtable",
    extraheaders=["Draughts", "Inventory"],
    anchor_name="potions-subtable",
    content={
        2: ("Poison", "1", "pack 1"),
        3: ("Dragon’s Breath", "1", "pack 1"),
        4: ("Sovereign Remedy", "1d3", "pack 1 per draught"),
        5: ("Theriac", "1d2+1", "pack 1 per draught"),
        6: ("Soothing Draught", "1d3", "pack 1 per draught"),
        7: ("Soldier's Friend", "1d2+1", "pack 1 per draught"),
        8: ("Faerie Wine", "1d2+1", "pack 1"),
        9: ("Liquor of Courage", "1d3", "pack 1 per draught"),
        10: ("Philter of Vigor", "1d3", "pack 1 per draught"),
        11: ("Effervescent Tonic", "2", "pack 1"),
        12: ("Giant's Blood", "1d2", "pack 1 per draught"),
    },
)
cursed_items_subtables = LootSubTable(
    roll="2d6",
    title="Cursed Items Subtable",
    extraheaders=[],
    anchor_name="cursed-items-subtable",
    content={
        "2-5": (
            "Cursed weapon. Reduces wielder’s Might by 1; must be wielded in combat; cannot be discarded until the curse is removed.",
        ),
        "6-7": ("Poison. Appears as another potion; acts as poison when used.",),
        "8": (
            "Cursed amulet. Worth 1D (worn/neck). It cannot be voluntarily removed except to be given away to anyone who asks for food, shelter or money. It can be stolen or taken by force.",
        ),
        "9": (
            "Cursed scroll. Appears as standard first circle spell, but when used it has no effect but to empty the magician's memory palace, causing the dreaded Temerarious Discharge.",
        ),
        "10": ("Cursed gem. See entry under the Gems subtable.",),
        "11": (
            "Cursed armor. Offers no protection but looks great (and even counts as Finery in courtly situations). Cursed armor must be worn at all times; it may not be discarded until the curse is removed.",
        ),
        "12": (
            "Cursed equipment. -1s to an appropriate skill test. Item must be used when testing related skill and cannot be discarded until the curse is removed.",
        ),
    },
)

treasure_and_valuables_1_subtable = LootSubTable(
    roll="2d6",
    title="Treasure and Valuables 1",
    extraheaders=[],
    anchor_name="Treasure and Valuables 1".replace(" ", "-").lower(),
    content={
        "2-3": ("Jewelry Subtable 1",),
        "4-8": ("Coins Subtable 1",),
        "9-10": ("Gem Subtable 1",),
        "11-12": ("Books & Maps Subtable",),
    },
)
treasure_and_valuables_2_subtable = LootSubTable(
    roll="2d6",
    title="Treasure and Valuables 2",
    extraheaders=[],
    anchor_name="Treasure and Valuables 2".replace(" ", "-").lower(),
    content={
        "2-4": ("Jewelry Subtable 1",),
        "5-6": ("Coins Subtable 1",),
        "7-8": ("Coins Subtable 2",),
        "9-10": ("Gems Subtable 1",),
        "11": ("Books & Maps Subtable",),
        "12": ("Potions Subtable",),
    },
)
coins_subtables_1 = LootSubTable(
    roll="1d6",
    title="Coins Subtable 1",
    extraheaders=["Value", "Inventory"],
    anchor_name="Coins Subtable 1".replace(" ", "-").lower(),
    content={
        "1-3": ("Small sack of copper coins", "1D", "pack 2"),
        "4-5": ("Pouch of silver coins", "1D", "pack 1"),
        "6": ("Pouch of gold coins", "2D", "pack 1"),
    },
)

coins_subtables_2 = LootSubTable(
    roll="1d6",
    title="Coins Subtable 2",
    extraheaders=["Value", "Inventory"],
    anchor_name="Coins Subtable 2".replace(" ", "-").lower(),
    content={
        1: ("Small sack of copper coins", "1D", "pack 2"),
        2: ("Small sack of silver coins", "2D", "pack 2"),
        3: ("Small sack of gold coins", "4D", "pack 2"),
        4: ("Large sack of copper coins", "3D", "pack 6"),
        5: ("Satchel of silver coins", "3D", "pack 3"),
        6: ("Satchel of gold coins", "6D", "pack 3"),
    },
)

gem_subtables_1 = LootSubTable(
    roll="2d6",
    title="Gem Subtable 1",
    extraheaders=["Value", "Inventory"],
    anchor_name="Gem Subtable 1".replace(" ", "-").lower(),
    content={
        2: ("Cursed gem", "8D", "pack 1"),
        3: ("Pouch of precious stones (3)", "9D", "pack 1"),
        4: ("Chipped semiprecious stone", "1D", "pocket"),
        5: ("Fine semiprecious stone", "2D", "pocket"),
        "6-7": ("Fine precious stone", "3D", "pocket"),
        8: ("Chipped precious stone", "3D", "pocket"),
        9: ("Pouch of semiprecious stones (3)", "6D", "pack 1"),
        10: ("Box of semiprecious stones (6)", "12D", "pack 2"),
        11: ("Box of precious stones (6)", "18D", "pack 2"),
        12: ("Magical Gems subtable", "3D", "pocket"),
    },
)


jewelry_subtables_1 = LootSubTable(
    roll="2d6",
    title="Jewelry Subtable 1",
    extraheaders=["Value", "Inventory"],
    anchor_name="Jewelry Subtable 1".replace(" ", "-").lower(),
    content={
        "2-3": ("Brooch", "4D", "worn/cloak 1 or pocket"),
        "4": ("Ring", "5D", "worn/hands 1 or pocket"),
        "5": ("Bracelet", "3D", "worn/hands 1 or pocket"),
        "6": ("Pendant", "2D", "worn/neck or pocket"),
        "7": ("Amulet", "1D", "worn/neck or pocket"),
        "8": ("Buckle", "2D", "belt 1 or pocket"),
        "9": ("Jeweled pin", "3D", "worn/cloak 1 or pocket"),
        "10": ("Armband", "4D", "upper arm 1"),
        "11": ("Necklace", "5D", "worn/neck or pocket"),
        "12": ("Gold tooth", "2D", "mouth 1 or pocket"),
    },
)

magical_gems_subtables = LootSubTable(
    roll="1d6",
    title="Magical Gems Subtable",
    extraheaders=[],
    anchor_name="Magical Gems Subtable".replace(" ", "-").lower(),
    content={
        1: (
            "<em>Mind Gem:</em> Peering through this gem grants +2D to find hidden, secret or concealed people or items. It also reduces light to dim light and dim light to darkness when peering through it.",
        ),
        2: (
            "<em>Radiant Gem:</em> This gem emits a constant, steady, silvery glow. The glow is equivalent to a candle, but can never be doused.",
        ),
        3: (
            "<em>Blood Gem:</em> If sewn into living flesh, this gem grants an additional wise related to a monster, creature or people. Embedding the gem in flesh imposes the injured condition that cannot be treated or recovered from, Grit your teeth to eliminate the penalty. Removing the gem removes the wise.",
        ),
        4: (
            "<em>Soul Gem:</em> Those who die while in possession of this gem find their souls trapped within it, rather than passing on to the Dry Lands.",
        ),
        5: (
            "<em>Beguiling Gem:</em> If sewn into your raiment for all to see, this gem grants the Beautiful trait at level 2 (and does not count against the four trait limit). Each beneficial use of the trait ages the bearer one year. Lose the gem and lose the trait, but retain the years.",
        ),
        6: (
            "<em>Eldritch Gem:</em> This gem contains 1d3 spells (game master’s choice). Activating a spell costs a turn or check. Once all spells are activated, the gem crumbles to dust. If dipped in water at any time, the gem dissolves, releasing any spells held within it in 1d6 turns.",
        ),
    },
)


loot_subtables = [
    books_and_maps_subtable,
    tome_of_ancient_lore_subtable,
    gear_subtable,
    stuff_subtable,
    magic_subtable,
    weapons_subtable,
    potion_subtable,
    cursed_items_subtables,
    treasure_and_valuables_1_subtable,
    treasure_and_valuables_2_subtable,
    coins_subtables_1,
    coins_subtables_2,
    gem_subtables_1,
    jewelry_subtables_1,
    magical_gems_subtables,
]
