from random import choice
from dataclasses import dataclass

wreck_data = (
    (
        "Wind-barge",
        "Decrepit",
        "Spies",
        "Bandits",
    ),
    (
        "Auto-chariot",
        "Laser-seared",
        "Masks",
        "Sabotage",
    ),
    (
        "Dune Skuggy",
        "Burned",
        "Water",
        "Sandstorm",
    ),
    (
        "Armoured Crawler",
        "Corrupted",
        "Soldiers",
        "Fuel Ran Out",
    ),
    (
        "Stilt Strutter",
        "Sun Bleached",
        "Memory Crystals",
        "Landmines",
    ),
    (
        "Kite Wagon",
        "Rusted",
        "Guns",
        "Disease",
    ),
    (
        "Transport Zeppelin",
        "Shattered",
        "Slaves",
        "Warfare",
    ),
    (
        "Hegemony Ornithopter",
        "Cloven",
        "Coffee",
        "Faulty Machinery",
    ),
    (
        "Orbital Satellite",
        "Disintegrating",
        "Prisoners of War",
        "Simply Abandoned",
    ),
    (
        "Autarchy War Stalker",
        "Graffiti-coated",
        "Heretics",
        "Biotech Infestation",
    ),
    (
        "Water Prospectors’ Rig",
        "Riddled with Holes",
        "Wine",
        "Nanomachines",
    ),
    (
        "Autarch’s Pleasure Barge",
        "Skeletal",
        "Refugees",
        "Faa Nomad Ambush",
    ),
    (
        "Colossal Exosuit",
        "Shredded",
        "Fungus",
        "Cacklemaw Ambush",
    ),
    (
        "Ancient Submarine",
        "Inside Out",
        "Embryos",
        "Faulty Navigation",
    ),
    (
        "Ancient Warship",
        "Overgrown",
        "Lithling Seeds",
        "Drunk Driving",
    ),
    (
        "Ancient Steam Ferry",
        "Looted",
        "Bombs",
        "Incompetent Officers",
    ),
    (
        "Ancient Train",
        "Halfway Repaired",
        "Cyborg Parts",
        "Crew Mutiny",
    ),
    (
        "Ancient Fighter Jet",
        "Occupied",
        "Synths",
        "Attacked by Monster",
    ),
    (
        "Motile Home",
        "Surprisingly Intact",
        "Holy Relics",
        "EMP Blast",
    ),
    (
        "Pre-Collapse Spacecraft",
        "Some Features Work",
        "Exotica",
        "Orbital Weapon Strike",
    ),
)


@dataclass
class Wreck:
    vehicle: str
    condition: str
    cargo: str
    cause_of_crash: str

    def __repr__(self):
        return f"""{self.vehicle.capitalize()} carrying {self.cargo.lower()}.
        <br>
        Condition: {self.condition.lower()} because of {self.cause_of_crash.lower()}.
        """


def gen_wreck():
    data = [choice(wreck_data)[k] for k in range(4)]
    return Wreck(*data)
