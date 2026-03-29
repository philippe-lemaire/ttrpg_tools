import random


def roll(dice):
    """Ex usage roll('3d6+1') -> random number between 3 and 18."""
    error_message = "Invalid argument. Please use a string such as '2d20' or '3d6'"
    dice = dice.lower()
    if "d" not in dice:
        raise ValueError(error_message)
    if dice.startswith("d"):
        n = 1
        dice_type = int(dice.split("d")[1])
    else:
        n, dice_type = dice.split("d")
        n = int(n)
        dice_type = int(dice_type)

    rolls = [random.randint(1, dice_type) for _ in range(n)]

    return sum(rolls)


def get_closest_key(rolled_value, d):
    "Returns the closest value in a table based on a rolled value"
    for key in d.keys():
        if key >= rolled_value:
            return key
    # if we get there, the roll + modifiers exceed the highest key in the table, so return the highest key
    return max(list(d.keys()))
