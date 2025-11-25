from random import choice, randint
from dataclasses import dataclass


@dataclass
class Follower:
    name: str
    level: str
    av: int
    morale: str
    attack: str
    description: str


names = (
    "Herta",
    "Kinmoon",
    "Ophinus",
    "Wellet",
    "Roscar",
    "Antfancy",
    "Lusaki",
    "Scula",
    "Caleon",
    "Teleo",
    "Abrax",
    "Greyoul",
    "Bluebliss",
    "Greeze",
    "Henex",
    "Longdream",
    "Chattan",
    "Xaphor",
    "Naigallow",
    "Willing",
    "Aalder",
    "Daeros",
    "Erken",
    "Goldwin",
    "Patina",
    "Magdan",
    "Khawari",
    "Yarsan",
    "Cheontra",
    "Audrew",
)

levels = ("0 (1 HP)", "1 (4 HP)", "2 (8 HP)", "3 (12 HP)")

morale_scores = [f"+{k}" for k in range(6)]

attacks = (
    "Rolling Pin (d4)",
    "Bookbinder’s Awl (d4)",
    "Sling (d4)",
    "Heavy Stick (d4)",
    "Dried Cactus in Sock (d4)",
    "Dart Gun (d4)",
    "Gardener’s Trowel (d4)",
    "Bag of Worthless Coins (d4)",
    "Leather Belt (d4)",
    "Screwdriver (d4)",
    "Blunt Training Sword (d4)",
    "Broken Trumpet (d4)",
    "Hypodermic Needle (d4)",
    "Rusted Dagger (d4)",
    "Carpenter’s Saw (d4)",
    "Old Revolver (d6)",
    "Ancestral Sword (d6)",
    "Shepherd’s Staff (d6)",
    "Axe (d6)",
    "Wooden Club (d6)",
    "Sharp Crystal (d6)",
    "Whip (d6)",
    "Bow (d6)",
    "Volt Baton (d6, electrical)",
    "Pick Axe (d6)",
    "Shovel (d6)",
    "Hammer (d6)",
    "Nomad’s Rifle (d8)",
    "3 Ancient Grenades (d8, blast, 50% chance won’t detonate)",
    "Lasrifle (d8, beam)",
)
descriptions = (
    "Elderly New-Falcon who wears a glitching video-mask",
    "Aged Mycomorph with a brittle, spiny body",
    "True-kin with virulent facial rash",
    "Cacogen with long flexible limbs",
    "Synth with barrel-shaped body, leaks pink ichor",
    "Cacogen with broad yellow leaves for hair",
    "Mycomorph with enormous damp black head",
    "True-kin with braided hair and one missing eye",
    "New-Cat who wears a mirrored mask",
    "Synth with a rusting falcon-shaped body",
    "Cacogen with short blunt horns",
    "Corpulent true-kin with crimson eyes",
    "New-Toad with cheap cybernetic limbs",
    "Boxy synth with a missing head",
    "Mycomorph with soft, apricot-coloured flesh",
    "True-kin with a tiny body and hunched back",
    "New-Anenome with a sorrowful crone mask",
    "Cacogen with five legs",
    "Synth with a silver child-like body",
    "Glowering true-kin who wears plastic clothes",
    "Cacogen with a prehensile beard",
    "New-Addax with ritual scars",
    "Mycomorph with an eyeless crimson head",
    "Synth with an ape-like body that emits smoke",
    "True-kin with long blonde hair and lacy attire",
    "Cacogen with AV-plated head (+1 AV)",
    "New-Mantis with a child’s face mask",
    "Mycomorph with a speckled, leathery head",
    "Synth with white priest-like body, worships bee hive",
    "True-kin with expensive ape-fur clothing",
)


def roll_ego(ego):
    result = randint(1, 20) + ego
    if result < 1:
        return 1
    return result


def gen_follower(ego):
    name = names[roll_ego(ego) - 1]
    level = levels[(roll_ego(ego) - 1) // 8]
    av = 10 + (roll_ego(ego) - 1) // 10
    morale = morale_scores[(roll_ego(ego) - 1) // 5]
    attack = attacks[roll_ego(ego) - 1]
    description = descriptions[roll_ego(ego) - 1]
    return Follower(name, level, av, morale, attack, description)
