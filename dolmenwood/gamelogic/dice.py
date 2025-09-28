from random import randint
import re


def roll(dice):
    dice = dice.lower()
    pattern = r"(\+|\-)\d+"
    if re.search(pattern, dice):
        mod = re.search(pattern, dice).group(0)
    else:
        mod = None
    # cut out the modifier
    if mod:
        dice = dice.replace(mod, "")

    if dice[0].isdigit():
        n, size = dice.split("d")
        n = int(n)
        size = int(size)
    elif dice[0] == "d":
        size = int(dice[1:])
        n = 1
    result = 0
    for _ in range(n):
        result += randint(1, size)
    if mod:  # add in the modifier
        result = eval(str(result) + mod)
    return result


def get_key(n, d):
    """gets the nearest valid key in a dict with integer keys"""
    while n not in d:
        n += 1
    return n
