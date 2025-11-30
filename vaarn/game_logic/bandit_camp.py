from random import choice
from dataclasses import dataclass

bandit_camp_data = (
    (
        "Ex-Gladiators",
        "an Injured Gladiator",
        "Martial Arts",
        "Water",
    ),
    (
        "Sly Mycomorphs",
        "Small but Intense",
        "Bite and Scream",
        "Food",
    ),
    (
        "Hegemony Deserters",
        "a One-Eyed Woman",
        "Crossbows",
        "Gold",
    ),
    (
        "Escaped Slaves",
        "a Rogue Synth",
        "Blowdarts",
        "Weapons",
    ),
    (
        "Luckless Drifters",
        "a Self-styled King",
        "Throwing Axes",
        "Sacrifices",
    ),
    (
        "Doomsday Cult",
        "an Exiled Nobleman",
        "Swords",
        "New Recruits",
    ),
    (
        "Lepers",
        "a teller of Jokes",
        "Slings",
        "Medicine",
    ),
    (
        "Slavers",
        "an Infamous Outlaw",
        "Spears and Nets",
        "Forbidden Books",
    ),
    (
        "Cruel Synthetic Children",
        "a Silent Brute",
        "Flails",
        "Fungus",
    ),
    (
        "Ghoul Clan",
        "a Scrawny Genius",
        "Rocket Launcher",
        "Synths",
    ),
    (
        "False Monks",
        "an Ex-Courtesan",
        "Poison Gas",
        "Children",
    ),
    (
        "Fungus-riddled Maniacs",
        "a Smiling Psychopath",
        "Revolvers",
        "Slaves",
    ),
    (
        "Businesslike Thugs",
        "a Delusional Drunkard",
        "Rifles",
        "Entertainment",
    ),
    (
        "Gibbering Cacogen",
        "a Sadistic Glutton",
        "Crude Jezails",
        "Wine",
    ),
    (
        "Maskless Newbeasts",
        "Calm and Polite",
        "Ancient Cannon",
        "Beer",
    ),
    (
        "Gang of Fools",
        "Apologetic but Firm",
        "Combat Lasers",
        "Forgiveness",
    ),
    (
        "Scantily Clad Women",
        "Lustful and Crude",
        "Sonic Weapons",
        "To Eat You",
    ),
    (
        "Elderly Thieves",
        "Cartoonishly Evil",
        "Trained Beasts",
        "Single Combat",
    ),
    (
        "Hegemony Soldiers",
        "Loves to leave a Calling Card",
        "Plasma Rifles",
        "Your Eyes",
    ),
    (
        "Gentleman Robbers",
        "a Robin Hood-esque",
        "Psychic Powers",
        "Your Teeth",
    ),
)

npc_a_options = (
    "Bandit Leader",
    "Leader’s Trusted Underling",
    "Leader’s Ambitious Underling",
    "Leader’s Despised Underling",
    "The Best Cook (of a Bad Bunch)",
    "The Best Shot (of a Bad Bunch)",
    "Widely Disliked Bandit",
    "Ferocious, Feared Bandit",
    "Very Young Bandit",
    "Ancient, Decrepit Bandit",
)

npc_b_options = (
    "Rival to Leader’s Authority",
    "Talkative, Annoying Bandit",
    "Lazy, Useless Bandit",
    "Scholarly, Educated Bandit",
    "Religious, Psychotic Bandit",
    "Sharp-eyed, Paranoid Bandit",
    "Tough-talking Bandit, Secret Coward",
    "Prisoner, Who Keeps the Camp Tidy",
    "Prisoner, Who Aids with Cooking",
    "Wealthy Prisoner, Kept for Ransom",
)

sources_of_conflict = (
    "Envy (Property)",
    "Envy (Success)",
    "Love (Forbidden)",
    "Love (Unrequited)",
    "Love (Triangle)",
    "Unpaid Debts",
    "Boredom",
    "Petty Rivalry",
    "Cheating at Cards",
    "Gossip",
    "Adultery",
    "Conspiracy",
    "Gluttony",
    "Mistaken Identity",
    "Wild, Baseless Accusations",
    "Addiction (Drink)",
    "Addiction (Narcotics)",
    "Division of Loot",
    "Blackmail",
    "Murder",
)


@dataclass
class BanditCamp:
    the_bandits: str
    their_leader: str
    weapons: str
    they_want: str
    npc_a: str
    source_of_conflict: str
    npc_b: str

    def __repr__(self):
        return f"""{self.the_bandits.capitalize()}, their leader is {self.their_leader.lower()}.<br>They fight with {self.weapons.lower()} and they want {self.they_want.lower()}.
    <br><br>
    {self.npc_a} is in conflict with {self.npc_b} over {self.source_of_conflict}.
    """


def gen_bandit_camp():
    data = [choice(bandit_camp_data)[k] for k in range(4)]
    data.extend(
        [choice(npc_a_options), choice(sources_of_conflict), choice(npc_b_options)]
    )
    return BanditCamp(*data)
