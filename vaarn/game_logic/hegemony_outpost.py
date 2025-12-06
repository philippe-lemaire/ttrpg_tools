from random import choice
from dataclasses import dataclass

unit_types = (
    "Deserters (d6)",
    "Deserters (d6)",
    "Scouts (d6)",
    "Scouts (d6)",
    "Scouts (d6)",
    "Scouts (d6)",
    "Rangers (d8)",
    "Rangers (d8)",
    "Rangers (d8)",
    "Rangers (d8)",
    "Synth-Hunting Team (d8)",
    "Synth-Hunting Team (d8)",
    "Synth-Hunting Team (d8)",
    "Synth-Hunting Team (d8)",
    "Legionaries (d20)",
    "Legionaries (d20)",
    "Legionaries (d20)",
    "Legionaries (d20)",
    "Artillery Unit (d8)",
    "Artillery Unit (d8)",
)


commander_status = (
    "Dead",
    "Missing",
    "Dying",
    "Wounded",
    "Weirdly Optimistic",
    "Raving Mad",
    "Incompetent",
    "Wavering",
    "Stern",
    "Grim",
    "Steady",
    "Measured",
    "Shrewd",
    "Bloodthirsty",
    "Cold",
    "Competent",
    "Loathed",
    "Respected",
    "Alert",
    "Beloved",
)

moods = (
    "Panicked",
    "Surly",
    "Mutinous",
    "Stressed",
    "Downcast",
    "Sleepy",
    "Lazy",
    "Paranoid",
    "Stoic",
    "Deranged",
    "Furious",
    "Hopeful",
    "Optimistic",
    "Celebratory",
    "Suspicious",
    "Bored",
    "Generous",
    "Drunken",
    "Overconfident",
    "Mournful",
)

activities = (
    "Treating Wounds",
    "Preparing for Combat",
    "Cleaning Campsite",
    "Cooking",
    "Weapons Drill",
    "Repairing Gear",
    "Troop Inspection",
    "Burying Dead",
    "Waiting for Orders",
    "Gambling",
    "Sleeping",
    "Feeding Prisoners",
    "Hunting Wildlife",
    "Executing Prisoners",
    "Searching for Water",
    "Combat With Monster",
    "Combat With Faa",
    "Combat With Cacklemaw",
)


@dataclass
class HegemonyOutpost:
    unit_type: str
    commander: str
    mood: str
    activity: str

    def __repr__(self):
        return f"""{self.unit_type}, their commander is {self.commander.lower()}.
        <br>
        They’re in a {self.mood.lower()} mood, busy with {self.activity.lower()}.
        """


def gen_hegemony_outpost():
    unit_type = choice(unit_types)
    commander = choice(commander_status)
    mood = choice(moods)
    activity = choice(activities)
    return HegemonyOutpost(unit_type, commander, mood, activity)
