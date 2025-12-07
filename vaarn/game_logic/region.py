from random import choice, randint
from dataclasses import dataclass
from .archive import gen_archive
from .anomaly import gen_anomaly
from .arcology import gen_arcology
from .bandit_camp import gen_bandit_camp
from .bounty_hunters_camp import gen_bounty_hunter_camp
from .cacklemaw_den import gen_cacklemaw_den
from .faa_nomad_camp import gen_faa_nomad_camp
from .grave import gen_grave
from .hegemony_outpost import gen_hegemony_outpost
from .wreck import gen_wreck
from .holy_place import gen_holy_place
from .lair import gen_lair
from .landmark import gen_landmark
from .oasis import gen_oasis
from .ruin import gen_ruin
from .science_mystics_abode import gen_science_mystics_abode
from .trade_post import gen_trade_post


locations_functions = {
    "Archive": gen_archive,
    "Anomaly": gen_anomaly,
    "Arcology": gen_arcology,
    "Bandit Camp": gen_bandit_camp,
    "Bounty Hunter's Camp": gen_bounty_hunter_camp,
    "Cacklemaw Den": gen_cacklemaw_den,
    "Faa Nomad Camp": gen_faa_nomad_camp,
    "Grave": gen_grave,
    "Hegemony Outpost": gen_hegemony_outpost,
    "Holy Place": gen_holy_place,
    "Lair": gen_lair,
    "Landmark": gen_landmark,
    "Oasis": gen_oasis,
    "Ruin": gen_ruin,
    "Science Mystic’s Abode": gen_science_mystics_abode,
    "Trade Post": gen_trade_post,
    "Wreck": gen_wreck,
}

location_types = tuple(locations_functions.keys())
landscapes = (
    "Featureless Sands",
    "Salt Pan",
    "Hard Rocky Plain",
    "Dried-up Lake",
    "Dried-up River",
    "Towering Monoliths",
    "Mesas",
    "Low Hills",
    "Single Mountain",
    "Toxic Lake",
    "Toxic River",
    "Fungal Forest",
    "Crystal Growths",
    "Windswept Plateau",
    "Mountainous",
    "Winding Canyons",
    "Abandoned City",
    "Cactus Fields",
    "Riddled with Caves",
    "Garbage-strewn Wastes",
)

name_origins = (
    "Famous Resident",
    "Local Wildlife",
    "Natural Wonder",
    "Natural Hazard",
    "Famous Monster",
    "Long-Dead Settlement",
    "Forgotten Religion",
    "Local Weather",
    "Natural Resource",
    "Name No Longer Understood",
)


@dataclass
class Region:
    locations: list
    landscape: str
    named_for: str


def gen_region(size):
    locations = [choice(location_types) for _ in range(size)]
    landscape = choice(landscapes)
    named_for = choice(name_origins)
    return Region(
        locations=[(locations_functions[l](), l) for l in locations],
        landscape=landscape.lower(),
        named_for=named_for.lower(),
    )
