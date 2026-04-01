town_types = (
    "Bustling Metropolis",
    "Busy Crossroad",
    "Dwarven Hall",
    "Elfhome",
    "Religious Bastion",
    "Remote Village",
    "Wizard’s Tower",
)

bustling_metropolis_events = {
    2: "<em>Black plague.</em> This place is a charnel house. Bodies lay piled in the streets. Mark this city as a ruin on your map, say your prayers to the Immortals and move on.",
    3: "<em>Raging fire.</em> This town is in flames. There is no safe place to rest; no market open. Remain in the adventure phase until the fire is put out or dies down or until you move on to another town.",
    4: "<em>Riots.</em> The citizens protest for their rights and the ruling class provokes them to riot. Remain in the adventure phase until the riots subside or until you journey to a new town.",
    5: "<em>Civil war.</em> The populace of this town has split into factions or has taken up arms against its ostensibly allied neighbor. Remain in the adventure phase until the war subsides or until you reach a different town.",
    6: "<em>Festival.</em> The streets are blocked by parades, and the market is closed.",
    7: "<em>New fashion rampant.</em> A fashion craze grips the city. All suffer a +1 Ob penalty to Circles tests until they are wearing the latest fashion (usually finery or its equivalent).",
    8: """<em>New law decreed.</em> Roll 1d6 to determine the type of law:
<table class='table'>
    <tr>
        <td>1-2</td>
        <td>Criminal law (choose one)</td>
        <td>4-5</td>
        <td>Civil law (choose one)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Sumptuary law (choose one)</td>
        <td>6</td>
        <td>Religious law (choose one)</td>
    </tr>
</table>
""",
    9: "<em>Labor strike.</em> The guild hall is closed. No services available.",
    10: "<em>Fad.</em> The city has been taken by a harmless new custom or fad. Everyone in the drinking halls and taverns is complaining about it. The folks at the well gossip about it. Children all envy it.",
    11: """<em>Foreign visitors.</em> Roll 1d6:
<table class='table'>
    <tr>
        <td>1-2</td>
        <td>The town is full of chatter in a new tongue</td>
    </tr>
    <tr>
        <td>3-4</td>
        <td>They are curious about the customs</td>
    </tr>
    <tr>
        <td>5-6</td>
        <td>They apologetically jostle you in the street</td>
    </tr>
""",
    12: """<em>Natural death of a prominent figure.</em> Roll 1d6:
<table class='table'>
    <tr>
        <td>1-2</td>
        <td>They die of old age</td>
    </tr>
    <tr>
        <td>3-4</td>
        <td>They die during childbirth</td>
    </tr>
    <tr>
        <td>5-6</td>
        <td>They die of illness</td>
    </tr>
</table>
""",
    13: "<em>Public performance.</em> Jugglers, boxers and acrobats put on a comical show. The crowd roars with laughter. Make a free test to recover from angry or afraid.",
    14: "<em>A polite request.</em> An impoverished, aging dowager mistakes you for someone else. She sends her ancient servant to politely inquire with you because she needs a gift for a young noble’s upcoming birthday. She can pay with gratitude. Will you create a fine gift for her? Succeed and add a new friend. If the widow is befriended and this result is rolled again, you encounter her and she invites you to stay with her while you are visiting this town.",
    15: "<em>Actually.</em> On the street, you hear a fool prattling on to their lady friend about the nature of the moon and the stars. Tip your hat and correct them using Scholar vs their Scholar 4. Suggested twist: you make a new enemy. If you make an enemy and roll this event again, you encounter them while entering town. No debate necessary!",
    16: """<em>Holy day.</em> The streets are packed with pilgrims and tourists.
<ul>
    <li>Any religious item may be sold for 1D of copper coins</li>
    <li>All are granted +1D to all Orator, Criminal and Scavenger tests</li>
    <li>Everyone may conduct one free bit of personal business without adding to lifestyle cost</li>
</ul>""",
    17: """<em>Jubilee.</em> The nobility celebrates the birth of a great leader. Everyone
receives one boon in the following order:
<ul>
    <li>If you are hungry or thirsty, you are given alms in the form of one portion of fresh rations</li>
    <li>If you are ill, a priest-healer treats you and removes the sick condition</li>
    <li>If you are neither hungry or sick, they commute any sentence or ban against you or forgive your outstanding debts in this town</li>
</ul>""",
    18: """<em>Craze.</em> The city is going wild for something again. Roll 1d6 to discover what they’re on about:
<table class='table'>
    <tr>
        <td>1</td>
        <td><em>Fine hats or shoes.</em> Sell them at the market for 4D of silver coins.</td>
    </tr>
    <tr>
        <td>2</td>
        <td><em>Elves.</em> Elves are granted +1D to Resources and Circles tests.</td>
    </tr>
    <tr>
        <td>3</td>
        <td><em>Dwarven-made items.</em> Any dwarven-made item can be sold for +1D (minimum value of 1D).</td>
    </tr>
    <tr>
        <td>4</td>
        <td><em>Home-cooked meals.</em> All fresh, home-cooked meals can be sold for 1D of copper coins.</td>
    </tr>
    <tr>
        <td>5</td>
        <td><em>Wizards.</em> A magician who casts a spell on a supplicant (or fakes it) can charge them 2D silver coin. This practice is considered highly illegal by the Magicians and Alchemists guild.</td>
    </tr>
    <tr>
        <td>6</td>
        <td><em>Prophets.</em> Anyone who performs an invocation in public (or fakes it) is showered with 2d2 dice worth of silver coins. This practice will bring down the wrath of the temple priests and their acolytes.</td>
    </tr>
</table>
""",
    19: "<em>Investment opportunity.</em> Hey, you look like a smart customer. I have a golden opportunity for you. Just cherry. How would you like to get in on something that is really going to pay off? Your group may invest in a caravan, expedition or ship, or may purchase a business in the city. Reduce Precedence requirement by one for this once-in-a-lifetime offer. You may invest even if not in respite. See the Lore Master’s Manual for costs and payouts.",
}


busy_crossroad_events = {
    2: "<em>Catastrophic fire.</em> The town burns to the ground with a rapidity that shocks even the cynical. Remain in the adventure phase. Mark the town as a ruin on your map.",
    3: "<em>Plague.</em> Town closed. Remain in the adventure phase until you reach a new town or until the plague is miraculously cured.",
    4: "<em>Famine.</em> There is no food available. Remain in the adventure phase until you reach a new town or until the famine is miraculously relieved.",
    5: """<em>Infestation.</em> Town closed. Remain in adventure phase until infestation is driven out or until you arrive at another town.
<table class='table'>
    <tr>
        <td>1</td>
        <td>Weevils eat all clothing</td>
        <td>3</td>
        <td>Worms devour all leather</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Locusts blanket town</td>
        <td>4-6</td>
        <td>Tiny devils everywhere</td>
    </tr>
</table>
""",
    6: "<em>Robbery.</em> A thief attempts to rob one character. The game master chooses the target. They test Criminal vs Criminal 6. If the thief succeeds, they remove one belt or carried item from the victim.",
    7: "<em>Hard luck.</em> One of your friends is in town and is at loose ends. They desperately need 2D of coin or two portions of food and wine.",
    8: """<em>Fire.</em> One facility was badly damaged in a fire. Roll 2d6 for facility:
<table class='table'>
    <tr>
        <td>2-3</td>
        <td>Guild hall</td>
        <td>8</td>
        <td>Market</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Homes</td>
        <td>9</td>
        <td>Inn</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Stables</td>
        <td>10</td>
        <td>Flophouse</td>
    </tr>
    <tr>
        <td>6-7</td>
        <td>Tavern</td>
        <td>11+</td>
        <td>Shrine</td>
    </tr>
</table>
""",
    9: "<em>Enemy at the gates.</em> An enemy awaits (game master’s choice).",
    10: "<em> Visiting nobility.</em> They smell nice, are polite and make no imposition.",
    11: "<em>A bell tolls.</em> All is well.",
    12: """<em>Small gifts.</em> A child emerges and presents you with:
<table class='table'>
    <tr>
        <td>1</td>
        <td>A flower</td>
        <td>4</td>
        <td>A key</td>
    </tr>
    <tr>
        <td>2</td>
        <td>An empty cup</td>
        <td>5</td>
        <td>A pair of wooden toy oxen</td>
    </tr>
    <tr>
        <td>3</td>
        <td>An icon of an Immortal</td>
        <td>6</td>
        <td>A tooth</td>
    </tr>
</table>
""",
    13: """<em>Market glut.</em> Reduce the Resources obstacle for affected goods by one. If an item is reduced to Ob 0, you may purchase two for the price of one instead. Roll 1d6 for affected commodity:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Wheat or millet (fresh rations)</td>
        <td>4</td>
        <td>Iron (weapons, heavy armor)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Wine</td>
        <td>5</td>
        <td>Wool (clothing, cloaks)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Oil, tar, pitch (torches, lanterns)</td>
        <td>6</td>
        <td>Paper (writing kit, spell books)</td>
    </tr>
</table>
""",
    14: "<em>Wedding.</em> A wedding spills into the square. Dance a jig with the bride and groom and recover one point of taxed Nature.",
    15: "<em>Right of way.</em> A noble desires to have the right of way. However, they want no trouble and toss down 1D of copper coins and urge you to step aside. What will you do? Any tests made add to your lifestyle cost.",
    16: """<em>Exotic goods.</em> A caravan or ship arrives selling exotic goods. You
have the opportunity to purchase at discount prices. Roll 1d6 for
what they’re selling:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Elixirs (Ob 2): Calming Scalp Balm or a Vial of Purifying Heavy Water </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Silks, lace and satin (Ob 4): 2d3 supplies for crafting finery</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Spices (Ob 1 per parcel): Roll 2d3 for parcels. Each parcel is worth 2D of treasure</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Weaponry: Roll twice on the Weapons loot subtable</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Oils and unctions (Ob 4): Roll once on the Potions subtable</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Religious amulets (Ob 1): +1D Maneuver weapon in spiritual conflicts (neck/worn)</td>
    </tr>
</table>
""",
    17: "<em>Stray dog.</em> A cheerful dog trots out of an alley and adopts one of you as her own. Feed her one portion of fresh or preserved rations to keep her. She’ll stick with you through thick and thin.",
    18: """<em>Victory celebration.</em> The local overlord returns victorious from campaign and distributes gifts among the populace. Roll 1d6 to find what each character receives:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Captive: you must either marry or emancipate them</td>
    </tr>
    <tr>
        <td>1</td>
        <td>A small sack of silver coins worth 2D (pack 2)</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Livestock: a horse, pony, cow or ox</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Fine silks and brocades: counts as finery (worn/torso 3 or pack 4)</td>
    </tr>
    <tr>
        <td>1</td>
        <td>A weapon won in battle (roll on the Weapons Loot Table)</td>
    </tr>
    <tr>
        <td>1</td>
        <td>A piece of jewelry (roll on the Jewelry subtable)</td>
    </tr>
</table>
""",
    19: "<em>Abandoned supply wagon.</em> A wagon sits on the road outside of town with no mules or drivers to be seen. Plunder it for 2d2 rolls on the Gear table or return it to the guild hall and be granted a reward of two small sacks of silver coins (2D, pack 2 each).",
}


dwarven_hall_events = {
    2: "<em>Dug too deep.</em> In their greed, the miners and artificers have dug too deep and awoken something sinister and terrible. The halls are empty, the dwarves within slain, and something twisted and loathsome has taken their place. Mark these halls as a ruin on your map. Remain in the adventure phase.",
    3: "<em>Struggle for power.</em> The dwarf princes plot against one another. The halls have split into factions. Remain in the adventure phase until the struggle subsides or until you reach a new town.",
    4: "<em>Famine.</em> No food is available in the halls or the surrounding lands. Remain in adventure phase until you reach a new town or until the famine is miraculously relieved.",
    5: "<em>Devastating flood.</em> The avenues are rivers, staircases waterfalls and towers islands. All is chaos. Remain in the adventure phase until you reach a new town.",
    6: """<em>Under siege.</em> The dwarves are resisting a besieging army, but their halls are open to allies. Increase all Resources and Circles obstacles by 1, but sell kit and salvage at a +1D cash markup. Roll 1d6 to determine the besiegers:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Giants</td>
        <td>4</td>
        <td>Dwarves</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Goblins</td>
        <td>5</td>
        <td>Elves</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Humans</td>
        <td>6</td>
        <td>Orcs</td>
    </tr>
</table>
""",
    7: "<em>Surly watch.</em> The axe bearers on watch at the gates are particularly surly. To gain entry to the halls, ask permission of the Gate Master Sergeant. Test Persuader vs Persuader 4. Suggested failure: angry or a twist that you must offer a bribe to enter.",
    8: "<em>Traffic.</em> The caravan line waiting to approach the dwarven halls is days long, and no one seems to be in charge. Make an Ob 3 Steward test to get your crew through before you die of old age. Suggested failure results: angry or a twist that entry requires a bribe valued at 2D of cash.",
    9: "<em>Nogfest.</em> It’s Nogfest time at the dwarven halls! The taverns are packed full of merry, singing folk. Increase accommodations costs by 1, but haggling at the market is free.",
    10: "<em> Dwarven penny.</em> You find a copper penny stamped with the face of a heroic dwarf sovereign; on the obverse sits a majestic rune.",
    11: "<em> Jocular guards.</em> The axe bearers on watch gently tease you about your inferior blades as they happily point you to the tavern.",
    12: """<em>Misplaced baggage.</em> A bundle falls from the wagon of a trader
heading in the opposite direction. Will you hail them and return it?
If opened, roll 1d6 to determine what it contains:
<table class='table'>
    <tr>
        <td>1</td>
        <td>An infant child</td>
        <td>4</td>
        <td>Charcoal</td>
    </tr>
    <tr>
        <td>2</td>
        <td>A pouch of silver worth 1D </td>
        <td>5</td>
        <td>A sack of flour</td>
    </tr>
    <tr>
        <td>3</td>
        <td>A large snake</td>
        <td>6</td>
        <td>A decapitated head</td>
    </tr>
</table>
""",
    13: "<em>Unattended till.</em> As you enter the halls, you see a dwarf vendor leave their till open and unattended while they fulfill a customer’s request. To snag the take, test Criminal test vs Beginner’s Luck Health 5. Success nets 2D of silver coins. Suggested failure: a twist in which they summon the axe bearers on watch to arrest you.",
    14: "<em>Lucky duck.</em> Nothing goes better with nog than a throw of the dice. Sit. Play. I insist. Each character who can stake 1D of coins or loot must play a round of Wizard, Krazzik or a hand of Diamondback (as detailed in the Gambling chapter of the Lore Master’s Manual). If you win, take a satchel of silver coins. If you lose, you lose your stake.",
    15: """<em>Artificer’s indulgence.</em> An eccentric local artificer is willing to part with some of their work for a price. Roll 1d6 once:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Dwarven helmet (Ob 3).</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Dwarven shield (Ob 4).</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Dwarven coat of plates (Ob 5): Coat of plates that wards off damage on a roll of 3-6.</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Dwarven belt and buckle (Ob 4): Increases belt inventory by one.</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Dwarven canteen (Ob 4): Two-slot liquid container (belt 1).</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Gold pendant set with ruby (Ob 5): This pendant is worth 10D in any other settlement (worn/neck).</td>
    </tr>
</table>
""",
    16: """<em>New hall opens.</em> The industrious dwarves open a new hall in their
sprawling holding. They invite you to stay for free! What could go
wrong? Roll 1d6 to see:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Due to unforeseen complications, the hall collapses as you enter. Your hosts offer you each 2D of gold as compensation, provided you never speak a word of it. Also, you must find new accommodations.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Bare halls (equivalent to stables)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Spartan halls (equivalent to flophouse)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Homey halls (equivalent to inn)</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Palatial hall (equivalent to hotel)</td>
    </tr>
    <tr>
        <td>6</td>
        <td>The dwarven proportions of this inn are uncomfortable for elves and humans. These guests suffer +1 Ob to recovery tests while staying at these accommodations, but they learn something: gain Dwarf-wise.</td>
    </tr>
</table>
""",
    17: "<em>You I like.</em> A friendly trader tips their hat as you enter the gates. If you successfully tell tales at the tavern, in addition to the standard results, add a new town friend in the dwarven halls. The game master determines their profession and name.",
    18: "<em>Gold flows like wine.</em> In an ostentatious show, the dwarf artificers make gold flow through the halls in rivers. Each character may dip one container into the stream and fill it. Each inventory slot counts as 2D of gold coins (pack 1). They must have the container on their person at the start of the town phase (and the container is ruined).",
    19: """<em>Immortal task.</em> An Immortal in need visits the dwarven halls in
search of the skills of their artificers. The Immortal requires a
special item created for a special task—a mighty hammer, a golden
boar, golden hair, etc. The artificers work diligently and do not want
to be disturbed. However, if the characters happen to be carrying
the item in question, they can offer it to the Immortal. The Immortal
will grant a boon for this service (restore a Nature descriptor, raise
the recently deceased, gift a greater relic, etc.). However, striking
this bargain makes an enemy of the Master Artificer of the dwarven
halls. If the characters refrain from interfering, they may dig through
the cast off from the artificers’ forges. Everyone is too focused on
the artisanal task to notice. Roll 1d6 once to determine what is found:
<table class='table'>
    <tr>
        <td>1</td>
        <td>Dwarven forge mask (see the Magical Items list in the Loot chapter).</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Dwarven helmet (Ob 3): Counts a reinforced helmet.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Dwarven shield (Ob 4): Counts as a reinforced shield.</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Dragonslaying sword: The sword is Dragon-wise and grants +1 Might.</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Gold slag worth 8D (pack 4).</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Dwarven artificer tools (special tools for Smith and Jeweler that replace default skill tools and grant a +1D bonus to all crafting tests).</td>
    </tr>
</table>
""",
}

elfhome_events = {
    2: "<em>Pass on to the Shining Realm.</em> The elves here have decided this mortal world is no longer for them. They have, en masse, passed on to their eternal home. No trace remains. Erase this settlement from your map and remain in the adventure phase.",
    3: "<em>Betrayal.</em> Spiteful elves have set to kinslaying. A war rages within, and no outsiders are permitted. Remain in the adventure phase until the bloodletting ceases or you find a new settlement to shelter in.",
    4: """<em>Ancient war.</em> The greedy and the bloodthirsty seek to plunder the
fabled riches of Elfhome. A war rages in the fields before the secret
citadel. Remain in the adventure phase until the attackers are driven
off, the elves are defeated or you skulk off to another settlement.

<table class='table'>
    <tr>
        <td>1</td>
        <td>Giants</td>
        <td>4</td>
        <td>Dwarves</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Orcs</td>
        <td>5</td>
        <td>Dragons</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Humans</td>
        <td>6</td>
        <td>Werewolves</td>
    </tr>
</table>
""",
    5: "<em>Immortal quarrel.</em> An Immortal visits Elfhome to quarrel with the dreamwalkers about troubling visions. The way is shut until this matter is settled. Remain in the adventure phase until you find another settlement in which to shelter.",
    6: """<em>Dreamlands call.</em> Omens hang heavy in the air. Elves from all tribes have been called to enter the dreamlands to assess the portents.
Roll to determine which services are closed:

<table class='table'>
    <tr>
        <td>1</td>
        <td>Tavern</td>
        <td>3</td>
        <td>Inn and Homes</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Stables</td>
        <td>4-6</td>
        <td>Market</td>
    </tr>
</table>
""",
    7: "<em>Lamentations.</em> The elves are singing laments to grieve for those elves who have died of pierced and broken hearts. The tavern is closed. Also, all who hear the lament must make an Ob 3 Will test. Success indicates they grieve for broken dreams and lost loves along with the elves. Suggested failure results: angry or a twist that the character falls into a state of wonderment and racks up +1 lifestyle cost as they sit for days and marvel at the elvish songs.",
    8: """<em>Suspicion.</em> The elves are furious over some crime committed by
outlanders in Elfhome. They search all pouches, pockets, sacks,
satchels, packs and baggage for contraband. Roll 1d6 to see what
they confiscate:
<table class='table'>
    <tr>
        <td>1</td>
        <td>All strange idols</td>
        <td>4</td>
        <td>A relic</td>
    </tr>
    <tr>
        <td>2</td>
        <td>A potion</td>
        <td>5</td>
        <td>A scroll</td>
    </tr>
    <tr>
        <td>3</td>
        <td>All knives and daggers</td>
        <td>6</td>
        <td>A dwarven or elven-made item</td>
    </tr>
</table>
""",
    9: "<em>Enraptured.</em> Your friend has found their way into Elfhome and now cannot bring themselves to leave this beautiful, peaceful place. Will you guide them on their journey home, or will you leave them to remain with the elves forever? The game master chooses which friend.",
    10: "<em>It’s a bright, clear day.</em>",
    11: "<em> Eye contact.</em> An elf smiles enigmatically at you as you enter Elfhome.",
    12: "<em>Shafts of sunlight.</em> Trunks of ancient trees stretch to the sky; shafts of golden sunlight gently flow to the earth. All is well here.",
    13: "<em>Omens.</em> A strange elf approaches. They touch your face and speak to you directly of your dreams—your deepest, unshared secrets. Test Lore Master (Ob 3) to interpret their omens. If successful, remove the angry, afraid or exhausted condition. Suggested failure results: afraid or a twist that you experience terrifying nightmares that cause +1 Ob to all recovery tests until the next town phase. The game master chooses the character approached.",
    14: "<em>Song of merriment.</em> The elves are at feast. Join them and satisfy any hunger or thirst. Also, all are granted +1D to recover from angry, exhausted or sick. If you have no conditions, cadge some food or wine from the table (fresh rations or a bottle) for later.",
    15: "<em>Wanderer’s gift.</em> An ancient elf matron approaches you with a gift of elven waybread. The waybread acts as preserved rations, but it is pack 1 for six portions. However, when used with Cook or Grace of the Lords of Plenty, each piece acts as fresh rations.",
    16: "<em>Remembrance day.</em> The elves remember the Shining Lands and all that has befallen them since leaving. All elves recover all taxed Nature. If not taxed, mark a pass or fail for Nature. If one test would advance you, you must mark it. All others may rewrite their creed, even if this town phase is not a respite.",
    17: "<em>Restful memory.</em> You carry with you the peace and tranquility of Elfhome, even after you leave this place. The memory suffuses you with a warm glow and grants +1D to all recovery tests until the next town phase.",
    18: "<em>Doomsayer.</em> The elven etharch walks among their people, speaking to them of their travels and travails. The etharch automatically alleviates the most dire condition afflicting a character. If unafflicted, the etharch removes any curse carried by the character. If unafflicted and uncursed, the etharch passes on to others. However, if a character misbehaves in Elfhome during this town phase, the etharch summons them and reads their doom. The game master then changes the character’s belief or goal. It cannot be changed by the player until the next town phase.",
    19: "<em>Enter the Dreamlands.</em> While you sleep, you dream too deeply and lose a bit of yourself to this place. Non-elf characters must replace one Nature descriptor with Singing, Remembering or Hiding. Elves may conduct all business in town in dream. Reduce their lifestyle cost for each activity by one (minimum 0—but market prices are unaffected). If an elf fails their Resources test to leave Elfhome, they must take the exhausted condition in addition to other effects.",
}
religious_bastion_events = {}
remote_village_events = {}
wizard_tower_events = {}

events_dicts = (
    bustling_metropolis_events,
    busy_crossroad_events,
    dwarven_hall_events,
    elfhome_events,
    religious_bastion_events,
    remote_village_events,
    wizard_tower_events,
)
town_events_table = {k: v for k, v in zip(town_types, events_dicts)}
