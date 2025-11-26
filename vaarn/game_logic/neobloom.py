from random import choice
from dataclasses import dataclass
from .special_rules import SpecialRule


shape_leaves_bark_flowers_table = (
    (
        "Hulking",
        "Leopard-Print",
        "Chalky White",
        "Have Tiny Teeth",
    ),
    (
        "Gnarled",
        "Black",
        "Crimson",
        "Have Tongues",
    ),
    (
        "Elegant",
        "White",
        "Silver",
        "Pure Black",
    ),
    (
        "Knotted",
        "Coral Pink",
        "Geometric Whorls",
        "Like Rising Suns",
    ),
    (
        "Bulbous",
        "Square",
        "Covered in Blue Moss",
        "Like Setting Suns",
    ),
    (
        "Child-like",
        "Like New Moons",
        "Hairy",
        "Cloud-like",
    ),
    (
        "Thin",
        "Like Full Moons",
        "Translucent",
        "Translucent",
    ),
    (
        "Writing",
        "Eye-Patterned",
        "Cement Grey",
        "Contain Tiny Eyes",
    ),
    (
        "Sinuous",
        "Blood Red",
        "Rust Orange",
        "Colourless and Ashen",
    ),
    (
        "Round",
        "Orange",
        "Warning Yellow",
        "Heliotrope Purple",
    ),
    (
        "Humanoid",
        "Indigo",
        "Midnight Blue",
        "Stormcloud Blue",
    ),
    (
        "Top-Heavy",
        "Azure",
        "Electric Blue",
        "Blood Red",
    ),
    (
        "Wispy",
        "Violet",
        "Bruise Purple",
        "Golden Trumpet-Shapes",
    ),
    (
        "Swollen",
        "Bronze",
        "Golden",
        "Fleshy Pink",
    ),
    (
        "Towering",
        "Furred",
        "Glossy Black",
        "Shaped like Ears",
    ),
    (
        "Hug the Ground",
        "Like Tiny Hands",
        "Deep Green",
        "Iridescent",
    ),
    (
        "Tangled",
        "Glass-like",
        "Frost-White",
        "Silver Bell-Shapes",
    ),
    (
        "Ragged",
        "Spiny",
        "Emerald Green",
        "Only Open at Night",
    ),
    (
        "Unstable",
        "Are Plastic; Glued on",
        "Hot Pink",
        "Are Plastic; Glued on",
    ),
    (
        "Fire-Scarred",
        "Zebra-Striped",
        "Like Snakeskin",
        "Change Colour Daily",
    ),
)

name_manner_vox_pod_quirk_table = (
    (
        "Artherry",
        "Arrogant",
        "Shrill",
        "Can Only Say Your Name",
    ),
    (
        "Bittle",
        "Cheerful",
        "Buzzing",
        "Pollinated by Tiny Winged Snakes",
    ),
    (
        "Wintercup",
        "Callous",
        "Deep",
        "Shed Leaves When Nervous",
    ),
    (
        "Creenash",
        "Confident",
        "Silky",
        "Flowers Smell of Cinnamon",
    ),
    (
        "Fallower",
        "Decadent",
        "Nasal",
        "Flowers Smell of Rotten Meat",
    ),
    (
        "Zedoak",
        "Fanatical",
        "Heroic",
        "Flowers Smell of Metal",
    ),
    (
        "Grassel",
        "Grim",
        "Whiny",
        "Off-Cut from More Famous Neobloom",
    ),
    (
        "Summerroot",
        "Honourable",
        "Jovial",
        "Wear Boots on Your Roots",
    ),
    (
        "Burnum",
        "Melancholy",
        "Monotone",
        "Prayers Carved in Your Bark",
    ),
    (
        "Azolly",
        "Mellow",
        "Jittery",
        "Love Poem Carved in Your Bark",
    ),
    (
        "Lanket",
        "Petty",
        "Booming",
        "Map Carved in Your Bark",
    ),
    (
        "Bitterbush",
        "Sadistic",
        "Staccato",
        "Face Carved in Your Bark",
    ),
    (
        "Prick",
        "Shy",
        "Harsh",
        "Even Smaller Sentient Bromeliad Parasites You",
    ),
    (
        "Cotterwort",
        "Obnoxious",
        "Halting",
        "Preserve Insect Specimens in Your Sap",
    ),
    (
        "Tassel",
        "Perfectionist",
        "Menacing",
        "Sword Stuck in Your Trunk",
    ),
    (
        "Henplague",
        "Romantic",
        "Despairing",
        "Once Struck by Lightning, Never Shut up About It",
    ),
    (
        "Kinnik",
        "Pretentious",
        "Animated",
        "Charming Singing Frog Lives In Your Branches",
    ),
    (
        "Cursenettle",
        "Shallow",
        "Honeyed",
        "Rude, Disgusting Bird Nests In Your Branches",
    ),
    (
        "Falseal",
        "Violent",
        "Whispering",
        "Despised by Other Neoblooms",
    ),
    (
        "Inkweed",
        "Witty",
        "Soothing",
        "Bigoted Vegetable Supremacist",
    ),
)

bloomboons_data = (
    (
        "Plated Bark",
        " gain +2 base AV.",
    ),
    (
        "Mirrored Leaves",
        " DEX save to reflect Beam attacks back at the source. DIS when hiding.",
    ),
    (
        "Barbed Bark",
        " opponents who miss melee attacks against you suffer d4 damage.",
    ),
    (
        "Shield Vines",
        " spend two points of DEX to grow a Shield Vine, adding +1 Armour Defence. DEX loss cannot heal until you choose to shed all vines.",
    ),
    (
        "Lashing Vines",
        " spend two points of STR to grow a Lashing Vine, adding +1 melee attack (d6) per round. STR loss cannot heal until you choose to shed all vines.",
    ),
    (
        "Vantablooms",
        " your light-absorbing vantablooms create a cloud of shadows around you. Ranged attacks have DIS to hit you. You have ADV to hide from pursuers.",
    ),
    (
        "Empathogen Pollen",
        " once per day, release a cloud of empathogenic pollen. Biological creatures caught in the cloud must EGO save or become friendly and harmless for d6 rounds.",
    ),
    (
        "Soporific Pollen",
        " once per day, release a cloud of soporific pollen. Biological creatures caught in the cloud must EGO save or fall asleep for d6 rounds.",
    ),
    (
        "Neurotoxic Pollen",
        " once per day, release a cloud of neurotoxic pollen. Biological creatures caught in the cloud must CON save or be reduced to 1 HP.",
    ),
    (
        "Toxic Sap",
        " you emit one dose of a poisonous (d10 TOX) sap per day. Creatures who bite you or eat any part of your body must CON save vs a d10 TOX attack.",
    ),
    (
        "Vampiric Roots",
        " you can root yourself on Biological creatures, dealing d4 damage per round. You heal HP equal to the damage caused. The target must STR save to tear you off.",
    ),
    (
        "Luftpods",
        " you sprout pods full of lighter- than-air gas. You can fly in the air, slowly and predictably, and can act as a parachute to one other character.",
    ),
    (
        "Tesla Blossom",
        " spend two points of CON to grow a Tesla Blossom, which makes an extra ranged electrical attack (d6, ADV to hit Synthetic creatures) every combat round. CON loss cannot heal until you shed all Tesla Blossoms.",
    ),
    (
        "Seed Cannon",
        " spend two points of DEX to grow a Seed Cannon, which makes an extra ranged attack (d6) every combat round. DEX loss cannot heal until you shed all Seed Cannons.",
    ),
    (
        "Medicinal Fruit",
        " each day you sprout a golden fruit. It can be eaten as a food ration, healing d10 + CON bonus HP. Your maximum fruit cannot exceed your Level. You cannot eat your own fruit.",
    ),
    (
        "Sticky Sap",
        " you emit one dose of a glutinous sap per day. When spread on a surface, it acts as a strong contact glue. Creatures must STR save or be stuck fast to the surface. Saltwater dissolves the bond.",
    ),
    (
        "Sapling Retainers",
        " spend d4 points of CON to create an equal number of Sapling Retainers (<b>LVL 1, AV 12, ML +1, ATK D6</b>). They serve you for the rest of the day before withering.",
    ),
    (
        "Blast Pods",
        " each day you sprout an explosive pod (d10, blast). Your maximum pods cannot exceed your Level.",
    ),
    (
        "Grafting",
        " you may graft part of a Biological creature to your branches or trunk, gaining whatever extra attack or bonus is appropriate. For each day the grafted part stays alive, lose 1 point of CON.",
    ),
    (
        "Puppeteer Roots",
        " you may burrow your roots into the nervous system of a Biological creature. If the target fails an EGO save, you can control their movements. Damage taken by the controlled creature is split between both entities.",
    ),
)


@dataclass
class Bloomboon:
    name: str
    effect: str

    def __repr__(self):
        return f"<b>{self.name}</b>: {self.effect}"


@dataclass
class NeobloomLooks:
    shape: str
    leaves: str
    bark: str
    flowers: str

    def __repr__(self):
        return f"{self.shape} shape, {self.leaves} leaves, {self.bark} bark, flowers {self.flowers}."


def get_neobloom_looks():
    data = [choice(shape_leaves_bark_flowers_table)[k] for k in range(4)]
    return NeobloomLooks(*data)


@dataclass
class NeobloomDetails:
    manner: str
    voxpod: str
    quirk: str

    def __repr__(self):
        return f"{self.manner} manner, {self.voxpod} Vox-Pod, quirk: {self.quirk}"


special_rules_data = (
    (
        "Photosynthesis",
        "You regain d8 + CON HP for every hour you spend rooted in damp soil under the light of Urth’s sun. Artificial lighting does not suffice. If you do not photosynthesise for three days in a row, you will perish.",
    ),
    (
        "Flammable",
        "you take double damage from flames and heat-based attacks. Once hit, you suffer d8 burning damage per round until extinguished.",
    ),
    (
        "Bloomboons",
        "You begin play with one Bloomboon (already rolled above). When you gain a Level, you may choose to roll for a Boon instead of gaining HP and increasing your ability scores. If a repeat result is rolled, take the next Boon down.",
    ),
)


def get_neobloom_details():
    data = [choice(name_manner_vox_pod_quirk_table)[k] for k in range(1, 4)]
    return NeobloomDetails(*data)


def set_neobloom_name_and_details(char):
    names = [row[0] for row in name_manner_vox_pod_quirk_table]
    char.name = choice(names)
    char.details = get_neobloom_details()
    char.looks = get_neobloom_looks()
    bloomboon_name, bloomboon_effect = choice(bloomboons_data)
    bloomboon_effect = bloomboon_effect.strip().capitalize()
    char.bloomboon = Bloomboon(bloomboon_name, bloomboon_effect)
    char.special_rules = (SpecialRule(*data) for data in special_rules_data)


def get_bloomboons_list():
    return [
        Bloomboon(name, effect.strip().capitalize()) for name, effect in bloomboons_data
    ]
