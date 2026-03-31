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


busy_crossroad_events = {}
dwarven_hall_events = {}
elfhome_events = {}
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
