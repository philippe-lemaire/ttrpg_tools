camp_types = (
    "Ancient Ruins",
    "Dungeons",
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
dungeons_events = dict()
events_dicts = (ancient_ruins_events, dungeons_events)
camp_events_table = {k: v for k, v in zip(camp_types, events_dicts)}
