from random import choice
from dataclasses import dataclass

science_mystic_data = (
    (
        "Secluded",
        "Cloaked, Masked, Decaying",
        "Immortality",
    ),
    (
        "Armoured",
        "Booming Voice, Tiny Body",
        "Telepathy",
    ),
    (
        "Vine-choked",
        "Sallow and Smelly",
        "Mind Control",
    ),
    (
        "Dark",
        "Dazzlingly Beautiful",
        "Antigravity Field",
    ),
    (
        "Spiralling",
        "Plastic-fleshed Synth",
        "Time Stasis",
    ),
    (
        "Sentient",
        "Double-faced Cacogen",
        "Time Travel",
    ),
    (
        "Wheeled",
        "Ostentatious New-Tiger",
        "Time Paradox",
    ),
    (
        "Transparent",
        "Permanently Invisible",
        "Hypergeometry",
    ),
    (
        "Crystalline",
        "Brain in a Vat",
        "Synthetic Anatomy",
    ),
    (
        "Sword-like",
        "Levitating Idiot",
        "Synthetic Psychology",
    ),
    (
        "Towering",
        "Terrified of their Reflection",
        "Newbeast Biology",
    ),
    (
        "Severe",
        "Flesh-eating Mycomorph",
        "Newbeast Psychology",
    ),
    (
        "Decadent",
        "Extra Arms Grafted On Back",
        "Mycomorph Biology",
    ),
    (
        "Buried",
        "Neurotic New-Lynx",
        "Mycomorph Psychology",
    ),
    (
        "Overgrown",
        "Stuttering Synth",
        "Language Virus",
    ),
    (
        "Elegant",
        "Bashful Murderer",
        "Teleportation",
    ),
    (
        "Devotional",
        "Icily Polite",
        "Titancreed Syntax",
    ),
    (
        "Pyramid",
        "Blood-drinking Cacogen",
        "Ancient Super-weapon",
    ),
    (
        "Deceptively Normal",
        "Way Too Friendly",
        "Contact Azathoth",
    ),
    (
        "Glows in the Dark",
        "Voice from an Orb",
        "Space Travel",
    ),
)

wants = (
    "'Volunteers' for Experimentation",
    "To Hire A New Assistant; Don’t Ask About the Old One",
    "To Dispose of a Rogue Creation",
    "A Fabled Chemical Substance; Found In Nearby Ruin",
    "A Fabled Artefact; Said to be Held by a Faa Nomad Clan",
    "Body Parts of Local Monster",
    "Revenge on Ex-Assistant; They Stole Research",
    "An Armed Escort To Explore A Distant Vault",
    "An Armed Escort to Accompany Them to Gnomon",
    "Assistance With An Obviously Dangerous Experiment",
)


@dataclass
class ScienceMysticsAbode:
    abode: str
    the_mystic: str
    researching: str
    they_want: str

    def __repr__(self):
        return f"""{self.abode.capitalize()} abode. {self.the_mystic.capitalize()} researching {self.researching.lower()}.
        <br>
        They want {self.they_want.lower()}.
        """


def gen_science_mystics_abode():
    data = [choice(science_mystic_data)[k] for k in range(3)]
    data.append(choice(wants))
    return ScienceMysticsAbode(*data)
