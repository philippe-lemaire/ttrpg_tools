byway_environment = {
    0: (
        "Footpath worn into the cave oor.",
        "Skittering in the dark. A pitiful whimper.",
    ),
    1: (
        "Metal railways, abandoned subway cars.",
        "A manual railway handcar, in need of repair.",
    ),
    2: (
        "Reective crystal clusters and columns.",
        "Tight paths and sharp, threatening edges.",
    ),
    3: (
        "A metal grate walkway hangs over vast emptiness.",
        "Broken, fallen platform. Other end is visible.",
    ),
    4: (
        "Wet, slippery paths wind between hot springs, bubbling pleasantly.",
        "Rank sulfur geysers erupt in unexpected places. The steam is putrid and choking.",
    ),
    5: ("Churning rush of an underground river.", "The only way forward is by boat."),
    6: (
        "Sweet, nutty spores waft down from a fungal forest.",
        "Bifurcating paths and false echoes in the fungal wood make it easy to get lost.",
    ),
    7: (
        "A smooth, obsidian tunnel. Searing heat sizzles through yellowed cracks.",
        "Pools of scorching lava rise, the threatening re growls over the melting stone.",
    ),
    8: (
        "Ice-sculpted bridges cross glacial crevices.",
        "Icicles drip. Thin ice cracks under heavy feet.",
    ),
    9: (
        "An elongated cemetery of worn headstones.",
        "Imago unearth the dead in search of chalk",
    ),
}

illuminations = (
    "Streetlights jut out from rock walls, overgrown with stalactites.",
    "Patches of bioluminescent mushrooms stud the earthen ceilings.",
    "Blue-white glowgourds grow upon trellises, illuminating other crops.",
    "Bands of harsh white LEDs at regular intervals.",
    "A squealing orb of yellow light is shackled to a mechanical rail. It zips back and forth, following any movement.",
    "Pyrotech Ants (pg. 10) toil about, scorching the ground with their orange, aming footsteps.",
    "Hot gas mantles sizzle and pop. The cast iron posts and lanterns remain pristine, ageless and cackling.",
    "Many blinking red lights icker, unsynchronized. If touched, the holo-projectors whirr to life, casting a bright holographic spectacle.",
    "Large cyborg pill bugs with headlights build a stone structure.",
    "A river glimmers with inviting cyan pulsations, like a heartbeat.",
)


settlement_sizes = (
    "Long-term Encampment",
    "Clusters of Homes",
    "Lively Village Commons",
    "Complex Cultural Edifices",
    "Bustling town",
)

settlement_citizens = (
    "Concentrate on survival",
    "Cater ot explorer types for trade",
    "Keen to progress",
    "Unethical problem solving",
    "Shun outsiders",
)

settlement_leaders = (
    "Seeking to recruit town members",
    "Eager for Intel on other settlements",
    "Uninterested in outsider opinions",
    "Labor alongside their fellows",
    "Recently died",
)

settlement_tech = (
    "Adept cave-farm techniques",
    "False sun burns bright overhead",
    "Revived Robo snidely assists",
    "Maze of chalk machinery",
    "Scavenged tools",
)

settlement_sites_former_use = (
    "Orbital bombardment silo",
    "Black ops R&D labs and habitat",
    "Slash and burn fungal forest",
    "Servers for a vast intelligence",
    "Water treatment",
)

guilds_mostly = (
    "Cloudlings",
    "Unseen Citizens",
    "Farmelings",
    "Mystling group",
    "A healthy mix",
)

guilds_map_quality = (
    "Out of date",
    "Worn path to Settlement",
    "Direction out",
    "Perfect for five points from Post",
    "To Another Post",
)

guilds_superstition = (
    "Spit-handshake",
    "Trust no one who has no toes",
    "Wear six rings",
    "Hold breath entering doors",
    "Tends small plant",
)

guilds_job = (
    "Map to new Post",
    "Barter passage past Mystlings",
    "Guide Lordling",
    "Remove deadly obstacle in path",
    "Find Lost Team",
)

guilds_pay = (
    "Map to Surface",
    "Advanced medical care",
    "Map to Gate",
    "Guild member application fees",
    "Chalk deposit",
)

mystling_size_and_shape = (
    "Human norm",
    "Gourd-sized",
    "Insectile lower body",
    "Tree-like",
    "Multi-limbed torso",
)

mystling_head = (
    "Human norm",
    "Mantis-like eyes",
    "Large leathery prehensile ears",
    "U-shaped skull",
    "Squid-like mounth parts",
)

mystling_features = (
    "Human norm",
    "Bioluminescent",
    "Horns or antlers instead of hair",
    "Chameleon Skin",
    "Polyp-fungal growths",
)

mystling_want = (
    "Directions",
    "Human connection",
    "Your stuff. Trade of Theft?",
    "Chalk",
    "You for dinner. Invite or Threat?",
)

mystling_have = (
    "A meal to share",
    "Old tech that needs repair",
    "Small collection of spells",
    "Deadly weapons",
    "Their clothes and an illness",
)


cavern_dict = {
    1: """<u>Farmerling Mine</u>: Roll on the Forgotten Mines Table. Farmerlings pry up shattered concrete and sift
through their ndings. One additional Byway descends Deeper. Another follows a string of solar-powered lights
ascending to a village; <b>roll on the Exit from the Unseen City table (pg. 9)</b>.""",
    2: """<b>Carved Marble Palace:</b> Ornamental fountains trickle, misting the lifelike statues of beautiful men.
Column-lled aisles connect at right angles to the decadent throne room of the False Queen. She showers PCs
with palatial hospitality, if they agree to enact her will.""",
    3: """<u>Geothermal Power Station</u>: Spitting pipes and orange sodium-vapor lamps lead to rooms where whistling
steam engines shriek. Roll 1d10. On 7-9, the machine is about to blow, cutting energy from the nearest
Settlement. There is a Gate here (pg. 12) and one additional Byway leads Deeper.""",
    4: """<b>Desert of the Broken Sun</b>: A churning false sun bakes stone walls dry. While traversing this underground
desert, an additional Provision must be consumed to avoid the eects of hunger. Body Save, or become painfully
sunburnt for 1d5 days.""",
    5: """<u>Mystling Village</u>: Roll on Mystling and Settlement tables (pg.11) to create this community. Mystlings are
Unseen Citizens; some have never seen a Farmerling.""",
    6: """<u>Exhausted Mine</u>: Roll on the Forgotten Mines table. Liftless pits, buckling rafters, and the odor of rotten
eggs. Anything useful left? One additional Byway heads Deeper.""",
    7: """<u>Subway Depot</u>: On the tracks, train cars like hollow bones house exiled Mystlings (nearby Settlement).
Sellswords “protect” a Lordling from the meager pleas of a skinny Mystling. All connecting Byways are subway
tunnels, one additional Byway leads Deeper.""",
    8: """<u>Housing Megacomplex</u>: Roll on the Settlements Table (pg. 11). Glowing violet insects the size of carriages
(Holo-bandits, pg.10) guard the tower blocks’ courtyards.""",
    9: """<b>Fungal Forest</b>: Wet and moldy like an old sponge, the air swims with spores. A dense green canopy glows,
turning purple deeper within. The Children of the Spore leave trails for the lost. An additional Byway leads
Deeper into another Fungal Forest.""",
    10: """<b>Galak’s Peak</b> (Adventure Location): The upper tip of a skyscraper-sized snail’s shell pierces the cavern oor. No Byways.""",
    11: """<u>Riverside Guildhouse Post</u>: This Guildhouse oers boats to travel the Unseen City’s deadly rivers. Roll
1d5. On 1-2, a river Byway passes this many Caverns before arriving at another Riverside Guildhouse Post. On
3-5, the river disappears underground.""",
    12: """<u>Exiled Mystling Magician Hut</u>: Roll on the Mystling table (pg.11). They help the unmagical obtain what
they want, yet only once. Those they bewitch must face the consequences of their desires.""",
    13: """<u>Gate Church</u>: Roll on the Settlement Table (pg. 11). A grand circle entrance emulating the Gates seen
throughout the Byways. Gate Priests reward conrmed Gate locations, and oer even more for an escort to a
Gate.""",
    14: """<u>Excavated Mining Pit</u>: Storeys of rotted planks, ladders and rails descend, giving way to branching, fruitless shafts deep into the earth like gouged out roots. One Byway leads 1d5 Levels Deeper.""",
    15: """<u>Wet, freshly bored tunnels</u>: Imago blood or oil teases the nostrils. 1d10 Guild members run in terror from
either 3d10 Imago or the tunnel-boring Razor Wyrm.""",
    16: """<b>Sunken Cathedral</b>: Firelight aglow in the rose window, towers and saints carved into the bedrock, and a
morose chanting song echoes from within.""",
    17: """<u>Hibernating Imago Den</u>: Tremors of the walls are the sleeping brown carapaces of 3d100 Hibernating
juvenile Imago, in clusters. Wake if chalk is exposed.""",
    18: """<u>Dangerous Mystling Lair</u>: A fence of masks block the path. Past a lychgate built of bones and skulls, a
freshly painted white house glimmers in the light of a sunken repit. Roll on the Mystling table (pg. 11).""",
    19: """<u>Unseen Citizen Hall</u>: 1d10 Holo-bandits set re to an arriving caravan, attempting to steal a massive
mining haul. Roll on the Guild and Settlement tables (pg. 11) and combine the results to create an Unseen
Citizen Hall.""",
    20: """<u>Active Mystling Mine</u>: The creaking drone of lift shafts, and the ringing of hammers and pickaxes echoes
up from deep in the tunnels. Roll on the Mystling table (pg. 11). An attentive, protective escort accompanies the
PCs during their transit through the mines. An additional Byway leads Deeper.""",
    21: """<u>Smelting Works</u>: Acrid fumes zzle forth from amber brilliance. A False Sun has been pulled from above,
used for smelting ore. Roll on the Settlement table (pg. 11).""",
    22: """<u>Smuggler’s Den</u>: Roll on Guilds table (pg. 11). A crowd shouts around the edges of a sinkhole covered with
a grimy chain-link fence. Within, a tall Farmerling takes betting cards on how many live Rat Grubs their trained
Bathound can catch unharmed in a minute.""",
    23: """<u>Mystling Vault</u>: Poor souls locked away for untold time. Roll on the Mystling (pg. 11) and Environment
tables (pg. 6) for this Cavern and following Byways. An additional Byway leads Deeper.""",
    24: """<u>Abandoned Imago Temple</u>: Was this built for the great bugs or by them? Should the PCs rest here, Imago
descend upon the Temple while they sleep.""",
    25: """<b>The Lid of the World</b>: The Fellowship of the Sunset Imago welcomes travelers to rest within their walls.
They serve hot soup, oer medical aid, and space to rest, free of charge. Once a year, they open the doors to the
Lid for explorers to venture into the Heart of the World.""",
}

cavern_departing_byways = {
    1: "1 Byway departs, ending at a cave-in.",
    5: "1 Byway departs to another Cavern.",
    9: "2 Byways depart to different Caverns.",
    10: "1 Byway leads Higher; 1 Byway departs to another Cavern.",
}

forgotten_mines = (
    "Luminous Coralstone",
    "Singing Crystals",
    "Dancing patterns undulated in Marble",
    "Lines of copper wiring",
    "Shipping containers of space ore rusted shut",
    "A derelict’s steel plating",
    "Crumbled concrete ruins over old tech",
    "Ancient computers",
    "Chalked remains of the unknown dead",
    "An Imago tomb",
)
