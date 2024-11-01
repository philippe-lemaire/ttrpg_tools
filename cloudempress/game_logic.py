from .unseen_city_tables import *

from .roll import roll_d10, roll, get_key, roll_d100
from random import choice


class Byway:
    def __init__(self, environment, alternate_environment=None) -> None:
        self.environment = environment
        self.alternate_environment = alternate_environment


def roll_byway():
    tens = roll_d10()
    ones = roll_d10()
    environments = byway_environment.get(tens)
    if tens == ones:
        byway = Byway(environment=environments[0])
    else:
        byway = Byway(
            environment=environments[0], alternate_environment=environments[1]
        )
    if ones % 2 == 1:
        byway.illumination = "Pitch dark."
    else:
        # roll on illuminations
        byway.illumination = choice(illuminations)
    return byway


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
        self.z = roll("d20") + level
        self.description = cavern_dict.get(self.z)
        self.departing_byways = cavern_departing_byways.get(
            get_key(roll_d10(), cavern_departing_byways)
        )

    def __repr__(self) -> str:
        return self.description


def roll_mine():
    return choice(forgotten_mines)


def roll_exit():
    r = roll_d100()
    k = get_key(r, exits)
    return exits.get(k)


class Encounter:
    def __init__(self) -> None:
        r = roll_d100()
        k = get_key(r, encounter_table)
        self.kind = encounter_table.get(k)
        if r <= 25:
            self.attitude = None
        else:
            r = roll_d10()
            k = get_key(r, attitude_table)
            self.attitude = attitude_table.get(k)


if __name__ == "__main__":
    s = Settlement()
    g = Guild()
    m = Mystling()
    print(s)
    print("")
    print(g)
    print("")
    print(m)
