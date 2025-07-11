from dataclasses import dataclass


@dataclass
class Calling:
    name: str
    description: str
    might: int
    deft: int
    grit: int
    insight: int
    aura: int
    attack_bonus: int
    hearts: int
    defense: int
    speed: str
    starting_abilities: list


factotum_data = {
    "name": "factotum",
    "description": "You elevate everyday skills to an almost magical level. Your motto: be prepared, focus on the details, don’t be a hero.",
    "might": 7,
    "deft": 9,
    "grit": 8,
    "insight": 9,
    "aura": 9,
    "attack_bonus": 0,
    "hearts": 2,
    "defense": 10,
    "speed": "average",
    "starting_abilities": ["Second to None", "Factotum Pack", "Don't Mind Me"],
}

champion_data = {
    "name": "champion",
    "description": "You are a valiant fighter who favors force and direct action.  Why pick a locked door when it can be kicked off its hinges?",
    "might": 10,
    "deft": 8,
    "grit": 9,
    "insight": 7,
    "aura": 8,
    "attack_bonus": 1,
    "hearts": 3,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Combat Momentum",
        "Favored Weapon",
        "Into the Fray",
    ],
}

sneak_data = {
    "name": "sneak",
    "description": "You’re a rogue who uses acrobatics and dirty tricks to succeed.  Not everyone approves, but that’s their problem.",
    "might": 7,
    "deft": 10,
    "grit": 7,
    "insight": 10,
    "aura": 8,
    "attack_bonus": 0,
    "hearts": 2,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Light Footed",
        "Furtive ",
        "Sticky Fingers",
    ],
}

raider_data = {
    "name": "raider",
    "description": "You find victory through speed and precision. Even the mightiest foes fear your fluid and precise combat prowess.",
    "might": 9,
    "deft": 9,
    "grit": 9,
    "insight": 8,
    "aura": 7,
    "attack_bonus": 1,
    "hearts": 3,
    "defense": 10,
    "speed": "fast",
    "starting_abilities": [
        "Like the Wind",
        "Hunter’s Focus",
        "Sidestep",
    ],
}

battle_princess_data = {
    "name": "battle princess",
    "description": "You are a wielder of Bright Magic and a stalwart defender of the things you hold dear. You inspire and motivate all those around you.",
    "might": 8,
    "deft": 8,
    "grit": 9,
    "insight": 7,
    "aura": 10,
    "attack_bonus": 1,
    "hearts": 3,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Heart’s Blade",
        "Shield of Love",
        "Soul Companion",
    ],
}

murder_princess_data = {
    "name": "murder princess",
    "description": "You focus your Dark Magic to obliterate the source of your hatred. There will be no clemency for those who oppose you.",
    "might": 8,
    "deft": 7,
    "grit": 10,
    "insight": 8,
    "aura": 9,
    "attack_bonus": 1,
    "hearts": 3,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Wrath’s Blade",
        "Withering Glare",
        "Tenacity",
    ],
}

sage_data = {
    "name": "sage",
    "description": "You are a learned researcher and practitioner of Wizardry. Mana is yours to command, and with it you weave wonder and whimsy.",
    "might": 6,
    "deft": 8,
    "grit": 8,
    "insight": 10,
    "aura": 8,
    "attack_bonus": 0,
    "hearts": 2,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Grand Grimoire",
        "Sage’s Staff",
        "Prestidigitonium",
    ],
}

heretic_data = {
    "name": "heretic",
    "description": "You read from the Blasphemous Script to call forth the Forbidden.  Sometimes they serve, sometimes they chastise.",
    "might": 7,
    "deft": 7,
    "grit": 10,
    "insight": 7,
    "aura": 9,
    "attack_bonus": 0,
    "hearts": 2,
    "defense": 10,
    "speed": "average",
    "starting_abilities": [
        "Fitful Sleep",
        "Dreadful",
        "Squire Marlow",
    ],
}


callings_names = [
    "factotum",
    "champion",
    "sneak",
    "raider",
    "battle princess",
    "murder princess",
    "sage",
    "heretic",
]


calling_objects = [
    Calling(**factotum_data),
    Calling(**champion_data),
    Calling(**sneak_data),
    Calling(**raider_data),
    Calling(**battle_princess_data),
    Calling(**murder_princess_data),
    Calling(**sage_data),
    Calling(**heretic_data),
]
CALLINGS = {n: c for n, c in zip(callings_names, calling_objects)}
