from random import choice
from dataclasses import dataclass

bounty_hunter_camp_data = (
    (
        "Grim and Scarred",
        "Heretic",
        "Patient Stalker",
    ),
    (
        "Avuncular and Evil",
        "Bandit King",
        "Guns Blazing",
    ),
    (
        "Psychotic Synth",
        "Murderer",
        "Use Poison",
    ),
    (
        "Three-headed Cacogen",
        "Conman",
        "Use Gas",
    ),
    (
        "One-Eyed New-Wolf",
        "Water Debtor",
        "Elaborate Disguises",
    ),
    (
        "Remote-Controlled Armour",
        "Gambling Debtor",
        "Sniper Rifle",
    ),
    (
        "Young and Beautiful",
        "Livestock Thief",
        "Tranquilliser Crossbow",
    ),
    (
        "Depressed Drunkard",
        "Adulterer",
        "Shoot First",
    ),
    (
        "Husband and Wife Team",
        "Rogue Synth",
        "Alluring Honey Trap",
    ),
    (
        "Looks Way Too Young",
        "Cacklemaw Exile",
        "Enlist Big Posse",
    ),
    (
        "Clean Cut and Heroic",
        "Faa Nomads",
        "Bribes for Information",
    ),
    (
        "Dashing Womaniser",
        "Water Token Forger",
        "Reliable Informants",
    ),
    (
        "Flamboyant Old Woman",
        "Poisoner",
        "Trained Monster",
    ),
    (
        "Clone Siblings",
        "Child Killer",
        "Quiet Abductions",
    ),
    (
        "New-Baboon, Riding Human",
        "Oath Breaker",
        "Secret Martial Art",
    ),
    (
        "Veteran Soldier",
        "Runaway Bride",
        "Psychic Gifts",
    ),
    (
        "Famous Exile",
        "Runaway Groom",
        "Expert Desert Tracker",
    ),
    (
        "Sacred Assassin",
        "Disgraced Cleric",
        "Use Camera Drones",
    ),
    (
        "Faa Nomad Tracker",
        "Hegemony Deserter",
        "Utterly Incompetent",
    ),
    (
        "Psychic Mute",
        "Own Family Member",
        "Absurd Traps",
    ),
)

wants = (
    "A Lead on their Quarry",
    "Help Killing Dangerous Quarry",
    "Help Catching Dangerous Quarry Alive",
    "Help Killing Someone You Know",
    "Help Bringing Prisoner to Distant Settlement ",
    "Help Bringing Prisoner To Distant Arcology ",
    "Help Bringing Prisoner To Faa Nomads",
    "Help Capturing Science-Mystic Alive",
    "Help Killing Dangerous Monster",
    "Help Escorting Prisoner to Gnomon",
)


@dataclass
class BountyHunterCamp:
    the_hunter: str
    chasing: str
    their_methods: str
    they_want: str

    def __repr__(self):
        return f"""{self.the_hunter.capitalize()} bounty hunter, chasing {self.chasing}.
    Their method: {self.their_methods.lower()}.
    <br><br>
    They want {self.they_want.lower()}.
    """


def gen_bounty_hunter_camp():
    data = [choice(bounty_hunter_camp_data)[k] for k in range(3)]
    data.append(choice(wants))
    return BountyHunterCamp(*data)
