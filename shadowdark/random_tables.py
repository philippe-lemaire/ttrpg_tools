from itertools import product

lost_citadel_oh_no_you_died_table = (
    "Your new character is… Trapped inside a cocoon of ettercap webs in a dark corner.",
    "Your new character is… Hanging by your backpack from a spur in the stone wall.",
    "Your new character is… Waking up on the floor with no memory of the past week.",
    "Your new character is… Hiding inside a large clay jar painted with leaping bulls.",
    "Your new character is… Standing very still in the next room to look like a statue.",
    "Your new character is… Materializing here after some unexpected magical mishap.",
    "Your new character is… Sleeping under a pile of dusty, moth-eaten rags and trash.",
    "Your new character is… A prisoner of the ettercaps; you just escaped from them.",
    "Your new character is… A lost traveler who thought this was a safe place to camp.",
    "Your new character is… Looking for your cousin, Giuseppe Baldini.",
    "Your new character is… The last surviving member of a party the Minotaur just killed.",
    "Your new character is… A prisoner of the beastmen; you just broke free of them.",
    "Your new character is… A secret bull god cultist who wants Oros worship to return.",
    "Your new character is… Actively being chased by another random encounter.",
    "Your new character is… Hog tied and gagged with a note that says 'Minotaur bait'.",
    "Your new character is… Stuck to the ceiling by a cave creeper that will be back later.",
    "Your new character is… A descendant of Orwyn the Younger.",
    "Your new character is… Wrapped in an ancient, dusty carpet set against the wall.",
    "Your new character is… Crammed inside a large treasure chest in the next room.",
    "Your new character is… Thrown through a dimensional door to land here in a heap.",
)


durations = (
    "1 round",
    "1d4 rounds",
    "1d4 rounds",
    "2d8 rounds",
    "2d8 rounds",
    "1 day",
    "1 day",
    "1 day",
    "1 week",
    "1 week",
    "2 weeks",
    "1 month",
)
locations = (
    "Where PCs are",
    "Area 1",
    "Area 2",
    "Area 15",
    "Area 16",
    "Area 26",
    "Area 21",
    "Area 22",
    "Area 22",
    "Area 18",
    "Area 18",
    "Pool in Area 27",
)
changes = (
    "Gains 1 greataxe attack",
    "Gains 1d8 HP",
    "Charge deals x3 damage",
    "Is next random encounter",
    "Wears plate mail (AC 15)",
    "Gains 1d4 HP",
    "Focuses on his prior killer",
    "Loses 1d4 HP",
    "Charge reduced to near",
    "Has no armor (AC 11)",
    "Loses 1d8 HP",
    "Loses 1 greataxe attack",
)


def gen_minotaur_table():

    return [
        f"The Minotaur respawns in {duration}, in {location}, and {change}"
        for duration, location, change in product(durations, locations, changes)
    ]


def gen_beastman():
    names = (
        "Rat / Gobbo ",
        "Barto / Hule ",
        "Egor / Ralk ",
        "Nila / Bugg ",
        "Dent / Borvin ",
        "Tail / Ludo ",
        "Skred / Billo ",
        "Halda / Yarv ",
        "Crag / Dorel ",
        "Lorga / Mouse ",
    )
    appearances = (
        "Patchy / Sickly ",
        "Broken jaw or nose ",
        "Scarred / Fat ",
        "Stooped / Short ",
        "Elderly / Stout ",
        "Missing ear or tooth ",
        "Braided hair / Bald ",
        "White fur / Skinny ",
        "Clean / Blank stare ",
        "Wild eyes / Lanky ",
    )
    behaviors = (
        "Glares / Lurks",
        "Whispers / Burps",
        "Scratches / Snorts",
        "Picks nose / Growls",
        "Creeps / Rushes",
        "Yawns / Drools",
        "Limps / Sulks",
        "Paces / Chews nails",
        "Polite / Complains",
        "Curses / Silent",
    )
    return [
        f"Name: {name}, looks: {look}, behavior: {behavior}"
        for name, look, behavior in product(names, appearances, behaviors)
    ]


def gen_ettercap():
    names = (
        "Kreel / Bisky ",
        "Slivin / Slaask ",
        "Tiri / Vilis ",
        "Chiska / Liss ",
        "Jarla / Miri ",
        "Char / Squill ",
        "Fisk / Yeek ",
        "Chirr / Vim ",
        "Rask / Miska ",
    )
    appearances = (
        "Groomed / Rotund ",
        "Skalt / Trisk ",
        "Singed fur / Gangly ",
        "Blue eyes / Spotted ",
        "Pained / Hunched ",
        "Springy / Withered ",
        "Sickly / Molting ",
        "Missing limb / Tall ",
        "Scarred / Lumpish ",
        "Filthy / Hulking ",
        "Jewelry / Clothing ",
    )
    behaviors = (
        "Preening / Haughty",
        "Twitches / Cowers",
        "Bossy / Skeptical",
        "Delicate / Squeamish",
        "Distracted / Mutters",
        "Clicks claws / Hisses",
        "Hasty / Alarmist",
        "Nosy / Gossips",
        "Critical / Sarcastic",
        "Rude / Surly",
    )
    return [
        f"Name: {name}, looks: {look}, behavior: {behavior}"
        for name, look, behavior in product(names, appearances, behaviors)
    ]


TABLES = {
    "Lost Citadel You Died Table": lost_citadel_oh_no_you_died_table,
    "Minotaur Respawns": gen_minotaur_table(),
    "Bestman": gen_beastman(),
    "Ettercap": gen_ettercap(),
}
