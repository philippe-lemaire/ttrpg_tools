from .unseen_city_tables import byway_environment, illuminations
from .roll import roll_d10
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
