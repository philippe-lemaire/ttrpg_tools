from .tor_dice_roller import eye, gandalf, FeatDie
from gradientdescent.dice import get_key
from random import choice

solo_events = {
    eye: ["Terrible Misfortune", "If the roll fails, you are Wounded.", 3],
    1: ("Despair", "If the roll fails, gain 2 Shadow points (Dread).", 2),
    3: ("Ill Choices", "If the roll fails, gain 1 Shadow point (Dread).", 2),
    7: (
        "Mishap",
        "If the roll fails, add 1 day to the length of the journey, and gain 1 additional Fatigue.",
        2,
    ),
    9: (
        "Short Cut",
        "If the roll succeeds, reduce the length of the journey by 1 day.",
        1,
    ),
    10: (
        "Chance-­meeting",
        "If the roll succeeds, no Fatigue is gained, and you may improvise an encounter favouring your Player-­hero.",
        1,
    ),
    gandalf: ("Joyful Sight", "If the roll succeeds regain 1 Hope.", 0),
}

terrible_misfortunes = [
    (
        "Dire confrontation",
        "Noteworthy Encounter",
    ),
    (
        "Rival Predator",
        "HUNTING to avoid becoming the hunted",
    ),
    (
        "Violent weather",
        "EXPLORE to find shelter",
    ),
    (
        "Hidden hazard",
        "AWARENESS to avoid stumbling into danger",
    ),
    (
        "Dangerous terrain",
        "EXPLORE to find a safer route",
    ),
    (
        "Stalking enemy",
        "AWARENESS to spot the foul presence",
    ),
]


def roll_journey_event(die):
    k = get_key(die.value, solo_events)
    event = solo_events.get(k)
    if k == eye:
        misfortune = choice(terrible_misfortunes)
        event[0] = f"{event[0]}: {misfortune[0]}"
        event[1] = f"{misfortune[1]}.<br>{event[1]}"
    return k, event
