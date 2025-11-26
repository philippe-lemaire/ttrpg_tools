from random import randint
from .follower import Follower, roll_ego


class Mercenary(Follower):
    pass


names = (
    "Ekateria",
    "Whiss",
    "Nevermont",
    "Clori",
    "Groak",
    "Ulfendrop",
    "Panaga",
    "Sunrine",
    "Lupe",
    "Mud",
    "Ratch",
    "Xharo",
    "Episgrasso",
    "Charity",
    "Aret",
    "Imehnit",
    "Lementer",
    "Vasildos",
    "Damatra",
    "Inthus",
    "Goosehilda",
    "Kanak",
    "Birksop",
    "Mannoch",
    "Croxley",
    "Nussof",
    "Uck",
    "Ricola",
    "Yarrange",
    "Vanise",
)

levels = [f"{k} ({4*k})" for k in range(2, 10)]

morale_scores = [f"+{k}" for k in range(5, 11)]

attacks = (
    "Jewelled Dagger (d6)",
    "Crystal Club (d6)",
    "Holy Flail (d6)",
    "Black War-Fan (d6)",
    "Quicksilver Sling (d6)",
    "Laspistol (d6, beam)",
    "Venomous Knife (d6 TOX)",
    "Chrome Revolver (d6 ranged)",
    "Nomad’s Rifle (d8 ranged)",
    "Nomad’s Mace (d8)",
    "Biomechanical Sword (d8)",
    "Ornate Lasrifle (d8, beam)",
    "Plasma Rapier (d8)",
    "Ritual Crossbow (d8)",
    "Fungal Spear (d8)",
    "Sky-Iron Greatsword (d10)",
    "Blasphemous Shotgun (d10) ",
    "Obsidian Trident (d10)",
    "Plasma Rifle (d10)",
    "Luminous War Hammer (d10)",
    "Grenade Launcher (d10 blast)",
    "Inferno Cannon (d10, fire)",
    "Heavy Lasgun (d10 beam)",
    "Tesla Cannon (d10 electrical, auto-hit Synth targets)",
    "Railgun (d12 ranged)",
    "Port-A-Cannon (d12 blast)",
    "Nano-edged Greatsword (2d10)",
    "Doom Gauntlets (d12)",
    "Annihilation Ray (d12, beam)",
    "Neon Hypersword (d12, hypergeometric)",
)

descriptions = (
    "Cacogen with vestigial feathered wings",
    "New-Wolf who wears a necklace of human teeth",
    "True-kin who wears a fearsome gilded mask",
    "Synth with chrome pyramid-shaped body",
    "Mycomorph with a glossy skull-like head",
    "Faa nomad with a long blue beard ",
    "Cacklemaw who wears a wedding dress",
    "Black haired true-kin, claims descent from an Autarch",
    "Warty cacogen with thermal vision",
    "Synth with a transparent, serpent-like body",
    "New-Gibbon who wears quicksilver rings",
    "Mycomorph with a pink veil-like head",
    "Cadaverous Faa nomad, always coughing",
    "Cacklemaw with blackened nubs for teeth",
    "True-kin with heavily burned face ",
    "Cacogen with powerful horse-like legs",
    "Synth which travels on tank-treads",
    "New-Wolf, committed vegetarian",
    "Mycomorph with poisonous peach-pink flesh",
    "Faa nomad with implanted night-vision lenses",
    "Cacklemaw with lustrous fur, always combing it",
    "Small true-kin with golden teeth",
    "Headless cacogen, four purple eyes on chest",
    "Synth with one cyclopean black eye",
    "New-Raven who wears funeral attire",
    "Mycomorph with a black, spiny body",
    "Faa nomad with a silver tongue",
    "Cacklemaw with a triple-row of teeth",
    "Planeywoman with luminous veins",
    "Tall orange Lithling (+4 AV)",
)


def gen_mercenary(ego):
    name = names[roll_ego(ego) - 1]
    level = levels[(roll_ego(ego) - 1) // 8]
    av = 10 + (roll_ego(ego) - 1) // 10
    morale = morale_scores[(roll_ego(ego) - 1) // 5]
    attack = attacks[roll_ego(ego) - 1]
    description = descriptions[roll_ego(ego) - 1]
    return Mercenary(name, level, av, morale, attack, description)
