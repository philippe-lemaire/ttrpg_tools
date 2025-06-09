from random import randint

eye = "👁️"
gandalf = "🧙‍♂️"


class FeatDie:

    def __init__(self):
        face_value = randint(1, 12)
        if face_value == 11:
            self.value = eye
        elif face_value == 12:
            self.value = gandalf
        else:
            self.value = face_value

    def __gt__(self, other):
        order = [eye]
        order.extend(list(range(1, 11)))
        order.append(gandalf)
        return order.index(self.value) >= order.index(other.value)

    def __repr__(self):
        return str(self.value)


class SuccessDie:
    def __init__(self):
        self.value = randint(1, 6)
        self.success = self.value == 6

    def __gt__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return str(self.value)


def roller(
    rating,
    target_number,
    favoured=False,
    ill_favoured=False,
    weary=False,
    miserable=False,
):
    feat_dice = [FeatDie()]
    success_dice = [SuccessDie() for d in range(int(rating))]
    if favoured ^ ill_favoured:
        feat_dice.append(FeatDie())
    # remove best FeatDie if ill_favoured
    if ill_favoured and not favoured:
        feat_dice.sort()
    if favoured and not ill_favoured:
        feat_dice.sort(reverse=True)

    # compute the final result
    total = feat_dice[0].value
    successes = sum(s.success for s in success_dice) + 1
    if total == eye:
        total = 0
        if miserable:
            return False, 0, total, feat_dice, success_dice
    elif total == gandalf:
        # skip the sum
        return (True, successes, total, feat_dice, success_dice)
    # compute the total value and check if TN is met
    if weary:
        total += sum(d.value for d in success_dice if d.value > 3)
    else:
        total += sum(d.value for d in success_dice)
    tn_met = total >= target_number
    successes = successes if tn_met else 0
    return tn_met, successes, total, feat_dice, success_dice


if __name__ == "__main__":
    print(
        roller(
            rating=2,
            favoured=False,
            ill_favoured=True,
            miserable=False,
            target_number=15,
            weary=True,
        )
    )
