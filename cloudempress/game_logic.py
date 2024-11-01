from .unseen_city_tables import *

from .roll import roll_d10, roll
from random import choice


def get_byways(n):
    envs = set()
    byways = []
    for _ in range(n):
        tens = roll_d10()
        ones = roll_d10()
        environments = byway_environment.get(tens)
        if tens == ones or environments[0] in envs:
            environment = environments[1]
        else:
            environment = environments[0]
            envs.add(environment)
        if ones % 2 == 1:
            byways.append(f"{environment} Pitch dark.")
        else:
            # roll on illuminations
            illumination = choice(illuminations)
            byways.append(f"{environment} Illuminated by {illumination.lower()}")
    return byways


class Settlement:
    def __init__(self):
        self.size = choice(settlement_sizes)
        self.citizens = choice(settlement_citizens)
        self.leaders = choice(settlement_leaders)
        self.tech = choice(settlement_tech)
        self.sites_former_use = choice(settlement_sites_former_use)

    def __repr__(self):
        return f"A {self.size}. Citizen {self.citizens}. Leaders are {self.leaders}. Local tech is {self.tech}. The site used to be used for {self.sites_former_use}."


class Guild:
    def __init__(self):
        self.mostly = choice(guilds_mostly)
        self.map_quality = choice(guilds_map_quality)
        self.superstition = choice(guilds_superstition)
        self.job = choice(guilds_job)
        self.pay = choice(guilds_pay)

    def __repr__(self):
        return f"A Guild made mostly of {self.mostly}. Their map quality is {self.map_quality}. They have this weird superstition: {self.superstition}. They offer this job {self.job} and pay {self.pay}."


class Mystling:
    def __init__(self) -> None:
        self.size_and_shape = choice(mystling_size_and_shape)
        self.head = choice(mystling_head)
        self.features = choice(mystling_features)
        self.want = choice(mystling_want)
        self.have = choice(mystling_have)

    def __repr__(self) -> str:
        return f"A {self.size_and_shape} Mystling. Its head is {self.head}. Its features are {self.features}. It wants {self.want}. It has {self.have}."


class Cavern:
    def __init__(self, level=0) -> None:
        self.number = roll("d20") + level
        self.description = cavern_dict.get(self.number)

    def __repr__(self) -> str:
        return self.description


if __name__ == "__main__":
    s = Settlement()
    g = Guild()
    m = Mystling()
    print(s)
    print("")
    print(g)
    print("")
    print(m)
