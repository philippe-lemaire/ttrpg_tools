from random import choice
from dataclasses import dataclass

lair_data = (
    (
        "D4 Alzabo",
        "Hillside Cave",
        "Hear a Child’s Voice, Which Echoes Oddly",
    ),
    (
        "2d8 Anthrophagi",
        "Bowels of Rusting War Machine",
        "Glitching Chirps and Alarm Noises",
    ),
    (
        "D4 Amaranthine Death-Worms",
        "Toxin-Rotted Tree",
        "Huge Sinuous Tracks in the Dirt",
    ),
    (
        "Argent Shepherd",
        "Ruined Chapel",
        "Madmen with Argent Halos Beg You to Repent",
    ),
    (
        "2d4 Babble Birds",
        "Nest in Hollow Tree",
        "Distant Chirping and Singing",
    ),
    (
        "Bacterial Gestalt Colony",
        "Within Belly of Corpse",
        "Indecipherable Psychic Noise",
    ),
    (
        "2d6 Battle Boars",
        "Shaded Dustbath",
        "Boulders with Tusk-Marks",
    ),
    (
        "2d6 Behemoth Toads",
        "Stagnant Pool",
        "Webbed Footprints",
    ),
    (
        "D3 Blightbeasts",
        "Toxic Waste Dump",
        "Skyward Plumes of Acrid Breath",
    ),
    (
        "2d6 Blind Crabs",
        "Shallow Burrows in Sand",
        "Remains of Shed White Crabshell",
    ),
    (
        "6d6 Blue Baboons",
        "Rocky Outcrop",
        "Excrement Heaped Everywhere",
    ),
    (
        "Brood Mother",
        "Vast Web Spun Inside Ruins",
        "Dead Body of Broodling",
    ),
    (
        "D3 Chimera",
        "Roost Atop Mesa",
        "Fire-Blackened Bones of Victim",
    ),
    (
        "Chrome-Feathered Sailback",
        "Flat Basking Plain",
        "Chrome Feathers Float on the Wind",
    ),
    (
        "Chromavore",
        "Colourless Cactus Grove",
        "Colourless Husks of Faa Family",
    ),
    (
        "2d8 Cliff Ghuls",
        "Roosts in Clifside Caves",
        "Distant Spitting and Retching",
    ),
    (
        "d6 Copy Cats",
        "Dens Dug in Shady Hillside",
        "Pink Hairball Stuck in Vegetation",
    ),
    (
        "D4 Daggertrunks",
        "Cellar of Abandoned House",
        "Dead Animal with Round Trunk-Wounds",
    ),
    (
        "D6 Deathblight Husks",
        "Curse-Blackened Ruins",
        "Black Footprints Seared into Sand",
    ),
    (
        "D3 Desiccators",
        "Grove of Dessicated Cacti",
        "Bone-Dry Corpse, Turning to Dust",
    ),
    (
        "D4 Doppelgellers",
        "Jelly-Rimed Sinkhole",
        "Solitary Jelly-Clone, Decaying to Sludge",
    ),
    (
        "Entropy Wight",
        "Utterly Lifeless Wasteland",
        "Deathly Whispers and Groans",
    ),
    (
        "4d6 Eyeless Dogs",
        "Sleep in Shade of Martyr Trees",
        "Hear Howling on the Wind",
    ),
    (
        "Exemplar",
        "Perfect White Pagoda",
        "Perfect Circle Effortlessly Drawn in Sand",
    ),
    (
        "2d4 Faminebearers",
        "Empty Granary",
        "Corpse; Died Eating Themselves",
    ),
    (
        "Fissile Glittersludge",
        "Rusting Chemical Tank",
        "Globs of Glittering Black Jelly",
    ),
    (
        "Fractalisk",
        "Hypergeometric Relay Station",
        "Recursive Fractal Footprints in Sand",
    ),
    (
        "2d8 Gene Thieves",
        "Clay-Brick Shelters",
        "Attempts at Setting Snare-Traps",
    ),
    (
        "2d8 Ghouls",
        "Untidy Wooden Huts",
        "Graveyard with Unearthed Graves",
    ),
    (
        "2d4 Giant Azure Scorpions",
        "Hide Beneath Sand",
        "Shed Azure Exoskeleton",
    ),
    (
        "2d6 Gitchghasts",
        "Crystal-Encrusted Hovel",
        "Crystallised Rotting Limb",
    ),
    (
        "D6 Gladiator Synths",
        "Sand-Swallowed Arena",
        "Synthetic Voice Recites Upcoming Fights",
    ),
    (
        "2d4 Glass Tigers",
        "Lurk on Salt Flats",
        "Corpse with Tell-Tale Broken Neck",
    ),
    (
        "Gorgon",
        "Decadent Boudoir Tent",
        "Huge Shed Snakeskin",
    ),
    (
        "Gravity Tyrant",
        "Mass of Accreted Boulders",
        "See Distant Victim ‘Falling’ into Sky",
    ),
    (
        "2d8 Greenguard",
        "Abandoned Fortifications",
        "Enamel Bullets Embedded in Rocks",
    ),
    (
        "2d8 Grey Crickets",
        "Nest in Undergrowth",
        "Hear Distinctive Chirping Songs",
    ),
    (
        "D4 Harlequin Serpents",
        "Beneath Large Boulder",
        "Hear ‘Laughter’ of Poisoned Animal",
    ),
    (
        "2d6 Hiveymen",
        "Gruesome Black Hive",
        "Single Sable Bee Crawls on Ground",
    ),
    (
        "2d4 Hollow Maidens",
        "Hypergeometric Chapel",
        "Möbius Strip of White Cloth Caught in Bush",
    ),
    (
        "2d6 Iridium Vultures",
        "Treetop Nests of Wire",
        "See Vultures Circling High in the Sky",
    ),
    (
        "Jollyhoss",
        "Bisected Tent",
        "Find Corpse Bitten Exactly in Half",
    ),
    (
        "Juggernaut",
        "Large Flat Roaming Plain",
        "Hear Its Roars and Lamentations",
    ),
    (
        "Khronophage",
        "Ruined Clocktower",
        "Timepieces Behave Erratically",
    ),
    (
        "2d6 Lambent Lynx",
        "Den High in the Cliffs",
        "Electrical Taste in the Air",
    ),
    (
        "2d6 Lazarus Guard",
        "Autarchy Tomb",
        "Neat Footprints in Patrol Patterns",
    ),
    (
        "2d4 Leopard Worms",
        "Hide in Undergrowth",
        "Half-Eaten Animal Encased in Glue-Spit",
    ),
    (
        "2d6 Lizard Lions",
        "Sun-Kissed Basking Rock",
        "Large Shed Lizard Skin",
    ),
    (
        "2d8 Luxfoe Beetles",
        "Sleep Inside Hollow Tree",
        "Shard of Beetle Carapace",
    ),
    (
        "D4 Magneticrabs",
        "Shapeless Metal Wreckage",
        "Torn-Apart Synth Corpse",
    ),
    (
        "D4 Maladaptors",
        "Ruined Cybernetics Kiosk",
        "Subsonic Dirge",
    ),
    (
        "2d6 Memory Eaters",
        "Ruined Library",
        "Skull with Holes Bored Through It",
    ),
    (
        "D4 Metamorphic Sludges",
        "Dried up Well",
        "Hideously Mutated Corpse",
    ),
    (
        "2d4 Moonbeast Imagos",
        "Monolithic Black Outpost",
        "Blasphemous Warning Idols",
    ),
    (
        "2d8 Negativfolk",
        "Inverted Negativhuts",
        "Hear Backwards Speech",
    ),
    (
        "2d8 Nerve Crawlers",
        "Abandoned Hegemony Outpost",
        "Length of Silvery Pseudo-Neural Tissue",
    ),
    (
        "3d6 Nomes",
        "Weird Candy-Striped Hive",
        "Nomish Petroglyphs on Rocks",
    ),
    (
        "Oblivion Obelisk",
        "Amidst Lesser Monoliths",
        "Hear Songs of the Oblivion Heralds",
    ),
    (
        "Occulith",
        "Amidst Petrified Forest",
        "Lifelike Statues of Screaming People",
    ),
    (
        "D4 Parched Man’s Snares",
        "Seemingly Placid Water",
        "Drag Marks by Water’s Edge",
    ),
    (
        "2d4 Phase Panthers",
        "Lair Inside Solid Object",
        "Pile of Out Of Phase Dung",
    ),
    (
        "6d6 Phthalo-Jackals",
        "Shallow Dens",
        "Hear Distant Howling",
    ),
    (
        "4d8 Piranaha Moles",
        "Hidden Burrows",
        "Corpse Chewed to the Bone at Shins",
    ),
    (
        "2d6 Planeyfolk",
        "Hypergeometric Building",
        "Shards of 2D Pottery",
    ),
    (
        "2d6 Plated Beetles",
        "Nest Amongst Shrubs",
        "Find Large Egg-Sacs",
    ),
    (
        "D4 Pontiff Scorpions",
        "Shaded Burrow",
        "Shed Crimson Exoskeleton",
    ),
    (
        "2d4 Pseudo-Giants",
        "Hillside Cave",
        "Remains of a Skiff, Stomped to Pieces",
    ),
    (
        "Psyche Leech",
        "Ruins of Mystic’s Sanctum",
        "Unsettling Psychic Screams",
    ),
    (
        "2d6 Psy-Owls",
        "Burrows in Sand",
        "Hear Soft Hooting",
    ),
    (
        "Quicksilver Exterminator",
        "Ruined Containment Facility",
        "Laser-Scarred Rocks",
    ),
    (
        "2d6 Quill-Spiders",
        "Burrows in Sand",
        "Antelope, Limping, Leg Full of Quills",
    ),
    (
        "2d6 Regenerators",
        "Human-Skin Tents",
        "Crude Idols Made of Bones",
    ),
    (
        "D4 Rustaceans",
        "Mound of Rusted Metal",
        "Dead Synth, Rusted to Pieces",
    ),
    (
        "Scintillating Swarm",
        "Burrowed in Open Sands",
        "Single Dead Golden ‘Coin’",
    ),
    (
        "D4 Scytheslivers",
        "Ruins of Hypergeometric Forge",
        "Corpse Cut With Impossible Precision",
    ),
    (
        "2d6 Spambots",
        "Ruined Customer Service Depot",
        "Advertising Slogans Scrawled in Blood",
    ),
    (
        "D3 Spectres of Indifference",
        "Near Flickering Paradox Gateway",
        "Blankly Staring Victim, Mind Erased",
    ),
    (
        "Sphinx",
        "Ruins of Oracle’s Sanctum (P.Xx)",
        "Xx",
    ),
    (
        "D4 Star Vampires",
        "Near Cyclopean Monolith",
        "Blood-Drained Corpse",
    ),
    (
        "2d6 Stumbling Drones",
        "Hibernate in Decrepit Fort",
        "Unsteady Tracks in Sand",
    ),
    (
        "3d6 Squishwolves",
        "Cave Accessible Through Tiny Crack ",
        "Wet Slimy Pawprints",
    ),
    (
        "D4 Subtle Stalkers",
        "Lurk near Waterhole",
        "Sharp Tracks in Dirt",
    ),
    (
        "2d8 Synth Skeletons",
        "Ruined Synth-Repair Station",
        "Discarded Synth Limb",
    ),
    (
        "Tarantella",
        "Nest Beneath Ruined Dancehall",
        "Footprints of Dancing Victims",
    ),
    (
        "Thermasaur",
        "Unnaturally Frozen Oasis",
        "Flash-Frozen Corpse",
    ),
    (
        "D6 Thornthrower Cacti",
        "Disguised Amidst Regular Cacti",
        "Corpse with Spines in Their Throat",
    ),
    (
        "Thunderstrike Bird",
        "Roosts on Mesa",
        "Huge Tar-Black Feather",
    ),
    (
        "3d6 Tiger Flies",
        "Tall Papery Nest",
        "Tell-Tale Buzzing",
    ),
    (
        "2d6 Troika",
        "Roam Constantly in Open Desert",
        "Cartwheeling Tracks in Sand",
    ),
    (
        "2d6 Tumblesnares",
        "Hidden Beneath Sand",
        "Bloodstained Tumble-Marks",
    ),
    (
        "Turretwright",
        "Scrapyard",
        "Non-Functional Gun Turret",
    ),
    (
        "4d6 Unicorns",
        "Nests in Garbage Heaps",
        "Glittery White Dung",
    ),
    (
        "Viridian Ooze",
        "Hazardous Waste Containment",
        "Area Totally Scoured of Biological Matter",
    ),
    (
        "Void Dragon",
        "Beneath Random Ruin (P.Xx)",
        "Trade Caravan Burned by Apocalypse Beam",
    ),
    (
        "2d6 Voltworms",
        "Disused Cable Relay",
        "Electrical Charge in the Air",
    ),
    (
        "2d4 Walking Wombs",
        "Foul-Smelling Sinkhole",
        "Wide Dragging Tracksin the Sand",
    ),
    (
        "D4 Xanthous Mycomorphs",
        "Fungal Thicket",
        "Yellow Spores on the Wind",
    ),
    (
        "2d10 Xeric Triffids",
        "Root Themselves by Goat Path",
        "Spit-Blinded Fox Stumbles in Circles",
    ),
    (
        "4d6 Yurlings",
        "Nest Amongst Orbital Debris",
        "Scrap Metal with Signature Bite-Marks",
    ),
    (
        "2d10 Zoanthropes",
        "Sleep Inside Abandoned Vehicle",
        "Tracks Show Humans Walking on All Fours",
    ),
)


@dataclass
class Lair:
    inhabitants: str
    location: str
    omen: str

    def __repr__(self):
        return f"""{self.location.capitalize()} occupied by  {self.inhabitants}.
        <br>
        Omen: {self.omen.lower()}.
        """


def gen_lair():
    data = [choice(lair_data)[k] for k in range(3)]
    return Lair(*data)
