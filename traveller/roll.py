from random import randint


def traveller_roll(boon=False, bane=False):
    if boon and bane:
        raise ValueError("Can't have boon and bane at the same time")
    dice = [randint(1, 6) for _ in range(2 + boon + bane)]
    dice.sort()
    if boon:  # drop lowest
        dice = dice[1:]
    if bane:  # drop highest
        dice = dice[0:2]
    return sum(dice)


def get_key(n, d):
    """gets the nearest valid key in a dict with integer keys"""
    while n not in d:
        n += 1
    return n
