from random import choice
from .dice import roll, get_key
from .abilities import abilities
from .constants import ALIGNMENTS


def roll_kindred_and_class():
    kindred_table = {
        3: "Breggle",
        4: "Elf",
        5: "Grimalkin",
        10: "Human",
        11: "Mossling",
        12: "Woodgrue",
    }

    kindred_roll = roll("1d12")
    k = get_key(kindred_roll, kindred_table)
    kindred = kindred_table[k]

    class_by_kindred = {
        "Breggle": {
            1: "Bard",
            2: "Cleric",
            3: "Enchanter",
            8: "Fighter",
            9: "Friar",
            11: "Hunter",
            15: "Knight",
            18: "Magician",
            20: "Thief",
        },
        "Elf": {
            2: "Bard",
            # 2: "Cleric",
            8: "Enchanter",
            12: "Fighter",
            # 9: "Friar",
            15: "Hunter",
            # 15: "Knight",
            17: "Magician",
            20: "Thief",
        },
        "Grimalkin": {
            4: "Bard",
            # 2: "Cleric",
            8: "Enchanter",
            10: "Fighter",
            # 9: "Friar",
            14: "Hunter",
            # 15: "Knight",
            16: "Magician",
            20: "Thief",
        },
        "Human": {
            2: "Bard",
            5: "Cleric",
            6: "Enchanter",
            10: "Fighter",
            12: "Friar",
            14: "Hunter",
            16: "Knight",
            18: "Magician",
            20: "Thief",
        },
        "Mossling": {
            3: "Bard",
            # 2: "Cleric",
            4: "Enchanter",
            10: "Fighter",
            # 1: "Friar",
            16: "Hunter",
            # 15: "Knight",
            17: "Magician",
            20: "Thief",
        },
        "Woodgrue": {
            5: "Bard",
            # 2: "Cleric",
            8: "Enchanter",
            10: "Fighter",
            # 9: "Friar",
            14: "Hunter",
            # 15: "Knight",
            16: "Magician",
            20: "Thief",
        },
    }
    class_roll = roll("1d20")
    k = get_key(class_roll, class_by_kindred[kindred])
    class_ = class_by_kindred[kindred][k]
    return kindred, class_


def roll_quest(alignment):
    quests = (
        (
            "Locate a lost shrine and report to the Bishop of Brackenwold (e.g. St Sedge in 0202, St Hamfast in 0309, St Cornice in 1505).",
            "Secretly carry a holy magic item to a patron (e.g. a Horn of Blasting, a Rod of Greater Healing, a Holy Mace).",
            "Destroy a powerful undead monster (e.g. the spectres in 0701, the gloam in 0906, the Descendant in 1409).",
            "Scout the movements of crookhorn troops and report to the duke (e.g. around Fort Vulgar in 0604, the ruined abbey in 0906, Prigwort in 1106).",
            "Capture a Chaotic NPC and bring them to Castle Brackenwold (e.g. Praephator Lenore in 0111, Captain Snarkscorn in 0803, Shub’s Nanna in 0911).",
            "Locate the lost relics of St Jorrael, rumoured to have been buried in hex 1705 in Mulchgrove. The adventurers do not have a map.",
        ),
        (
            "Search for magical herbs/fungi (e.g. Grinning Jenny in 0908, Horridwort in 1002, Purple Nightcap in 0510).",
            "Locate a fairy door (e.g. the emerald door in 0602, the moggle door in 0711, the dungle-crack in 1402).",
            "Loot a fabulous treasure hoard (e.g. the bicorne’s hoard in 0510, the Big Chook’s hoard in 0606, the wyrm’s hoard in 1107).",
            "Spy on the arcane doings of a wizard, on behalf of another wizard (e.g. Mostlemyre Drouge in 1106, Tamrin Tweede in 1110, Ygraine in 1802).",
            "Find a means of curing a party member’s curse (e.g. by bathing in the Lethean Well in 0209, at the hill in 0805, by visiting the Hag in 0908).",
            "Secretly carry a magic item to the Drune (e.g. a Crystal Ball, a Mirror of Life Trapping, a Ring of Protection).",
        ),
        (
            "Scout the movements of human troops and report to Atanuwë (e.g. around Fort Vulgar in 0604, Prigwort in 1106, Castle Brackenwold in 1508).",
            "Rob any weaker looking groups they encounter.",
            "Assassinate or kidnap a Lawful NPC (e.g. Sir Osric Hazelmire from Fort Vulgar in 0604, Lady Harrowmoor from Harrowmoor Keep in 1105, Abbot Spatulard from the Refuge of St Keye in 1307).",
            "Secretly carry the remains of a saint to Atanuwë.",
            "Steal a precious item from an NPC (e.g. the Rod of the Wyrd from Nodding Castle in 0210, the magic mirror from Chateau Shantywood in 1110, the Mornblade from Ferneddbole House in 1209).",
            "Sell poisonous substances (e.g. Angel’s Lament, Purple Nightcap) to a paying client. (e.g. Wyrmspittle the herbalist from Prigwort in 1106, Madame Shantywood from Chateau Shantywood in 1110).",
        ),
    )
    quest_table = {a: q for a, q in zip(ALIGNMENTS, quests)}
    return choice(quest_table[alignment])


class NPC:
    hp_per_class = {
        "Bard": "1d6",
        "Cleric": "1d6",
        "Enchanter": "1d6",
        "Fighter": "1d8",
        "Friar": "1d4",
        "Hunter": "1d8",
        "Knight": "1d8",
        "Magician": "1d4",
        "Thief": "1d4",
    }

    def __init__(self, kindred, class_, level):
        self.kindred = kindred
        self.class_ = class_
        self.level = level
        self.hp = sum(
            roll(self.hp_per_class.get(self.class_)) for _ in range(self.level)
        )

    def __repr__(self):
        return f"{self.kindred} {self.class_}, level {self.level}"


class AdventuringParty:
    def __init__(self):
        self.size = roll("1d4") + 4
        self.party_level = "1d6+3" if roll("1d6") == 1 else "1d3"
        self.kindred_and_class = [
            roll_kindred_and_class() for member in range(self.size)
        ]
        self.character_levels = [roll(self.party_level) for member in range(self.size)]
        self.characters = [
            NPC(kindred, class_, level)
            for (kindred, class_), level in zip(
                self.kindred_and_class, self.character_levels
            )
        ]
        self.treasure = " ".join(
            [f"{roll('1d100')}cp", f"{roll('1d100')}sp", f"{roll('1d100')}gp"]
        )  # TODO add gems and art objects
        # TODO - roll magic items, 5%*character level chance
        self.mounts = roll("1d100") <= 75
        self.alignment = choice(ALIGNMENTS)
        self.quest = roll_quest(self.alignment)
        # TODO : tables for names per kindred

    def __repr__(self):
        return f"Adventuring party of {self.size} {self.alignment} adventurers."
