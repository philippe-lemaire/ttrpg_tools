from .tor_dice_roller import eye, gandalf, FeatDie
from gradientdescent.dice import get_key
from random import choice

targets_table = {
    2: ("Scouts", "EXPLORE"),
    4: ("Look-outs", "AWARENESS"),
    6: ("Hunters", "HUNTING"),
}

terrible_misfortune = (
    "Terrible Misfortune",
    "If the roll fails, the target is Wounded.",
    3,
)
despair = (
    "Despair",
    "If the roll fails, everyone in the Company gains 1 Shadow point (Dread).",
    2,
)
ill_choices = (
    "Ill Choices",
    "If the roll fails, the target gains 1 Shadow point (Dread).",
    2,
)
mishap = (
    "Mishap",
    "If the roll fails, add 1 day to the length of the journey, and the target gets 1 additional fatigue.",
    2,
)
shortcut = (
    "Shortcut",
    "If the roll succeeds, reduce the length of the journey by 1 day.",
    1,
)
chance_meeting = (
    "Chance-meeting",
    "If the roll succeeds, no Fatigue is gained, and the Loremaster improvises an encounter favouring the Company.",
    1,
)
joyful_sight = (
    "Joyful Sight",
    "If the roll succeeds, everyone in the Company regains 1 Hope.",
    "–",
)

journey_events_table = {
    eye: terrible_misfortune,
    1: despair,
    3: ill_choices,
    7: mishap,
    9: shortcut,
    10: chance_meeting,
    gandalf: joyful_sight,
}


class JourneyEvent:
    def __init__(self, success_die, feat_die):
        k = get_key(success_die.value, targets_table)
        self.target, self.skill = targets_table.get(k)
        event_row = journey_events_table.get(
            get_key(feat_die.value, journey_events_table)
        )
        self.name = event_row[0]
        self.description = event_row[1]
        self.fatigue_gained = event_row[2]
