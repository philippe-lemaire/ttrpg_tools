from random import choice
from dataclasses import dataclass

ruin_data = ()
original_purposes = (
    "Interrogation Halls",
    "Cryogenic Chambers",
    "Orbital Defence Turret",
    "Cyborg Construction",
    "Munitions Factory",
    "Cloning Facility",
    "University",
    "Nanotech Forge",
    "Power Generator",
    "Noble’s Residence",
    "Autarch’s Tomb",
    "Chemical Plant",
    "Psychic Training Facility",
    "Pleasure Garden",
    "Transit Hub",
    "Farm Array",
    "Bioengineering Facility",
    "Medical Facility",
    "Communications Array",
    "Prison",
)

following_purpose = (
    "Brewery",
    "Criminal’s Hideout",
    "Bath House",
    "Ossuary",
    "Monastery",
    "Barracks",
    "Brothel",
    "Inn",
    "Theatre",
    "Gladiator Pit",
    "Madhouse",
    "Observatory",
    "Mystic’s Abode",
    "Titan Cult Shrine",
    "Hydroponic Garden",
    "Battle Site",
    "Quantum Daemon Shrine",
    "Trading Post",
    "Slaughterhouse",
    "Space Port",
)
current_purposes = (
    "Desolate Shell",
    "Intact But Empty",
    "Faa Nomad Campsite",
    "Hideout for Bandits",
    "Cacklemaw Den",
    "Hegemony Outpost",
    "Monster Lair",
    "Science-Mystic’s Abode",
    "Grave Site",
    "Holy Place",
)
appearances = (
    "Opulent",
    "Fragmented",
    "Looming",
    "Crumbling",
    "Graffiti-Coated",
    "Gigantic",
    "Translucent",
    "Bat-Infested",
    "Sunbleached",
    "Half-Collapsed",
    "Threatening",
    "Crooked",
    "Towering",
    "Monolithic",
    "Dazzling",
    "Decrepit",
    "Sand-scoured",
    "Ill-Omened",
    "Beautiful",
    "Molten",
)
shapes = (
    "Dome",
    "Arch",
    "Tower",
    "Orb",
    "Shell",
    "Knife",
    "Bottle",
    "Flower",
    "Hand",
    "Eye",
    "Head",
    "Pyramid",
    "Slab",
    "Prism",
    "Cube",
    "Wheel",
    "Needle",
    "Torus",
    "Bowl",
    "Ziggurat",
)
features = (
    "Inhabited by Planeyfolk",
    "Choked with Synthetic Vines",
    "Has Hidden Water Source",
    "Has Abundant Food Source",
    "Has Abundant Drugs",
    "Contains Exotica",
    "Secret Surivival Cache",
    "Contains Wild Animal Nest",
    "Used for Sacrifices",
    "Ancient Defense Systems Active",
    "Upsetting Decorations",
    "Swallowed by the Sands",
    "Fire Damaged",
    "Radiation Poisoned",
    "Servitor Synths Still Function",
    "Crashed Vehicle Present",
    "Encrusted with Crystals",
    "Overgrown with Fungus",
    "Hypergeometric Portal Inside",
    "Conceals Long-Buried Threat",
)


@dataclass
class Ruin:
    what_was_it: str
    and_then: str
    and_now: str
    appearance: str
    shape: str
    other_feature: str

    def __repr__(self):
        return f"""{self.what_was_it.capitalize()} turned into a {self.and_then.lower()}, it is now a {self.and_now.lower()}.
        <br>
        It looks like a {self.appearance.lower()} {self.shape.lower()}.<br>
        Other feature: {self.other_feature.lower()}
        """


def gen_ruin():
    what = choice(original_purposes)
    then = choice(following_purpose)
    now = choice(current_purposes)
    appearance = choice(appearances)
    shape = choice(shapes)
    feature = choice(features)
    return Ruin(
        what_was_it=what,
        and_then=then,
        and_now=now,
        appearance=appearance,
        shape=shape,
        other_feature=feature,
    )
