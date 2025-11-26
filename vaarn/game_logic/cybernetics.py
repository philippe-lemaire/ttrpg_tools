from random import choice
from dataclasses import dataclass


cybernetics = (
    (
        "Air Current Microsensor",
        "PSY",
        "You suffer no navigation or combat penalties from blindness or darkness.",
    ),
    (
        "Alluring Fakeface",
        "EGO",
        "You are extraordinarily beautiful. EGO save to enthrall a Biological creature. They will never harm you.",
    ),
    (
        "Autoglot HeadBank",
        "INT",
        "+2 to INT. You understand all languages.",
    ),
    (
        "Backup Heart",
        "CON",
        "+2 to CON. +5 max HP.",
    ),
    (
        "Carbide Knucklebones",
        "STR",
        "Your bare fists deal 2d4 damage.",
    ),
    (
        "Cyberliver",
        "CON",
        "You gain immunity to all poisons. You cannot get drunk",
    ),
    (
        "Dazzleskin Filaments",
        "CON",
        "You are immune to laser beams and energy weapons. DIS when hiding.",
    ),
    (
        "Dopamine Synthesizer",
        "EGO",
        "+2 to EGO. You are immune to fear, panic, and embarrassment.",
    ),
    (
        "Dorsal Jump-pack",
        "DEX",
        "You have hover-jets mounted on your back. You fly slowly and loudly.",
    ),
    (
        "Ferrosteel ExoSkeleton",
        "STR",
        "Add +2 to AV and STR. Subtract -4 DEX. You cannot swim.",
    ),
    (
        "Finger Syringe",
        "DEX",
        "One finger is a hidden injector. You can load it with any elixir or poison.",
    ),
    (
        "Hydraulic Biceps",
        "STR",
        "Add STR bonus to melee weapon damage.",
    ),
    (
        "Hyper-elastic Tendons",
        "DEX",
        "+2 to DEX. You can jump across huge distances like a frog.",
    ),
    (
        "Merciless Cybereyes",
        "DEX",
        "Add DEX bonus to ranged weapon damage.",
    ),
    (
        "Mercurial Fakeface",
        "EGO",
        "Your face can alter its features and colour at will.",
    ),
    (
        "Subdermal Ceramic Plating",
        "CON",
        "+2 to base AV. Cannot be removed.",
    ),
    (
        "Subdermal Insulation",
        "CON",
        "Immunity to damage from flames, cold, and electricity. Cannot be removed.",
    ),
    (
        "Tactical Bioscanner",
        "PSY",
        "You know the Level, AV, and current HP of any Biological or Fungal creature.",
    ),
    (
        "Tactical Technoscanner",
        "INT",
        "You know the Level, AV, and current HP of any Synthetic creature.",
    ),
    (
        "Trauma-Response Rig",
        "CON",
        "Negate the effects of a Wound. Can be activated once per day.",
    ),
)


@dataclass
class CyberneticImplant:
    name: str
    ability: str
    effect: str


def gen_cybernetic_implant():
    return CyberneticImplant(*choice(cybernetics))


def get_cybernetic_implants_list():
    return [CyberneticImplant(*data) for data in cybernetics]
