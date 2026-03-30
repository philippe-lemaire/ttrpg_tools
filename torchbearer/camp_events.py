camp_types = (
    "Ancient Ruins",
    "Dungeons",
    "Natural Caves",
    "Outside of or Near Town",
    "Squatting in Town",
    "Wilderness",
)


ancient_ruins_events = {
    1: "<em>Collapse.</em> This ancient structure can bear no more grief. It collapses with a mournful sigh. Nothing can be done to prevent this. Camp ends, remain in adventure phase.",
    2: "<em>Pits of despair.</em> The flooring has eroded and gives way under your weight. The party is dumped into a dungeon or natural cave system below. The watch cannot prevent this disaster. Camp ends, remain in adventure phase.",
    3: "<em>Terror.</em> This place is haunted by screaming terrors which emerge howling from your nightmares. What could the watch possibly do to prevent this? Test Will against Ob 8 to remain sane. Suggested failure result: afraid. Camp ends, remain in adventure phase.",
    4: "<em>Lair.</em> This entire ruin is the lair for some indescribable fell entity, and you are perched in its maw. If you set watch, the watch may spend a check to make a test to escape before being swallowed or engage in a conflict to avert the disaster. Otherwise, remain in adventure phase as camp ends and your packs, sacks and animals slide to their doom.",
    5: "<em>Cursed.</em> One of your number becomes entangled in evil magic: They suffer -1s to all actions until the curse is removed. The one affected is: the first to enter, the first to eat or drink, the first to speak, or the first to leave (game master’s choice).",
    6: "<em>Wild magic and strange gods.</em> Memorizing a spell in this place will burn the spell out of your spell book. If an attempt at purification fails, it will backfire and increase Immortal burden by margin of failure instead of decreasing it. Also, theurges and magicians suffer a +1 Ob penalty to cast spells and perform invocations during this camp phase.",
    7: """<em>Strange corrosion.</em> One piece of gear rusts, rots or crumbles
away in the night. Roll randomly to select the player. Roll 1d6 to
determine gear from one of the following inventory locations:
<table class="table">
<tr>
<td>1</td>
<td>Torso</td>
<td>4</td>
<td>Pouch</td>
</tr>
<tr>
<td>2</td>
<td>Belt</td>
<td>5</td>
<td>Pack or satchel</td>
</tr>
<tr>
<td>3</td>
<td>Head</td>
<td>6</td>
<td>Feet</td>
</tr>
</table>
""",
    8: "<em>Pestilence.</em> Your food bursts with maggots, water turns to piss and wine turns to blood.",
    9: "<em>Whispers.</em> Strange voices speak to those who close their eyes: +1 Ob to recover from afraid and exhausted during this camp.",
    10: "<em>Penetrating chill.</em> The air of the ruin —and the very stone itself— emanates a sharp chill: +1 Ob to recover from sick and injured during this camp phase.",
    11: "<em>Safe camp.</em>",
    12: "<em>Safe camp.</em>",
    13: "<em>Rare herbs.</em> The flora of this place can be harvested to make healing poultices that grant +1D to Healer tests.",
    14: "<em>Mirror font.</em> Drinking the cool water from this glass-like font grants +1D to recover from angry and afraid. Roll 1d6 for every draught taken. On a 1, the font’s potency is expended.",
    15: "<em>Ancient engravings.</em> You may spend a check to make an Ob 6 Scholar test to decipher these ancient engravings. If successful, roll on the Tome of Ancient Lore Loot subtable.",
    16: "<em>Shrine of the Immortals.</em> Behold an ancient shrine, untouched by the ravages of time and chaos. Magicians do not need to spend a check to memorize spells; shamans and theurges do not need to spend a check for purification rituals.",
    17: "<em>Sanctuary.</em> This ruin still holds ancient magic and will shelter up to eight from weather and cold: +1D to recover from all conditions when camping in this sanctuary.",
    18: "<em>Votive statues.</em> You discover lost treasures. Roll on the Works of Art Loot subtable in the Lore Master’s Manual.",
    19: "<em>Artifact.</em> Hidden within this forgotten place is a welter of ephemera. Roll on the Magic Loot subtable.",
    20: "<em>Impossible distances.</em> Stepping into an inky black portal within this ruin will transport you to another doorway from your past. However, one item on your person always disappears before you emerge from the other side.",
}
dungeons_events = {
    0: "<em>Flood.</em> The room rapidly fills with filthy, swirling water. If you set watch, make tests to get to safety or to save packs and gear. Otherwise, remain in adventure phase as camp ends as packs and gear are lost in the torrent.",
    1: "<em>Roof or floor collapses.</em> If you set watch, they may spend a check to test to lead the group to safety. If no watch, remain in adventure phase as camp ends and packs, sacks and animals are all crushed.",
    2: "<em>Foul vapors.</em> The inviting place you’ve picked to camp is suffused with foul vapors. No watch will save you. Camp ends as you flee choking. Remain in adventure phase.",
    3: """<em>Monsters attack.</em> If you set watch, the watch may spend a check to
make a test or engage in a conflict to avert the disaster. Otherwise,
remain in adventure phase as camp ends and you flee or combat the
interlopers. Roll 1d6 for interlopers:
<table class="table">
<tr>
<td>1</td>
<td>Oozes (1d3)</td>
<td>3-4</td>
<td>Troll Rats (2d6)</td>
</tr>
<tr>
<td>2</td>
<td>Goblins (3d6)</td>
<td>5-6</td>
<td>Strixes (2d6)</td>
</tr>
</table>""",
    4: """<em>Curiosity.</em> The commotion of your camp draws the attention of a
curious creature. If you set watch, the watch may spend a check to
attempt to trick or drive away the creature. If the watch cannot drive
them away, remain in adventure phase. Roll 1d6 for creature:
<table class="table">
<tr>
<td>1</td>
<td>Black Dragon</td>
<td>3-5</td>
<td>Stone Spider</td>
</tr>
<tr>
<td>2</td>
<td>Troll Haunt</td>
<td>6</td>
<td>Owl Bear</td>
</tr>
</table>""",
    5: "<em>Vermin.</em> Vermin get into one character’s pack and ruin their rations (game master’s choice). Roll 1d6 for amount ruined.",
    6: "<em>Offal.</em> This camp is surrounded by filth and waste left by vermin and other foul creatures: All suffer +1 Ob to recover from sick. In addition, injured characters must make an Ob 3 Health test. Suggested failure: sick condition or a twist that their wound becomes infected and may not be treated by the Healer skill.",
    7: "<em>Breakage.</em> During your travails, 1d3 of your bottles, jugs, pots, flasks and vials were crushed. The game master distributes the damage as appropriate.",
    8: "<em>Dust.</em> You disturb a thick layer of dust while making camp: +1 Ob to all tests during this camp phase.",
    9: "<em>Wear and tear.</em> Something ripped a hole in your pack, and a piece of gear dropped out. Roll randomly for the character. They lose the object in the bottom-most slot(s) of their backpack or satchel.",
    10: "<em>Safe camp.</em>",
    11: "<em>Safe and sound.</em> You’re able to thoroughly secure the entrances to your camp, making you feel at ease+1D to recover from exhausted and afraid during this camp phase.",
    12: "<em>Clear water.</em> The site you pick has a ready source of potable water from an old well, broken pipe or basin formed by seepage. It provides three draughts of water during each camp phase.",
    13: "<em>Luck.</em> You find an old leather pouch containing coins of various provenance worth 2D (pack 1).",
    14: "<em>Fungus.</em> You find a patch of glowing fungi. If picked, each stalk acts as a candle or as cooking supplies. There are 1d6 stalks.",
    15: "<em>Gear.</em> You find a serviceable piece of gear. Roll on the Gear subtable in the Loot chapter.",
    16: "<em>Connections.</em> You find a secret entrance into another section of the dungeon.",
    17: "<em>Treasure.</em> One of the flagstones is loose. Beneath it you find treasure! Roll on the Treasure & Valuables subtable 1.",
    18: "<em>Antiquity.</em> You discover the entrance to a lost, sunken temple. During this camp phase, all may remove the sick or injured conditions and reduce Immortal burden by 1. In addition, the lost temple grants a +2D bonus to purification rituals (instead of the standard +1D). Should you return to this camp, the lost temple’s magics are expended and no longer cure conditions or burden, but the purification bonus remains.",
    19: "<em>Etchings.</em> Wiping away the dust in this room, you find a series of petroglyphs. Roll on the Tome of Ancient Lore subtable in the Loot chapter.",
    20: "<em>Death grip.</em> A skeleton lies in a heap in the corner. It’s clutching something. Roll on the Magic subtable in the Loot chapter.",
}

natural_caves_events = {
    0: "<em>Cave-in.</em> The area you’re camping in is obliterated. If you set watch, they may spend a check to make a test to sound the alarm and get the group to safety. Otherwise, remain in the adventure phase as camp ends as you scramble to safety, and all packs and gear are destroyed in the chaos. Run!",
    1: """<em>Lair.</em> This cave is the lair of something terrifying. If you set watch, they may spend a check to drive off the creature. Otherwise, remain in adventure phase as camp ends and you flee in terror. Roll 1d6 to determine whose lair it is:
<table class="table">
<tr>
    <td>1</td>
    <td>Red dragon</td>
    <td>4</td>
    <td>Owlbear</td>
</tr>
<tr>
    <td>2</td>
    <td>Black dragon</td>
    <td>5</td>
    <td>Linnorm</td>
</tr>
<tr>
    <td>3</td>
    <td>Manticore</td>
    <td>6</td>
    <td>Troll bear</td>
</tr>
</table>
""",
    2: "<em>Rock fall.</em> One of the passages leading to your camp site collapses in a shower of stone and dirt. If there was just one passage, you best have set a watch. If you set watch, the watch may spend a check to make a test to drag you to safety before the way is sealed. If no watch, remain in adventure phase: You’re trapped.",
    3: "<em>Flood.</em> Torrential rain on the surface causes a flood below. If you set watch, they may spend a check to sound the alarm and get you to safety. Otherwise, remain in adventure phase as camp ends and your packs and gear float off in the torrent and the water continues to rise.",
    4: "<em>Foul air.</em> The air here quickly goes stale and you all begin to asphyxiate. If you set watch, they may spend a check to vent the air or get the group to safety. Otherwise, remain in adventure phase as camp ends and your eyes bulge and tongue swells as you choke on fumes.",
    5: """<em>Raid.</em> A bold group of subterranean denizens raids your camp seeking food or captives. If you set watch, the watch may spend a check to confront the raiders. Otherwise, remain in the adventure phase as camp ends and chaos erupts. Roll 1d6:
<table class="table">
<tr>
    <td>1-2</td>
    <td>Kobolds (2d6)</td>
    <td>5</td>
    <td>Troll Bats (3d6)</td>
</tr>
<tr>
    <td>3-4</td>
    <td>Goblins (2d6)</td>
    <td>6</td>
    <td>Orcs (2d6)</td>
</tr>
</table>
""",
    6: "<em>Bad temperature.</em> Extreme cold (or heat in hot caves) makes you uncomfortable: +1 Ob to all tests during this camp phase.",
    7: "<em>Lost.</em> Lose your bearings while you rest. After breaking camp, you must test Cartographer or Dungeoneer to get back on track.",
    8: "<em>Damp.</em> Cloying moisture soaks clothing and gear. You may not recover from the exhausted condition during this camp phase.",
    9: "<em>Claustrophobia.</em> The tight space and the rock above starts to weigh on you. You suffer a +1 Ob penalty to recover from angry and afraid during this camp phase.",
    10: "<em>Unlucky.</em> One character drops a carried a item and it either breaks or disappears down a crevasse. Game master chooses.",
    11: "<em>Safe camp.</em>",
    12: "<em>Safe camp.</em>",
    13: "<em>Cache.</em> You stumble upon a cache of torches or rope left by previous explorers. Roll 1d6 to determine the number of items left behind.",
    14: "<em>Fungus.</em> You find a patch of edible fungi here. Each stalk acts as a unit of forage or as supplies for Cook tests. There are 1d3 stalks.",
    15: "<em>Creature comfort.</em> The site you pick is dry and comfortable: +1D to recover from exhausted during this camp phase.",
    16: "<em>Dictionary.</em> This site has magnificent speleothems to look at (draperies, curtains, stalactites, stalagmites, cave crystals, etc.): +1D to recover from angry and afraid during this camp phase.",
    17: "<em>Spring.</em> You find a clear, cold spring bubbling through a crack in the rocks. It can provide four draughts of water during each camp phase.",
    18: "<em>Remains.</em> You find the remains of a less fortunate explorer clutching a bit of marked up leather between their finger bones. Roll on the Books & Maps subtable in the Loot chapter.",
    19: "<em>Gem cluster.</em> You find a cluster of gems glinting among the rock formations. Roll on the Gems Loot subtable.",
    20: "<em>Basin.</em> You find a naturally occurring basin of water with healing properties: Each draught grants +2D to recover from sick or injured. There is enough water for three draughts. It may be stored in a container and carried away.",
}

outside_of_or_near_town_events = {
    1: "Brushfire (or blizzard). Run. If you set watch, they may spend a check to make a test to sound the alarm to get the group to safety. Otherwise, remain in adventure phase as camp ends and all packs and animals are lost.",
    2: "<em>Bad weather. Without shelter, you’re too exposed. If you have shelter and set a watch, the watch may spend a check to test to get everyone under cover (or hold down the shelter from blowing away). Otherwise, remain in adventure phase as camp ends and your possessions whirl away in the winds.",
    3: """<em>Raiding beasts.</em> The raiders who claw at the walls of civilization stumble into your camp. If you set watch, the watch can spend a check to attempt to kill or drive off the raiders. If no watch, camp ends as a conflict erupts with the raiders attempting to capture the adventurers. Roll 1d6 to discover who your new friends are:
<table class='table'>
<tr>
    <td>1-2</td>
    <td>Dragefolk raiders (2d6)</td>
    <td>5</td>
    <td>Hobgoblins (2d6)</td>
</tr>
<tr>
    <td>3-4</td>
    <td>Gnolls (2d3)</td>
    <td>6</td>
    <td>Bugbears (2d3)</td>
</tr>
</table>""",
    4: "<em>Bandits.</em> A group of 2d6 bandits surround the camp or attempt to ambush the group. If you set watch, the watch may spend a check to make a test or engage in a conflict to keep the peace. Otherwise, remain in adventure phase as camp ends as the bandits politely insist you donate food and coin to their cause.",
    5: "<em>Trespassing.</em> You’re camping on someone’s land. The local authorities summon knights, warriors or huscarls to perform their duties and see you off (always twice the number of the adventurers). If you set watch, the watch may spend a check to test to see off these annoying busybodies. If not, remain in adventure phase as camp ends as you are forced to deal with this distraction.",
    6: "<em>Traps.</em> You run afoul of some rather formidable animal traps laid in the area. If you set watch, the watch may spend a check to detect or disarm these snares. Otherwise, remain in adventure phase as camp ends as you’re ensnared and trapped.",
    7: "<em>Fouled stream.</em> Local industry has fouled this stream, making it undrinkable. Any who drink it must make an Ob 3 Health test. Suggested condition: sick; or twist: you cannot hold down food and liquid until treated by a healer.",
    8: "<em>Barren lands.</em> This area has been hunted and foraged clean. There’s nothing edible to be had for miles: you may not make Hunter or Scavenger tests when camping in this area.",
    9: "<em>Hanged man.</em> There’s a corpse hanging from a tree nearby, full of ill omen. You cannot recover from the angry or afraid conditions while camping in this area.",
    10: "<em>Burial mound.</em> This place is full of ghosts. Memorizing spells and purifying burden is impossible while camping in this area.",
    11: "<em>Safe camp.</em>",
    12: "<em>Safe camp.</em>",
    13: "<em>Midden.</em> You camp near a massive pile of garbage: +1D to Scavenger tests to find wilderness and town items while camping in this area.",
    14: "<em>Sympathetic children.</em> The local farm kids leave out portions of food and wine for you all.",
    15: "<em>Fell off the wagon.</em> You find a useful item by the side of the road. Roll on the Gear subtable in the Loot chapter.",
    16: "<em>Domesticated beasts.</em> There are herds and flocks in these precincts: +1D to Hunter tests during this camp phase. But don’t let the farmers catch you.",
    17: "<em>Fruit-bearing trees.</em> If the Immortals didn’t want you to eat this fruit, they shouldn’t have planted these orchards here in nice neat rows. The group may collect 2d6 portions of forage.",
    18: "<em>Abandoned structure.</em> You find an abandoned house or barn: +1D to all recovery tests when camping in this quaint structure.",
    19: "<em>Friendly camp.</em> A like-minded group of adventurers have taken up residence here. They offer to share their fire and wine with you, and they’ll feed any who look put out. Once everyone is settled, they share a rumor from the Tavern Rumors table. The adventurers are equal to the party’s highest level plus one. Hopefully, you’ll return the favor some day.",
    20: "<em>Shelter.</em> This place is comfortable, hidden and sheltered from weather and prying eyes. When you return to this place to camp, you are granted a +1 bonus to the Near Town Camp Events table in addition to other bonuses.",
}

squatting_in_town_events = {
    1: "<em>Fire.</em> Someone or something sets fire to the place (it certainly was not your sputtering hobo fire). If you set watch, the watch may spend a check to douse the incipient inferno. Otherwise, remain in adventure phase as camp ends and this place is destroyed and may not be used further as a camp.",
    2: """<em>Collapse.</em> This old structure can handle no more abuse. It comes down on your heads with a relieved moan. If you set watch, the watch may spend a check to drag you to safety. If no watch, remain in adventure phase as camp ends as your packs and gear are buried in the rubble. Either way the structure is destroyed and may not be used further as a camp. 3Late night lurker. Something sinister slinks into to the structure late at night. If you set watch, the watch may spend a check to make a test to drive off the interlopers. Otherwise, remain in adventure phase as camp ends and you find yourself in a sticky situation. Roll 1d6 to determine what lurks in ze night:
<table class='table'>
<tr>
    <td>1-2</td>
    <td>Ghouls (1d2+1)</td>
    <td>5</td>
    <td>Wererats (1d6)</td>
</tr><tr>
    <td>3-4</td>
    <td>Strixes (2d6)</td>
    <td>6</td>
    <td>Sprikken (1d3)</td>
</tr>
</table>
""",
    4: "<em>Eviction.</em> The town watch comes to evict you (and also collect on any debts you might owe). The town watch sends three times as many thugs (see the Denizens chapter for stats) as squatters. If you set watch, the watch may spend a check to make a test to send away these irksome roustabouts. Otherwise, remain in adventure phase as camp ends and negotiations begin. How fun.",
    5: "<em>Feculence.</em> Some cretin has defiled this place with a substantial pile of human waste. The party cannot recover from sickness in camp. If eating or drinking in camp, make an Ob 2 Health test. Suggested failure: sick condition or a twist that you can’t stomach the stench and vomit (and thus can’t recover from hungry and thirsty during this camp phase). The watch can’t help you here, only the Lords of Fevers and Plagues.",
    6: "<em>Rats.</em> This place is infested with very bold rats. The party cannot recover from afraid or exhausted in camp. In addition, the rats steal the top-most item from one pack or satchel. If you set watch, they may spend a check to test to avert the theft. Otherwise, the rats return their spoils to their king, deep below the town.",
    7: "<em>Decomposing human corpse.</em> Someone has died in here—or perhaps died elsewhere and been dumped here to rot in peace: +1 Ob to recover from afraid and sick while the corpse remains in this area. If the corpse is not removed, future camps in this area suffer a -1 penalty to the camp events roll in addition to other penalties.",
    8: "<em>Drips.</em> The roof leaks or the room floods. Water seeps into your gear, ruining it. Roll 1d6: 1-3: torches (1d3), 4-6: rations (1d3).",
    9: "<em>Mold.</em> The place is home to a wretched mold that causes crushing headaches. The group cannot recover from exhaustion, memorize spells or perform purification rituals while camped in this area.",
    10: "<em>Stench.</em> The locals use this place as a garbage pit. The stench makes it impossible to keep anything down: You cannot alleviate the hungry and thirsty condition in camp, but you are granted +1D to all Scavenger tests.",
    11: """<em>Dalliance.</em> Teenagers use this place for their trysts. If you set watch, the watch may spend a check to make a test to intimidate, persuade or manipulate the impressionable youth. If the group does not pay the check or the test is failed, the teenagers report the incident to their parents or friends in the guilds. Roll 1d6, two teenagers are here to:

<table class='table'>
    <tr>
        <td>1-2</td>
        <td>Consummate a passionate love</td>
    </tr>
    <tr>
        <td>3-4</td>
        <td>Dabble in magic</td>
    </tr>
    <tr>
        <td>5-6</td>
        <td>Play a cruel trick on a friend</td>
    </tr>
</table>
""",
    12: "<em>Safe camp.</em> You are undisturbed, and all is well.",
    13: "<em>Midden.</em> You camp near a massive pile of garbage: +1D to Scavenger tests to find town items while camping in this area.",
    14: "<em>Youth.</em> Children come to explore and play in this structure. You go unnoticed: +1D to recover from angry or afraid.",
    15: """<em>Eavesdropping.</em> You overhear a whispered conversation outside. Roll 1d6 to discern its oddly relevant topic:
<table class='table'>
    <tr>
        <td>1-2</td>
        <td>A cult</td>
        <td>5</td>
        <td>A political matter</td>
    </tr>
    <tr>
        <td>3-4</td>
        <td>A local secret</td>
        <td>6</td>
        <td>One of the town’s guilds</td>
    </tr>
</table>
""",
    16: " <em>Allies.</em> You link up with another band of friendly squatters. They will give food, water or even wine if the group looks put out (they have 1d6 portions total per encounter). Otherwise, they offer to trade rumors. Roll on the Tavern Rumors table with a +1 bonus.",
    17: "<em>Connection.</em> You discover a secret connection (tunnel, canal, catwalk or crawl space) to an adjoining, occupied building.",
    18: "<em>Hidden loot.</em> There’s something buried beneath the floorboards or flagstones. Roll on the Treasure & Valuables 1 subtable.",
    19: """<em>Disembodied eyes.</em> A house goblin is curious about you. Feed it (one fresh or preserved ration), and it will treat you kindly, granting +1D to all recovery tests during the camp phase to the one who feeds it. Once found, the house goblin will remain visible. Should you return to this camp site, you may again opt to feed the house goblin. However, if you fail to feed the house goblin, roll 1d6:
<table class='table'>
    <tr>
        <td>1-4</td>
        <td>The house goblin disturbs your sleep and you are +1 Ob to recover from exhausted, sick or injured</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Steals an object from you</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Revokes its friendship and disappears</td>
    </tr>
</table>""",
    20: "<em>The room.</em> You discover a previously hidden but furnished room from another era that is eerily intact. This squat now counts as a free flophouse if used as accommodations during the town phase.",
}
wilderness_events = {
    0: "<em>Sinkhole.</em> The earth subsides and takes you with it. If you set watch, they may spend a check to make a test to get the group to safety. If you didn’t set watch, enjoy your new underground home, and remain in adventure phase as camp ends.",
    1: "<em>Evil weather.</em> Lightning, wind, rain or snow destroys your shelter and douses your fire. If you set watch, they may spend a check to make a test to save your gear and animals. If no watch, each character loses their pack, an animal or a companion, and remain in adventure phase as camp ends.",
    2: "<em>Falls in the woods.</em> A tree, rock or meteor falls onto your camp. One character must make an Ob 5 Health test. If you set watch, the watch may help the Health test. Suggested failures: injured condition or a twist that their pack is destroyed instead of their skull. Otherwise, remain in adventure phase as camp ends.",
    3: "<em>Gnits.</em> Swarms of biting insects makes camping impossible. No watch can save you against the gnits. Remain in adventure phase as camp ends.",
    4: "<em>Wildfire.</em> Run. This area is ravaged by wildfire. If you set watch, the watch may spend a check to make a test to save packs and gear. Otherwise, all packs and their contents burn, and remain in adventure phase as camp ends. This this area may not be used as a future camp.",
    6: """<em>Wandering monsters.</em> Something wicked this way comes. If you set watch, the watch may spend a check to make a test or engage in a conflict to avert the attack. Otherwise, remain in adventure phase as camp ends with a stand off. Roll 1d6 for friends:
<table class='table'>
    <tr>
        <td>1-2</td>
        <td>Dire wolves (1d6)</td>
        <td>5</td>
        <td>Bugbears (1d6)</td>
    </tr>
    <tr>
        <td>3-4</td>
        <td>Gnolls (2d3)</td>
        <td>6</td>
        <td>Devil boars (1d3)</td>
    </tr>
</table>
""",
    7: "<em>Foul water.</em> No clean water source to be found. If you sought water as a camp amenity, the source is dry or foul.",
    8: "<em>Lost.</em> Lose your bearings while you rest. You must make a Pathfinder or Cartographer test to get back on track. Add the site to your map to find it again.",
    9: "<em>Vermin.</em> Mice or other vermin crawl all over your camp and spoil 2d3 rations.",
    10: "<em>Wear and tear.</em> One character breaks a piece of equipment. Roll randomly for the player. Then roll to determine what is broken or worn out: 1d6 for backpack slot or 1d3 for satchel slot. Multislot items go if either slot is rolled.",
    11: "<em> Safe camp.</em>",
    12: "<em> Safe camp.</em>",
    13: "<em>Lovely view.</em> The site has majestic views: +1D to your next Pathfinder or Cartographer test after camp.",
    14: "<em>Verdant wilderness.</em> Birds, ungulates and fish abound: +1D to Hunter, Scavenger and Fisher tests in camp.",
    15: "<em> Sweet water.</em> This site has a freshwater spring or stream.",
    16: "<em>Game trail.</em> You find an easy trail and are granted +2D to your next Pathfinder or Scout test after breaking camp.",
    17: "<em>Greens.</em> You find a patch of edible plants. If harvested, you collect 2d6 portions of forage.",
    18: "<em> Out of the wind.</em> The site you pick is sheltered from the wind and weather: +1D to recover from angry and exhausted when camping in this area.",
    19: """<em>Fellow traveler.</em> Meet a helpful fellow wanderer. Their level is two higher than the highest-level character. If the highest level is 9, then this is a retired adventurer. If treated with hospitality, the wanderer will share wine, information in the form of warnings, advice relevant to the adventurers’ current endeavor or they will leave a gift (roll on Loot Table 3). Roll 1d6 for class:

<table class='table'>
    <tr>
        <td>1</td>
        <td>Ranger</td>
        <td>4</td>
        <td>Warrior</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Outcast</td>
        <td>5</td>
        <td>Burglar</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Magician</td>
        <td>6</td>
        <td>Theurge</td>
    </tr>


</table>""",
    20: "<em>Standing stones.</em> You find a circle of standing stones or faerie ring. Everyone automatically recovers from the angry and afraid conditions, no tests necessary. The circle remains and may be returned to. After each use, roll 1d6. On a roll of 1, the magic of the place is expended.",
}

events_dicts = (
    ancient_ruins_events,
    dungeons_events,
    natural_caves_events,
    outside_of_or_near_town_events,
    squatting_in_town_events,
    wilderness_events,
)
camp_events_table = {k: v for k, v in zip(camp_types, events_dicts)}
