from .roll import roll
from dataclasses import dataclass


@dataclass
class Event:
    kind: str
    description: str


dungeon_events_data = (
    (
        "Encounter",
        "Roll on an encounter table. Possibly hostile. (See Reactions (pg. 63).)",
    ),
    ("Sign", "A clue, spoor, track, abandoned lair, scent, victim, etc isdiscovered."),
    (
        "Environment",
        "Surroundings shift or escalate. Water rises, ceilings collapse, a ritual nears completion, etc.",
    ),
    (
        "Loss",
        "Torches are blown out, an ongoing spell fizzles, etc. The party must resolve the effects before moving on.",
    ),
    (
        "Exhaustion",
        "The party must take a brief rest (roll on this table again), add a Fatigue, or consume a ration.",
    ),
    ("Quiet", "The party is left alone (and safe) for the time being."),
)

dungeon_events = {k: Event(t, d) for (k, (t, d)) in enumerate(dungeon_events_data, 1)}
