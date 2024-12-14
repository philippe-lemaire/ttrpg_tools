from random import randint
import re


def roll(dice):
    dice = dice.lower()
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
    return result


def roll_d100():
    return randint(0, 99)


def check_doubles(n):
    if n < 10:
        d1, d2 = "0", str(n)
    else:
        d1, d2 = str(n)[0], str(n)[1]

    return d1 == d2


def doubles_value(n):
    if not check_doubles(n):
        raise ValueError(f'{n} is not a valid "double digits" result.')
    return n % 10


def roll_d10():
    return roll("1d10")


def get_key(n, d):
    """gets the nearest valid key in a dict with integer keys"""
    if n > max(list(d.keys())[1:]):
        raise KeyError(f"{n} is higher than all the keys in {d}.")
    while n not in d:
        n += 1
    return n


def get_reaction():
    roll = roll_d100()
    double = check_doubles(roll)
    positives = ("Positive", "Friendly")
    negatives = ("Negative", "Hostile")
    if roll % 2 == 0:  # even case
        return positives[double], roll
    return negatives[double], roll


def roll_encounter_numbers(s):
    pattern = r"\d{1,2}d\d{1,2}"
    search = re.search(pattern, s)
    if search:
        to_roll = search.group(0)
        number = roll(to_roll)
        return re.sub(pattern, repl=str(number), string=s)
    return s


def roll_pc_stats_and_saves():
    stats_and_saves = {
        "strength": roll("2d10") + 25,
        "speed": roll("2d10") + 25,
        "intellect": roll("2d10") + 25,
        "combat": roll("2d10") + 25,
        # second, roll saves
        "sanity": roll("2d10") + 10,
        "fear": roll("2d10") + 10,
        "body": roll("2d10") + 10,
    }
    return stats_and_saves
