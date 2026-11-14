from dataclasses import dataclass


@dataclass
class Planet:
    name: str
    born_skill: str
    made_skill: str
    broken_skill: str
    special: str
    made_equipment: str
    broken_equipment: str


zig = Planet(
    "Ziggurat Works",
    "Aesthetics",
    "Creatures",
    "Delegation",
    "You can glean cryptic meaning from stone objects by touching them intensely.",
    "Nano Rifle (d10 erode, long) and machete (d6 pierce)",
    "Your leaving gift, a Void Plant (gradually kills all plants that share its soil)",
)


wolf_pit = Planet(
    "Wolf Pit",
    "Secrecy",
    "Networking",
    "Administration",
    "Your body accepts any replacement organs or limbs just by pushing them into place.",
    "Revolver (d8 pierce), booze printer (two strong drinks per hour)",
    "Cyber Critter (Electronics 12, Scuttering 7, 4Gd, d6 burn electro-bite)",
)

heap = Planet(
    "Heap",
    "Salvage",
    "Brokering",
    "Smuggling",
    "You can smell and identify most non-organic materials as if they were hot food.",
    "Cudgelgun (d6 crush, melee and ranged), pleasure spray (creates mild joy for a moment)",
    "Nano-veil (your face cannot be recalled by brain or machine, but appears otherwise normal)",
)
chime = Planet(
    "Chime Waters",
    "Flight",
    "Botany",
    "Aerial Vehicles",
    "You have retractable gossamer wings, capable of bumbling flight.",
    "Shardgun (2d8 infect, long), fertile slime (nourishes plants, refills if jar is left half full)",
    "Leather packet of red moss (grants vaguely prophetic dreams if consumed before sleep)",
)
labyrinth = Planet(
    "Labyrinth",
    "Traps",
    "Transport",
    "Pathfinding",
    "You are blue, rubbery and suffer no harm from extreme cold.",
    "Sack of ice picks (d8 pierce, long), breaker bombs (2d8 crush, blast)",
    "Vision pills (super-enhanced vision, lasts 1 hour, mild hallucinations afterwards)",
)
anvil = Planet(
    "Anvil",
    "Stamina",
    "Steady Hands",
    "Sales",
    "If you would ever count as having Armour 0, you have Armour 1 instead.",
    "Ultimate glue (can adhere any material with itself strongly and invisibly)",
    "Personal coffee printer (can produce one cup per hour, strong but bitter)",
)
PLANETS = [zig, wolf_pit, heap, chime, labyrinth, anvil]
