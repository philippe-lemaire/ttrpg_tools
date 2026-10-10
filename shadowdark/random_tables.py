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


citadel_random_encounters = (
    "The <b>Scarlet Minotaur</b> (Area 18) stalks into sight, bellowing challenges and pawing the stone",
    "1d4 <b>ettercaps</b> and 1d8 <b>beastmen</b> clash in a bloody melee",
    "A dry gust of wind extinguishes all torches and lamps",
    "1d6 <b>ettercaps</b> creep along, searching for gold and gems",
    "The <b>skeletons</b> of 1d6 dead adventurers or warrior-mages stagger into sight",
    "2d4 <b>beastmen</b> argue in hushed whispers over who gets to eat the centipedes they just trapped in a bag",
    "1d4 <b>darkmantles</b> swoop out, bobbing and spinning in a territorial warning dance",
    "A <b>cave creeper</b> rushes along the ceiling toward light",
)
citadel_rumors = (
    "Ancient kings who dwelt in the citadel possessed magical weapons that were feared far and wide.",
    "A savage minotaur drenched in blood stalks the citadel's halls.",
    "Piles of gems and gold lie about as if totally forgotten.",
    "Beware when touching the body of a dead citadel dweller.",
    "Opportunistic, gray-furred beastmen haunt the shadows.",
    "The citadel is rife with secret rooms and passageways.",
)


def gen_trap():

    trap_types = (
        "Crossbow",
        "Hail of needles",
        "Toxic gas",
        "Barbed net",
        "Rolling boulder",
        "Slicing blade",
        "Spiked pit",
        "Javelin",
        "Magical glyph",
        "Blast of fire",
        "Falling block",
        "Cursed statue",
    )

    trap_triggers = (
        "Tripwire",
        "Pressure plate",
        "Opening a door",
        "Switch or button",
        "False step on stairs",
        "Closing a door",
        "Breaking a light beam ",
        "Pulling a lever",
        "A word is spoken",
        "Hook on a thread",
        "Removing an object",
        "Casting a spell",
    )

    trap_effects = (
        "1d6",
        "1d6/sleep",
        "1d6/paralyze",
        "1d6/blind",
        "2d8",
        "2d8/sleep",
        "2d8/paralyze",
        "2d8/confuse",
        "3d10",
        "3d10/paralyze",
        "3d10/unconscious",
        "3d10/petrify",
    )

    return [
        f"""<table class='table table-sm'>
<tr>
<th>Trap</th>
<th>Trigger</th>
<th>Effect</th>
</tr>
<tr>
<td>{trap}</td><td>{trigger}</td><td>{effect}</td>
</tr>
</table>"""
        for trap, trigger, effect in product(trap_types, trap_triggers, trap_effects)
    ]


rumors_reaches = (
    "Devil's Peak in the Rimespires has a mighty spell upon it",
    "No road in the Western Reaches is safe from local bandits",
    "Deep underground, there is a dark library full of knowledge",
    "If you see a suspicious mountain goat, try to capture it",
    "In the Steppes, the Iron King guards a castle full of treasure",
    "Pit fighting is a common practice in the Djurum Desert",
    "There is an inescapable prison-island in the Last Sea",
    "Rangers in the Sablewood are first to learn of dangers",
    "Portals to other worlds are hidden all throughout the land",
    "Demons hatch out of black trees in The Gloaming forest",
    "Giant crabs swarm all over a tropical island far to the south",
    "A secretive village of halflings hides in the Lowland Moor",
    "The founding king of Stonehall was not buried there",
    "Atop a cloudy peak, an immortal man dwells in isolation",
    "The dwarves in the Bastions are beset by wyvern attacks",
    "St. Terragnis fought mighty devils in the Rimespire peaks",
    "Black structures in the jungle house otherworldly beings",
    "The elf City-State of Lydonia is a surreal place of magic",
    "An accursed dragon flies over the desert during storms",
    "An ancient tyrant's castle lies abandoned in the Sablewood",
    "You might spot a rare blue tiger in the Dhalpurna range",
    "Elder dwarves called the dverg explored this land long ago",
    "The desert is home to ancient cults and dying traditions",
    "The villages in the Isles of Andrik are always in conflict",
    "A king's pyramid lies buried in the trackless desert sands",
    "Every devil's contract is pinned to a cursed tree in the bog",
    "You can find a dragon in almost every region of the Reaches",
    "Nuns who battle demons live in a priory in the Rimespires",
    "Beware mountains that spire fire; they have fierce denizens",
    "Don't try to steal a silver camel from the Siruul elves or else",
    "Powerful dead creatures draw evil necromancers like flies",
    "The raiders from the northern isles war among themselves",
    "The archmage Murabi is entombed in the Silent Mountains",
    "Dwarves are creating a new settlement in the Bastions",
    "Daryos of Reme is the greatest duelist in all the Reaches",
    "Countless bandits wait to ambush merchants in the desert",
    "A rare blue tree frog in the jungle can cure any disease",
    "Pirates hide out along the rivers and coasts of the jungle",
    "Every village and town hides a secret if you look carefully",
    "The dwarves of Stonehall are friendly, if you can get inside",
    "A terrible plague has beset a small village in The Gloaming",
    "A pirate with a genius intellect rules a town in the desert",
    "The most ancient humans in the Reaches live in the jungle",
    "There's a living mountain called Old Father who speaks",
    "Elemental powers take human shape in the Kyzian Steppes",
    "Do not trust ordinary folk who speak in the Dragon tongue",
    "A crazy blue kobold lives on a dinghy in the south Last Sea",
    "The lost citadel of an ancient bull god lies in the Steppes",
    "An old woman in the northern isles can change your fate",
    "Fire dwarves live on a volcanic island near the Rimespires",
    "An city of goblins and orcs sits high in the Gilzai Mountains",
    "Witches are hated in some villages in The Gloaming forest",
    "A famous saint stopped an earthquake on a rocky island",
    "Meeting a werebear is said to bring good health and luck",
    "There's a lawless pirate town on the coast of the jungle",
    "A wolf with six burning eyes stalks the Lowland Moor",
    "A retired old man lives alone in a keep on the west coast",
    "There is a way to summon storms in the far southern peaks",
    "Lizardfolk ruled the central swamp long before humankind",
    "Wizards build their lonely towers in the most remote places",
    "A grumpy old goblin saved a hunter lost inside Myre Swamp",
    "Beware empty cabins in the woods; they're always haunted",
    "Strange orcs that are sensitive to light dwell in the Bastions",
    "The best way to learn about a town is to visit its tavern",
    "Unsettling shamans in black gather in the Kyzian Steppes",
    "If you toss a coin in a well and don't hear a splash, beware",
    "The priest on the remote island of Huran recently went mad",
    "The many Kyzian Princes each vie for power and influence",
    "Sailing near the west side of the Bastions can be dangerous",
    "The pirate ship Myth Mortis was seen at a northern island",
    "Many famous explorers are drawn to the Tal-Yool Jungle",
    "The Green Knights have fallen, but a few of them still exist",
    "A strange mystic lives in a high cave in the Silent Mountains",
    "Only true-hearted wizards can study at Gedgarrin University",
    "The famous elf bandit Lysandir lives in the Sablewood",
    "Ancient abominations sleep beneath purple mountains",
    "A witch gifted with dark fey magic lives in Myre Swamp",
    "A giant iceberg in the northern sea has shapes moving in it",
    "Goblins and orcs always gather in remote box canyons",
    "Foolish nobles built estates at the edge of Myre Swamp",
    "The fire dragon the Kyzian Queen drove off is still out there",
    "The Willowman is real and he haunts The Gloaming forest",
    "If you see an onyx statue of a twisted human, don't touch it",
    "Some monks in the Dhalpurnas have transcended death",
    "If you want to learn witchcraft, find Uncle Grigor in the bogs",
    "Giant spiders have crept back into the Sablewood recently",
    "Madness lies beyond the lonely gate of metal and lightning",
    "There are no better horse trainers than the Kyzian people",
    "Gods walk in the Silent Mountains during the full moon",
    "Three island mark the site of a city that sank into the sea",
    "Trolls in the Lowland Moor know magical words of power",
    "Those on the road west of the swamp often hear yodeling",
    "Strange lords from the Fey Realms dwell in the Sablewood",
    "A retired gladiator named Rameer trains aspiring fighters",
    "Something bad is happening to travelers in Frostfall Pass",
    "A scary witch lives in the heath of the Duchy of Montmar",
    "The snake-people of myth still dwell in the remote jungle",
    "The Duke of the City of Masks and King of Lydonia are allies",
    "There is no more evil place under the sun than Myre Swamp",
    "There is an altar on a distant mountain that can restore life",
)

rumors_kyzian_steppes = (
    "A war camp of orcs is mustering near the Gilzai Mountains",
    "The burial mound of Overlord Ashurba lies to the north",
    "The princess in the city of The Ivory Palace is missing",
    "An elemental spirit of water lives in the Sardaquian Sea",
    "Old Yorin can train any horse into the best version of itself",
    "Gnolls have been attacking travelers on the eastern road",
    "Lightning repeatedly strikes a pit in the earth to the far east",
    "Capturing a horse on the open Steppes raises your notoriety",
    "A cult of black-clad shamans is growing more numerous",
    "Bull-worshipping cultists once ruled the southern Steppes",
)

points_of_interest_kyzian_steppes = (
    "A group of outcast Kyzians runs a giant millstone turned by captive peasants; one captive is an indomitable berserker",
    "Floodwater turns this hex into a field of deep mud; DC 12 WIS if crossing or mounts sink into it and become stuck",
    "A shrine to the Sky Mother, an aspect of Gede, has 1d6 knotted ropes; each one can banish an elemental once",
    "A herd of wild horses frequents this hex; catching one (DC 15 DEX, one attempt per week) grants +1 renown once",
    "A pole strung with dozens of hawk skulls marks a disputed border between two Kyzian Princes; two riders guard it",
    "An old woman tends to a cluster of six grassy burial mounds; she has seen pale, black-clad people snooping about",
    "Two rival Kyzian Princes have each brought 100 riders to witness them race; they argue over what the stakes will be",
    "A saddled horse skeleton grazes on nothing and tosses its head; it follows the PCs at a distance for the next 1d4 days",
    "A village of wheat farmers eke out a living; raiding orcs recently stole their entire crop and left the farmers to starve",
    "A field of squat stones each have a trail behind them; strong winds slowly push them along, carving shallow paths",
    "A group of Ashen One adepts gather around a burial mound; they refuse to answer questions and stare ominously",
    "4 efreet in red silk robes dance around a pillar of fire; this is a blessed tongue of flame that fell from the sun itself",
    "A massive colony of marmots scamper between dirt hills; they all screech wildly in unison if danger approaches",
    "A group of 40 gnolls makes camp in this hex; 20 pursue anyone they spot for 1d4 days on war hyenas (treat as worgs)",
    "A roaring pillar of wind reaches up to the sky, lifting dirt and debris; stepping inside transports you to Zulara (5848)",
    "A cluster of four burial mounds has been ransacked; their seals hang broken, and a cold wind emanates from inside",
    "Cawing vultures pick through a battleground of recently slain Kyzians; if left unburied, the dead soon rise as zombies",
    "Ribbons and prayer beads drape over a golden bull statue; petitioners of Oros gain a luck token by leaving an offering",
    "An abandoned yurt sits alone with its cookfire still hot and food untouched; the yurt's felt is made of human hair",
    "The Prince of Winds gallops here, a glorious stallion spirit of silver fire; mounts who run with him regain all lost HP",
)

TABLES = {
    "Lost Citadel Rumors": citadel_rumors,
    "Lost Citatel Encounters": citadel_random_encounters,
    "Lost Citadel You Died Table": lost_citadel_oh_no_you_died_table,
    "Minotaur Respawns": gen_minotaur_table(),
    "Bestman": gen_beastman(),
    "Ettercap": gen_ettercap(),
    "Random trap": gen_trap(),
    "Rumors in the Reaches": rumors_reaches,
    "Rumors in the Kyzian Steppes": rumors_kyzian_steppes,
    "Points of Interest Kyzian Steppes": points_of_interest_kyzian_steppes,
}
