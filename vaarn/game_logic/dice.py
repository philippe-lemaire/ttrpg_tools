from random import randint


def roll_stat():
    """Roll stats for Vaarn characters: roll 3d6 and take the lowest as the stats’s bonus"""
    return min(randint(1, 6) for _ in range(3))
