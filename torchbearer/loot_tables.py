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


loot_tables_list = [
    loot_table_1,
    loot_table_2,
    loot_table_3,
    loot_table_4,
    loot_table_5,
]
