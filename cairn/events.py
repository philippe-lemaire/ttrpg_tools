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
    ("Sign", "A clue, spoor, track, abandoned lair, scent, victim, etc is discovered."),
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

wilderness_events_data = (
    (
        "Encounter",
        "Roll on an encounter table for that terrain type or location.  Don’t forget to roll for NPC reactions if applicable.",
    ),
    (
        "Sign",
        "The party discovers a clue, spoor, or indication of a nearby encounter, locality, hidden feature, or information about a nearby area.",
    ),
    (
        "Environment",
        "A shift in weather or terrain.",
    ),
    (
        "Loss",
        "The party is faced with a choice that costs them a resource (rations, tools, etc), time, or effort.",
    ),
    (
        "Exhaustion",
        "The party encounters a barrier, forcing effort, care or delays.  This might mean spending extra time (and an additional Wilderness Action) or adding Fatigue to the PC’s inventory to represent their difficulties.",
    ),
    (
        "Discovery",
        "The party finds food, treasure, or other useful resources.  The Warden can instead choose to reveal the primary feature of the area.",
    ),
)


wilderness_events = {
    k: Event(t, d) for (k, (t, d)) in enumerate(wilderness_events_data, 1)
}
