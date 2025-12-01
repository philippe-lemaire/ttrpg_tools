from random import choice
from dataclasses import dataclass

faa_nomad_camp_data = (
    (
        "Stern Patriarch",
        "Meat",
        "Meat",
        "Angry",
    ),
    (
        "Stern Matriarch",
        "Dates",
        "Wine",
        "Scared",
    ),
    (
        "Council of Elders",
        "Olives",
        "Beer",
        "Mourning",
    ),
    (
        "Charismatic Visionary",
        "Cheese",
        "Salt",
        "Talkative",
    ),
    (
        "Wounded Old Warrior",
        "Weapons",
        "Weapons",
        "Sullen",
    ),
    (
        "Husband and Wife, arguing",
        "Hides",
        "Information",
        "Warlike",
    ),
    (
        "Husband and Wife, happy",
        "Precious Metal",
        "Shelter",
        "Contemplative",
    ),
    (
        "Young Hothead",
        "Machine Parts",
        "Slaves",
        "Pious",
    ),
    (
        "Drug-addled Oracle",
        "Medicine",
        "Escaped Prisoner",
        "Crazed",
    ),
    (
        "Sinister Slaver",
        "Spices",
        "Captured Bride",
        "Suspicious",
    ),
    (
        "Lecherous Patriarch",
        "Drugs",
        "Runaway Groom",
        "Cheerful",
    ),
    (
        "Lecherous Matriarch",
        "Spare Livestock",
        "Revenge: Other Faa",
        "Wary",
    ),
    (
        "Twin Brothers/Sisters",
        "Fabrics",
        "Revenge: Monster",
        "Overconfident",
    ),
    (
        "Blind Brothers/Sisters",
        "Fungus",
        "Revenge: Hegemony",
        "Argumentative",
    ),
    (
        "Skilled Worm-tamer",
        "Sugar",
        "Revenge: Bandits",
        "Proud",
    ),
    (
        "Frail Grandmother",
        "Cybernetics",
        "Missing Child",
        "Silent",
    ),
    (
        "Skilled Sharpshooter",
        "Tonics",
        "Medical Help",
        "Praying",
    ),
    (
        "Cruel Psychic",
        "Books",
        "Humiliate Other Faa",
        "Celebrating",
    ),
    (
        "Power Struggle",
        "Exotica",
        "To Party",
        "Drunken",
    ),
    (
        "Anarchy",
        "Water",
        "Water",
        "Boastful",
    ),
)

npc_a_options = (
    "Clan Leader",
    "Leader’s Spouse",
    "Leader’s Sibling",
    "Leader’s Respected Child",
    "Leader’s Contemptible Child",
    "Old, Frail Elder",
    "Cunning, Manipulative Elder",
    "Feared Old Warrior",
    "Young Warrior, with Something to Prove",
    "Widow of Previous Leader",
)

npc_b_options = (
    "Rival to Leader’s Authority",
    "Spouse of Rival to Leader",
    "Child of Rival to Leader",
    "Clan Member, Considered Foolish",
    "Clan Member, Considered Dangerous",
    "Clan Member, Injured in Battle",
    "Prisoner, Captured in Battle",
    "Cantankerous Storyteller",
    "Skilled Tracker",
    "Skilled Artisan",
)

sources_of_conflict = (
    "Envy (Property)",
    "Envy (Success)",
    "Love (Forbidden)",
    "Love (Unrequited)",
    "Love (Triangle)",
    "Unpaid Debts",
    "Boredom",
    "Honor",
    "Robbery",
    "Gossip",
    "Adultery",
    "Conspiracy",
    "Gluttony",
    "Mistaken Identity",
    "Wild, Baseless Accusations",
    "Addiction (Drink)",
    "Addiction (Narcotics)",
    "Wedding Plans",
    "Blackmail",
    "Murder",
)


@dataclass
class FaaNomadCamp:
    leader: str
    they_have: str
    they_want: str
    mood: str
    npc_a: str
    source_of_conflict: str
    npc_b: str

    def __repr__(self):
        return f"""
    They are lead by a {self.leader.lower()}.
    <br>
    They have {self.they_have.lower()} and they want {self.they_want.lower()}.
    Their mood is {self.mood.lower()}.
    <br><br>
    {self.npc_a.capitalize()} is in conflict with {self.npc_b.lower()} over {self.source_of_conflict.lower()}.
    """


def gen_faa_nomad_camp():
    data = [choice(faa_nomad_camp_data)[k] for k in range(4)]
    data.extend(
        [choice(npc_a_options), choice(sources_of_conflict), choice(npc_b_options)]
    )
    return FaaNomadCamp(*data)
