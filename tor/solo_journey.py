from .tor_dice_roller import eye, gandalf, FeatDie
from gradientdescent.dice import get_key
from random import choice

solo_events = {
    eye: ["Terrible Misfortune", "If the roll fails, you are Wounded.", 3],
    1: ["Despair", "If the roll fails, gain 2 Shadow points [Dread).", 2],
    3: ["Ill Choices", "If the roll fails, gain 1 Shadow point [Dread).", 2],
    7: [
        "Mishap",
        "If the roll fails, add 1 day to the length of the journey, and gain 1 additional Fatigue.",
        2,
    ],
    9: [
        "Short Cut",
        "If the roll succeeds, reduce the length of the journey by 1 day.",
        1,
    ],
    10: [
        "Chance-­meeting",
        "If the roll succeeds, no Fatigue is gained, and you may improvise an encounter favouring your Player-­hero.",
        1,
    ],
    gandalf: ["Joyful Sight", "If the roll succeeds regain 1 Hope.", 0],
}

terrible_misfortunes = [
    (
        "Dire confrontation",
        "Noteworthy Encounter",
    ),
    (
        "Rival Predator",
        "<b>HUNTING</b> to avoid becoming the hunted",
    ),
    (
        "Violent weather",
        "<b>EXPLORE</b> to find shelter",
    ),
    (
        "Hidden hazard",
        "<b>AWARENESS</b> to avoid stumbling into danger",
    ),
    (
        "Dangerous terrain",
        "<b>EXPLORE</b> to find a safer route",
    ),
    (
        "Stalking enemy",
        "<b>AWARENESS</b> to spot the foul presence",
    ),
]

despair_details = [
    ("Servants of the Enemy", "Noteworthy Encounter"),
    (
        "Torrential weather",
        "<b>EXPLORE</b> to find the least exposed path",
    ),
    (
        "Nightmarish presence",
        "<b>AWARENESS</b> to sense the danger",
    ),
    (
        "Fading vigour",
        "<b>HUNTING</b> to gain sustenance",
    ),
    (
        "Corrupted site",
        "<b>EXPLORE</b> to find your way out",
    ),
    (
        "Grisly scene or fore-boding portent",
        "<b>AWARENESS</b> to be forewarned",
    ),
]

ill_choices_details = [
    (
        "Mismanaged",
        "<b>HUNTING</b> to replenish provisions stores",
    ),
    (
        "Wayward path",
        "<b>EXPLORE</b> to retrace your steps",
    ),
    (
        "Overlooked hazard",
        "<b>AWARENESS</b> to escape safely",
    ),
    (
        "Lost quarry",
        "<b>HUNTING</b> to follow its tracks",
    ),
    (
        "Disorienting environs",
        "<b>EXPLORE</b> to find your way",
    ),
    (
        "Haunting visions",
        "<b>AWARENESS</b> to overcome darkness",
    ),
]

mishap_details = [
    (
        "Sparse wildlife",
        "<b>HUNTING</b> to forage what you can",
    ),
    (
        "Lost direction",
        "<b>EXPLORE</b> to find your way",
    ),
    (
        "Obstructed path",
        "<b>AWARENESS</b> to spot a way around",
    ),
    (
        "Elusive quarry",
        "<b>HUNTING</b> to track it down",
    ),
    (
        "Rough terrain",
        "<b>EXPLORE</b> to safely traverse",
    ),
    (
        "Wandering enemies",
        "<b>AWARENESS</b> to sense their coming",
    ),
]

shortcut_details = [
    (
        "Game trail",
        "<b>HUNTING</b> to traverse the path",
    ),
    (
        "Secluded path",
        "<b>EXPLORE</b> to navigate the wilds",
    ),
    (
        "Helpful tracks",
        "<b>AWARENESS</b> to follow the tracks",
    ),
    (
        "Animal guide",
        "<b>HUNTING</b> to follow at a distance",
    ),
    (
        "Favourable weather",
        "<b>EXPLORE</b> to make the most of it",
    ),
    (
        "Familiar waypoint",
        "<b>AWARENESS</b> to recognize the landmark",
    ),
]

chance_meeting_details = [
    (
        "Lone hunter",
        "<b>HUNTING</b> to trade stories",
    ),
    (
        "Fellow traveller",
        "<b>EXPLORE</b> to learn about the path ahead",
    ),
    (
        "Discreet watcher",
        "<b>AWARENESS</b> to spot them",
    ),
    (
        "Noble beast",
        "<b>HUNTING</b> to commune",
    ),
    (
        "Secluded encampment ",
        "<b>EXPLORE</b> to find your way off the beaten path",
    ),
    (
        "Auspicious gathering",
        "Noteworthy Encounter",
    ),
]

joyful_sight_details = [
    (
        "Majestic creatures",
        "<b>HUNTING</b> to observe without startling them",
    ),
    (
        "Inspiring vista",
        "<b>EXPLORE</b> to reach a vantage point",
    ),
    (
        "Benevolent being",
        "<b>AWARENESS</b> to sense their presence",
    ),
    (
        "Abundant foraging",
        "<b>HUNTING</b> to replenish your rations",
    ),
    (
        "Ancient monument",
        "<b>AWARENESS</b> to recognize its significance",
    ),
    (
        "Peaceful sanctuary",
        "Noteworthy Encounter",
    ),
]

details_table = {
    eye: terrible_misfortunes,
    1: despair_details,
    3: ill_choices_details,
    7: mishap_details,
    9: shortcut_details,
    10: chance_meeting_details,
    gandalf: joyful_sight_details,
}


def roll_journey_event(die):
    k = get_key(die.value, solo_events)
    event = solo_events.get(k)
    detail = choice(details_table.get(k))
    outcome = detail[1]
    event[0] = f"{event[0]}: {detail[0]}"

    return k, event, outcome
