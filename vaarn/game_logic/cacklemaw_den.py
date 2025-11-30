from random import choice
from dataclasses import dataclass

leaders = (
    "Mama Hecklehaw",
    "Mama Gloatgrim",
    "Mama Yawningfool",
    "Nana Rictus",
    "Nana Blacklaugh",
)

weapons = (
    "Bowcasters",
    "Rusted Blades",
    "Ornate Razorwhips",
    "Envenomed Spears",
    "Impulse Rifles",
    "Hellblasters",
    "Storm Guns",
    "Throwing Knives",
    "Blunderbores",
    "Prism Cannons",
    "Nailguns",
    "Flesh-rippers",
    "Nets and Tridents",
    "Spore Launchers",
    "Laser Rifles",
    "Exploding Javelins",
    "Shrieker Bombs",
    "Glue Guns",
    "Hegemony Autorifles",
    "Teeth and Claws",
)


activities = (
    "Sleeping",
    "Fleeing",
    "In-Fighting",
    "Funeral",
    "Singing",
    "Drunk",
    "Psychedelic Ritual",
    "Sacred Puppet Show",
    "Rustling Livestock",
    "Extorting a Merchant",
    "Transporting Prisoners",
    "Repairing Tents",
    "Gambling",
    "Marking Territory",
    "Cooking",
    "Fighting (Other Monster)",
    "Fighting (Other Monster)",
    "Fighting (Other Cacklemaw)",
    "Fighting (Other Cacklemaw)",
    "Fighting (Faa Nomads)",
)

wants = (
    "Meat",
    "Meat",
    "Meat",
    "Meat",
    "Water",
    "Water",
    "Water",
    "Water",
    "Directions",
    "Tribute",
    "Jokes",
    "Music",
    "Cruelty",
    "Repairs",
    "Drugs",
    "Booze",
    "Reinforcements",
    "Prisoners",
    "Shelter",
)


@dataclass
class CaclemawDen:
    sworn_to: str
    weapons: str
    activity: str
    they_want: str

    def __repr__(self):
        return f"""Sworn to {self.sworn_to.title()}, armed with {self.weapons.lower()}.
    <br>
    Their current activity: {self.activity.lower()}.
    <br>
    They want {self.they_want.lower()}.
    """


def gen_cacklemaw_den():
    leader = choice(leaders)
    weapon = choice(weapons)
    activity = choice(activities)
    want = choice(wants)
    return CaclemawDen(leader, weapon, activity, want)
