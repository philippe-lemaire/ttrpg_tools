from random import choice
from .roll import roll_d66

allies_and_ennemies_table = {
    "11": "Naval Officer",
    "12": "Imperial Diplomat ",
    "13": "Crooked Trader ",
    "14": "Medical Doctor",
    "15": "Eccentric Scientist",
    "16": "Mercenary",
    "21": "Famous Performer",
    "22": "Alien Thief",
    "23": "Free Trader",
    "24": "Explorer",
    "25": "Marine Captain",
    "26": "Corporate Executive",
    "31": "Researcher",
    "32": "Cultural Attaché",
    "33": "Religious Leader",
    "34": "Conspirator",
    "35": "Rich Noble",
    "36": "Artificial Intelligence",
    "41": "Bored Noble",
    "42": "Planetary Governor",
    "43": "Inveterate Gambler",
    "44": "Crusading Journalist",
    "45": "Doomsday Cultist",
    "46": "Corporate Agent",
    "51": "Criminal Syndicate",
    "52": "Military Governor",
    "53": "Army Quartermaster",
    "54": "Private Investigator",
    "55": "Starport Administrator",
    "56": "Retired Admiral",
    "61": "Alien Ambassador",
    "62": "Smuggler",
    "63": "Weapons Inspector",
    "64": "Elder Statesman",
    "65": "Planetary Warlord",
    "66": "Imperial Agent",
}

quirks_table = {
    "11": "Loyal",
    "12": "Distracted by other worries",
    "13": "In debt to criminals",
    "14": "Makes very bad jokes",
    "15": "Will betray characters",
    "16": "Aggressive",
    "21": "Has secret allies",
    "22": "Secret anagathic user",
    "23": "Looking for something",
    "24": "Helpful",
    "25": "Forgetful",
    "26": "Wants to hire the Travellers",
    "31": "Has useful contacts",
    "32": "Artistic",
    "33": "Easily confused",
    "34": "Unusually ugly",
    "35": "Worried about current situation",
    "36": "Shows pictures of their children",
    "41": "Rumour-monger",
    "42": "Possesses telepathy or other unusual quality",
    "43": "Unusually provincial",
    "44": "Drunkard or drug addict",
    "45": "Government informant",
    "46": "Mistakes a Traveller for someone else",
    "51": "Possesses unusually advanced technology",
    "52": "Unusually handsome or beautiful",
    "53": "Spying on the Travellers",
    "54": "Possesses TAS membership",
    "55": "Is secretly hostile towards the Travellers",
    "56": "Wants to borrow money",
    "61": "Is convinced the Travellers are dangerous",
    "62": "Involved in political intrigue",
    "63": "Has a dangerous secret",
    "64": "Wants to get off planet as soon as possible",
    "65": "Attracted to a Traveller",
    "66": "From offworld",
}


experience_level = (
    (
        "Green Non-combatant",
        "Drive/Flyer",
        "0",
        "+0",
    ),
    (
        "Green Combatant",
        "Drive/Flyer, Gun Combat, Melee",
        "0",
        "+0",
    ),
    (
        "Average Non-combatant",
        "Drive/Flyer, Profession",
        "1",
        "+1",
    ),
    (
        "Average Combatant",
        "Drive/Flyer, Gun Combat, Melee, Recon",
        "1",
        "+1",
    ),
    (
        "Experienced Non-combatant",
        "Admin, Drive/Flyer, Profession",
        "2",
        "+1, +2",
    ),
    (
        "Experienced Combatant",
        "Drive/Flyer, Gun Combat, Heavy Weapons, Melee, Recon",
        "2",
        "+1, +2",
    ),
    (
        "Elite Non-combatant",
        "Admin, Drive/Flyer, Investigate, Profession ",
        "3",
        "+1, +2, +3",
    ),
    (
        "Elite Combatant",
        "Drive/Flyer, Gun Combat, Heavy Weapons, Melee, Recon, Tactics",
        "3",
        "+1, +2, +3",
    ),
)


class NPC:
    def __init__(self):
        self.npc_type = allies_and_ennemies_table.get(roll_d66())
        self.quirk = quirks_table.get(roll_d66())
        (
            self.experience_level,
            self.skills,
            self.average_skill_levels,
            self.characteristics,
        ) = choice(experience_level)
