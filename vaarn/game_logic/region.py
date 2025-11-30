from random import choice, randint
from .archive import gen_archive
from .anomaly import gen_anomaly
from .arcology import gen_arcology
from .bandit_camp import gen_bandit_camp
from .bounty_hunters_camp import gen_bounty_hunter_camp


locations_functions = {
    "Archive": gen_archive,
    "Anomaly": gen_anomaly,
    "Arcology": gen_arcology,
    "Bandit Camp": gen_bandit_camp,
    "Bounty Hunter's Camp": gen_bounty_hunter_camp,
}

location_types = tuple(locations_functions.keys())


def gen_region(size):
    locations = [choice(location_types) for _ in range(size)]
    return [(locations_functions[l](), l) for l in locations]


if __name__ == "__main__":
    print(gen_region(6))
