camp_types = ("Ancient Ruins", "Dungeons", "Natural Caves", "Outside of or Near Town")


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

events_dicts = (
    ancient_ruins_events,
    dungeons_events,
    natural_caves_events,
    outside_of_or_near_town_events,
)
camp_events_table = {k: v for k, v in zip(camp_types, events_dicts)}
