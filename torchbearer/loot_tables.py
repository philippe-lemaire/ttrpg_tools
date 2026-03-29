from dataclasses import dataclass

books_and_maps = "Books & Maps"
gear = "Gear"
stuff = "Stuff"
treasure_and_valuables_1 = "Treasures & Valuables 1"
treasure_and_valuables_2 = "Treasures & Valuables 2"
magic = "Magic"


@dataclass
class LootTable:
    title: str
    roll: str
    description: str
    content: dict


loot_table_1 = LootTable(
    title="Loot Table 1",
    roll="2d6",
    description="""Use Loot Table 1 for twist encounters with creatures of Might 1-2, when
generating items found while using the Scavenger skill and for any other
shrug-of-the-shoulders-I-dunno-there-might-be-loot needs.""",
    content={
        "2": books_and_maps,
        "3-6": gear,
        "7-10": stuff,
        "11": treasure_and_valuables_1,
        "12": magic,
    },
)

loot_table_2 = LootTable(
    title="Loot Table 2",
    roll="2d6",
    description="""Use Loot Table 2 for planned encounters with creatures of Might 1-2
and for unplanned or twist encounters with creatures of Might 3-4.""",
    content={
        "2-3": books_and_maps,
        "4-5": stuff,
        "6-9": gear,
        "10-11": treasure_and_valuables_1,
        "12": magic,
    },
)
loot_table_3 = LootTable(
    title="Loot Table 3",
    roll="2d6",
    description="""Use Loot Table 3 for planned encounters with creatures of Might 3-4
and for twist or unplanned encounters with creatures of Might 5-6.""",
    content={
        "2-3": stuff,
        "4-5": books_and_maps,
        "6-8": gear,
        "9-10": treasure_and_valuables_1,
        "11": treasure_and_valuables_2,
        "12": magic,
    },
)


loot_table_4 = LootTable(
    title="Loot Table 4",
    roll="2d6",
    description="""Use Loot Table 4 for planned encounters with Might 5-6 denizens and
for twist encounters with Might 7-8 denizens.""",
    content={
        "2-3": "Gear",
        "4": "Treasure & Valuables 1",
        "5-6": "Treasure & Valuables 3",
        "7-9": "Treasure & Valuables 2",
        "10-11": "Books & Maps",
        "12": " Magic",
    },
)

loot_table_5 = LootTable(
    title="Loot Table 5",
    roll="2d6",
    description="""Use Loot Table 5 for
planned encounters with Might 7-8 denizens.""",
    content={
        "2-3": "Books & Maps",
        "4": "Treasure & Valuables 2",
        "5": "Treasure & Valuables 3",
        "6-8": "Treasure & Valuables 4",
        "9-12": "Magic",
    },
)

loot_subtables = {
    books_and_maps: {
        "title": books_and_maps,
        "roll": "3d6",
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
    gear: {
        "title": gear,
        "roll": "3d6",
        3: "Hidden valuables. Roll on Treasure & Valuables 2",
        4: "Rare item. Roll 1d6: 1: thieves’ tools, 2: ladder, 3: holy water, 4: wolfsbane, 5: musical instrument, 6: grappling hook",
        5: "Battle regalia. Helmet or shield, game master chooses",
        6: "Sacks and such. Roll 1d6: 1: large sack, 2: small sack, 3: purse, 4: satchel, 5: backpack, 6: chest",
        7: "Fortunate food. Roll 1d3 amount and 1d6 type: 1: forage, 2: game, 3: fresh rations, 4: preserved rations, 5: garlic, 6: salt block (pack 1)",
        8: "Equipment. Roll 1d6: 1: iron spikes, 2: hammer, 3: pry bar, 4: chalk, 5: rope, 6: tinderbox",
        9: "Light source. Roll 1d3 for amount and 1d6 for type: 1-4: candles, 5: torches, 6: flasks of oil",
        10: "Supplies. Roll 1d6: 1-4: skill supplies, 5: spell materials, 6: sacramentals",
        11: "Clothing. Roll 1d6: 1: cloak, 2: hat, 3: wool sweater, 4: shoes, 5: belt or bandolier, 6: boots",
        12: "Bottles and barrels. Roll 1d6: 1: waterskin, 2: clay pot, 3: wooden canteen, 4: bottle, 5: jug, 6: barrel",
        13: "Weapon. Either a weapon used by the opponent encountered or roll on the Weapons subtable",
        14: "Tools. Skill gear or tools, game master chooses",
        15: "Armor. Roll 1d6 for type: 1-4: leather, 5: chain, 6: plate",
        16: "Animal. Dog, mule, cat or starved horse, game master chooses",
        17: "Hidden dwarven or elven weapon. Roll on Weapons subtable for type",
        18: "Hidden dwarven or elven armor. Roll 1d6 for type: 1-4: leather, 5: chain, 6: plate",
    },
    stuff: {
        "title": stuff,
        "roll": "3d6",
        3: "Vile cult symbols",
        4: "Bag of rocks",
        5: "Bones",
        6: "String",
        7: "Dried leaves",
        8: "Some teeth",
        9: "Lint",
        10: "Worthless coins of unknown provenance",
        11: "Indecipherable notes",
        12: "Rusty keys",
        13: "An idol for an unknown religion",
        14: "A child’s dolly or puppet",
        15: "A tool of unknown use",
        16: "Dice",
        17: "A rusty nail",
        18: "A chipped bowl or cup",
    },
    treasure_and_valuables_1: {},
    treasure_and_valuables_2: {},
    magic: {},
}


loot_tables_list = [
    loot_table_1,
    loot_table_2,
    loot_table_3,
    loot_table_4,
    loot_table_5,
]
