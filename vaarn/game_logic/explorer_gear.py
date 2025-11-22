from random import choice

gear_a = (
    "Flashbang (x5)",
    "Magnetic Boots",
    "Grappling Hook & Rope",
    "Flare (x5)",
    "Smoke Bomb (x5)",
    "Flask of Oil",
    "Portable Stove",
    "Caltrops (x5)",
    "Vial of Acid (x3)",
    "Animal Trap (x3)",
    "Handheld Drill",
    "Chain & Manacles",
    "Hand Mirror",
    "Motion Sensor",
    "Crowbar",
    "EMP Grenade (x3)",
    "Skin of Wine",
    "Tube of Glue (Ud8)",
    "Ball Bearings (Ud20)",
    "Glowstone",
)

gear_b = (
    "Sleeping Gas Bomb (x5)",
    "Oxygen Mask (Ud6)",
    "Cast Iron Skillet",
    "Black Clay (Ud8)",
    "Loaded Dice",
    "Raucous Whistle",
    "Luminous Paint (Ud8)",
    "Drug (consult p.xx)",
    "Poison Pill (d10 TOX)",
    "Autoglot Translator Unit",
    "Lock Picks",
    "Mortar & Pestle",
    "Strong Liquor",
    "Hourglass",
    "Hammer & Chisel",
    "Anti-venom (x3)",
    "Welding Torch (Ud8)",
    "Thermal Goggles",
    "Fungicide Bomb (x5)",
    "Canary in Cage",
)


def gen_gear():
    return [choice(gear_a), choice(gear_b)]
