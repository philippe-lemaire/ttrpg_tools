from random import choice
from dataclasses import dataclass


anomaly_data = (
    (
        "Dazzling",
        "Web",
        "Inverts Local Gravity",
        "Induces Paranoia",
    ),
    (
        "Nauseating",
        "Mist",
        "Heals Injuries",
        "Total Silence Nearby",
    ),
    (
        "Floating",
        "Cave",
        "Translates Languages",
        "Absorbs Light",
    ),
    (
        "Singing",
        "Tower",
        "Reanimates Dead",
        "Extreme Cold Nearby",
    ),
    (
        "Mist-like",
        "Lotus",
        "Merges Creatures Together",
        "Strange Music Audible",
    ),
    (
        "Glitching",
        "Tree",
        "Makes Prophecies",
        "Strange Voices Echo",
    ),
    (
        "Luminous",
        "Pool",
        "Other Universe Visible",
        "Localised Weather System",
    ),
    (
        "Radioactive",
        "Fountain",
        "Implants Memories",
        "Time Flows Strangely",
    ),
    (
        "Self-replicating",
        "Stone",
        "Implants Mystic Gifts",
        "Induces Mania",
    ),
    (
        "Quicksilver",
        "Skull",
        "Induces Amnesia",
        "Always Nighttime Nearby",
    ),
    (
        "Many-eyed",
        "Prism",
        "Induces Delusions",
        "Induces Mutations",
    ),
    (
        "Iridescent",
        "Cube",
        "Kills Indiscriminately",
        "Rusts All Metal",
    ),
    (
        "Toxic",
        "Pyramid",
        "Induces Empathy",
        "Exudes Lightning",
    ),
    (
        "Crystal",
        "Sphere",
        "Transforms Matter",
        "Exudes Flames",
    ),
    (
        "Speaking",
        "House",
        "Teleports Matter",
        "Exudes Toxins",
    ),
    (
        "Mobile",
        "Miasma",
        "Creates Planeyfolk",
        "Creates Solid Light",
    ),
    (
        "Blossoming",
        "Waterfall",
        "Creates Monsters",
        "Nanomachine Cloud",
    ),
    (
        "Burning",
        "Infant",
        "Grants Visions of Past",
        "Infection with Virus",
    ),
    (
        "Mesmerising",
        "Shell",
        "Grants Visions of Future",
        "Infection with Fungus",
    ),
    (
        "Terrifying",
        "Helix",
        "Makes Thoughts Solid",
        "Infection with Spirit",
    ),
)


@dataclass
class Anomaly:
    quality: str
    form: str
    primary_effect: str
    secondary_effect: str

    def __repr__(self):
        return f"{self.quality} {self.form}.<br>Primary effect {self.primary_effect}.<br>Secondary effect {self.secondary_effect}."


def gen_anomaly():
    data = (choice(anomaly_data)[k] for k in range(4))
    return Anomaly(*data)
