from random import choice, randint
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
    "Wreck": gen_wreck,
}

location_types = tuple(locations_functions.keys())


def gen_region(size):
    locations = [choice(location_types) for _ in range(size)]
    return [(locations_functions[l](), l) for l in locations]
