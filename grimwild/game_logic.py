from random import randint


def grimwild_roll(dice, thorns):
    dice_result = [randint(1, 6) for _ in range(dice)]
    thorns_result = [randint(1, 8) for _ in range(thorns)]
    dice_result.sort()
    thorns_result.sort()
    outcomes = ["disaster", "grim", "messy", "perfect", "critical"]
    cuts = len([t for t in thorns_result if t >= 7])
    # check if critical
    if dice_result.count(6) >= 2:
        i = 4
    elif max(dice_result) == 6:
        i = 3 - cuts
    elif max(dice_result) in (4, 5):
        i = 2 - cuts
    else:
        i = 1 - cuts
    if i < 0:
        i = 0

    outcome = outcomes[i]
    return dice_result, thorns_result, outcome


def grimwild_pool(dice):
    dice_result = [randint(1, 6) for _ in range(dice)]
    dice_result.sort()
    outcome = len([d for d in dice_result if d > 3])
    return dice_result, outcome
