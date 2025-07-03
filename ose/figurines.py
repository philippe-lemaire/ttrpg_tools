from .hoard_treasure import roll, get_closest_key

ebony_fly = """
<h3>Ebony Fly</h3>
<p>A fly the size of a pony which may be
ridden as a mount.</p>
<hr>
<p><b>AC</b> 4 [15], HD 4+4 (22hp), <b>Att</b> None,<br>
<b>THAC0</b> 15 [+4], <b>MV</b> 480’ (160’) flying,<br>
<b>SV</b> D12 W13 P14 B15 S16 (2), ML 12, <b>AL</b>
Neutral, <b>XP</b> 125, <b>NA</b> 1 (1), <b>TT</b> None<br>
<hr>
<ul>
<li><b>Carrying loads:</b> Moves at 360’ (120’)
with a rider.</li>
<li><b>Usage frequency:</b> 3 times a week, for
at most 12 hours a day.</li>
</ul>
"""

golden_lion = """
<h3>Golden Lion</h3>
<p>A male lion with formidable combat
prowess.</p>
<hr>
<p><b>AC</b> 6 [13], <b>HD</b> 5 (22hp), <b>Att</b> 2 × claw (1d4+1) or 1 × bite (1d10),<br>
<b>THAC0</b> 15 [+4],<br>
<b>MV</b> 150’ (50’), <b>SV</b> D12 W13 P14 B15 S16<br>
(3), <b>ML</b> 12, <b>AL</b> Neutral, <b>XP</b> 175, <b>NA</b> 1<br>
(1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Usage frequency:</b> Once a day, for up
to 1 hour.</li>
<li><b>If slain:</b> Cannot be brought back from
statuette form for one full week.</li>
</ul>"""

goat_of_travelling = """
<h3>Ivory Goat of Travelling</h3>
<p>A large goat which can be ridden.</p>
<hr>
<p><b>AC</b> 6 [13], <b>HD</b> 4 (24hp), <b>Att</b> 2 × horn (1d8)<br>
<b>THAC0</b> 16 [+3], <b>MV</b> 480’ (160’),<br>
<b>SV</b> D12 W13 P14 B15 S16 (2), <b>ML</b> 12, <b>AL</b> Neutral<br>
<b>XP</b> 75, <b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Carrying loads:</b> Moves at 360’ (120’)
with a rider.</li>
<li><b>Usage frequency:</b> At most 24 hours in
the space of a week. After 24 hours of use,
the goat cannot be used again for at least
1 day. After 3 uses in total, the goat loses
its magic forever.</li>
</ul>
"""

goat_of_travail = """
<h3>Ivory Goat of Travail</h3>
<p>A monstrous goat, larger than a bull.</p>
<hr>
<p><b>AC</b> 0 [19], <b>HD</b> 16 (96hp), <b>Att</b> 1 × bite (2d4), 2 × hoof (2d4+2), 2 × horn (2d6),<br>
<b>THAC0</b> 8 [+11], <b>MV</b> 240’ (80’), <br>
<b>SV</b> D8 W9 P10 B10 S12 (8), <b>ML</b> 12, <b>AL</b> Neutral,<br>
<b>XP</b> 1,350, <b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Charge:</b> When not in melee. Requires
a clear run of at least 20 yards. Horns
inflict double damage. May not make bite
or hoof attacks when charging.</li>
<li><b>Usage frequency:</b> Once per month for
up to 12 hours. After 3 uses in total, the
goat loses its magic forever.</li>
</ul>
"""

goat_of_terror = """
<h3>Ivory Goat of Terror</h3>
<p>A giant goat, as large as a warhorse,
which may be ridden. The goat’s horns
become weapons which the rider may
wield.</p>
<hr>
<p><b>AC</b> 2 [17], <b>HD</b> 8* (48hp), <b>Att</b> None,<br>
<b>THAC0</b> 12 [+7], <b>MV</b> 360’ (120’), <br>
<b>SV</b> D12 W13 P14 B15 S16 (2), <b>ML</b> 12, <b>AL</b> Neutral,<br>
<b>XP</b> 1,200, <b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Horns:</b> One horn may be wielded as a
lance +3, the other as a sword +3.</li>
<li><b>Charge:</b> When not in melee. Requires
a clear run of at least 20 yards. Rider’s
lance inflicts double damage.</li>
<li><b>Aura of terror:</b> In battle, opponents
within 30’ must <b>save versus spells</b> or
suffer a –3 penalty to attack rolls while
the battle lasts.</li>
<li><b>Usage frequency:</b> Once every 2 weeks
for up to 3 hours. After 3 uses in total, the
goat loses its magic forever.</li>
</ul>
"""

marble_elephant = """
<h3>Marble Elephant</h3>
<p>A large, tusked elephant that can be used
as a beast of burden or commanded to
attack.</p>
<hr>
<p><b>AC</b> 5 [14], <b>HD</b> 9 (40hp), <b>Att</b> 2 × tusk (2d4) or 1 × trample (4d8),<br>
<b>THAC0</b> 12 [+7]<br>
<b>MV</b> 120’ (40’), <b>SV</b> D10 W11 P12 B13 S14 (5)<br>
<b>ML</b> 12, <b>AL</b> Neutral, <b>XP</b> 900,<br>
<b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Charge:</b> In first round of combat,
when not in melee. Requires clear run
of at least 20 yards. Tusks inflict double
damage.</li>
<li><b>Trample:</b> 3-in-4 chance of trampling
each round. +4 to hit human-sized or
smaller creatures.</li>
<li><b>Usage frequency:</b> At most 4 times a
month, for up to 24 hours at a time.</li>
</ul>
"""

obsidian_steed = """
<h3>Obsidian Steed</h3>
<p>In figurine form, a vaguely quadruped
lump of obsidian. Transforms into a
nightmare—an intelligent, demonic horse
with glowing red eyes, flaming nostrils,
and hooves like smouldering embers.</p>
<hr>
<p><b>AC</b> –3 [22], <b>HD</b> 6* (27hp), <b>Att</b> 2 × flaming hoof (2d4 + 2) 1 × bite (2d4), <br>
<b>THAC0</b> 14 [+5], <b>MV</b> 150’ (50’) / 360’<br>
(120’) flying, <b>SV</b> D10 W11 P12 B13 S14 (6),<br>
<b>ML</b> 10, <b>AL</b> Chaotic, <b>XP</b> 500, <b>NAb> 1 (1), TT None</p>
<hr>
<ul>
<li><b>Burning smoke:</b> Breathe out a choking cloud of burning smoke. Anyone in
melee with a nightmare must save versus
poison or suffer –2 to attack and damage
rolls against the monster.</li>
<li><b>Usage frequency:</b> Once per week, for up to 24 hours.</li>
</ul>
"""

onyx_dog = """
<h3>Onyx Dog</h3>
<p>A hunting dog with exceptional senses.</p>
<hr>
<p><b>AC</b> 6 [13], <b>HD</b> 2+2 (11hp), <b>Att</b> 1 × bite (2d4),<br>
<b>THAC0</b> 17 [+2], <b>MV</b> 120’ (40’),<br>
<b>SV</b> D12 W13 P14 B15 S16 (1), <b>ML</b> 11, <b>AL</b> Neutral,<br>
<b>XP</b> 25, <b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Tracking:</b> By scent. Once started, very
difficult to put off the trail.</li>
<li><b>Infravision:</b> 90’.</li>
<li><b>Detect invisible:</b> 65% chance.</li>
<li><b>Intelligent:</b> Speaks Common.</li>
<li><b>Usage frequency:</b> Once per week, for up to 6 hours.</li>
</ul>
"""

serpentine_owl = """
<h3>Serpentine Owl</h3>
<p>A horned owl with telepathic powers.</p>
<hr>
<p><b>AC</b> 7 [12], <b>HD</b> 1/2 (3hp), <b>Att</b> 2 × claw (1d2),<br>
<b>THAC0</b> 19 [0], <b>MV</b> 240’ (80’) flying, <br>
<b>SV</b> D12 W13 P14 B15 S16 (1), ML 12,<br>
<b>AL</b> Neutral, <b>XP</b> 5, <b>NA</b> 1 (1), <b>TT</b> None</p>
<hr>
<ul>
<li><b>Surprise:</b> On a 1–5, due to silent flight.</li>
<li><b>Telepathy:</b> Can inform owner of what it sees and hears.</li>
<li><b>Usage frequency:</b> Once per day, for up to 8 hours.</li>
</ul>
"""


class Figurine:
    rules = """
<p>A miniature (around 1” tall) statuette carved in the form of an animal. </p>
<p>Speaking the correct command word and casting the figurine onto the ground causes it to transform into a living animal which
obeys the character’s commands.</p>
<ul>
<li><b>Returning to figurine:</b> Repeating the
command word returns the animal to its
figurine form.</li>
<li><b>If an animal is slain:</b> It returns to its
figurine form.</li>
<li><b>If a figurine is destroyed:</b> Its magical
power is lost irrevocably.
</ul>
"""
    forms = {
        3: "Ebony Fly",
        6: "Pair of golden lions",
        8: "Trio of ivory goats (travelling, travail, and terror)",
        11: "Marble elephant",
        13: "Obsidian steed",
        17: "Onyx dog",
        20: "Serpentine owl",
    }

    forms_stat_blocks = {
        "Ebony Fly": ebony_fly,
        "Pair of golden lions": "<br>".join([golden_lion, golden_lion]),
        "Trio of ivory goats (travelling, travail, and terror)": "<br>".join(
            [goat_of_travelling, goat_of_travail, goat_of_terror]
        ),
        "Marble elephant": marble_elephant,
        "Obsidian steed": obsidian_steed,
        "Onyx dog": onyx_dog,
        "Serpentine owl": serpentine_owl,
    }

    def __init__(self):
        result = roll("1d20")
        self.form = get_closest_key(result, self.forms)

    def __repr__(self):
        return f"Figurine of Wondrous power of type {self.form}"

    def get_html_stat_blocks(self):
        return self.forms_stat_blocks.get(self.form)
