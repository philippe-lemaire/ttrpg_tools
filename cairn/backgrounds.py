backgrounds = [
    "Aurifex",
    "Barber-Surgeon",
    "Beast Handler",
    "Bone Keeper",
    "Cutpurse",
    "Field Warden",
    "Fletchwind",
    "Foundling",
    "Fungal Forager",
    "Greenwise",
    "Half Witch",
    "Hexenbane",
]

aurifex_tables = [
    {
        "name": "What experiment went horribly wrong?",
        "options": {
            1: "There was an explosion, and you lost your sense of smell. Well, almost: you can sniff out gold as a pig does truffles. Take a <b>Tin of Snuff</b> (6 uses) to dampen the impact. Use it every day or become deprived.",
            2: "You dematerialized a beloved pet. Now it follows you around, invisible but always present. Although it cannot interact with the physical realm, you are able to share its senses (add a Fatigue each time). It follows basic commands.",
            3: "You were exposed to a long-acting truth serum whose effects have yet to wear off. The disorder has its advantages: you cannot repeat lies you’ve heard, either.",
            4: "You were adept at creating fake gold, which is almost as good. Eventually, your ruse was discovered and you had to make a hasty retreat. Take a heavy Metal Ingot and Gold Powder (3 uses).",
            5: "Your recipe worked, but a rival stole the blueprint before your claims could be proven. Take a prototype Blunderbuss (d12, blast, bulky) and a taste for revenge.",
            6: "Ridiculed for discovering how to turn gold into lead, you were a laughing stock. Take a bottle of Universal Solvent (2 uses) that dissolves anything it touches into its constituent parts.",
        },
    },
    {
        "name": "What alchemical marvel is the product of your latest ingenuity?",
        "options": {
            1: "<b>Pyrophoric Gel:</b> A sticky green fluid that catches fire when exposed to air, then burns for 8 hours. Cannot be extinguished (1 use).",
            2: "<b>Blast Sphere</b>: A head-sized iron ball filled with explosive powder that explodes on impact (d12, blast, bulky, 1 use).",
            3: "<b>Aqua Vita</b>: Purifies any liquid, converting it to pure water. Drinking it cures 1d6 STR (1 use).",
            4: "<b>Mimic Stone</b>: Records a short phrase that can later be played back.",
            5: "<b>Spark Dust</b>: Ignites easily and quickly. Useful for starting a fire or as an incendiary device (3 uses).",
            6: "<b>Homunculus</b>: A miniature clay replica of yourself that follows your every command to the letter. It hates being enthralled to you and complains bitterly whenever possible. Any damage done to the homunculus is also done to you.",
        },
    },
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Lantern",
        "Oil Can (6 uses)",
        "Needle-Knife (d6)",
        "Protective Gloves (petty)",
    ],
    # profile
    """You are an artisan of the arcane, a smith of subtle forces.
    <br>In the crucible of your workshop, the laws that govern this world are warped to suit your needs.""",
    # names
    [
        "Hestia",
        "Basil",
        "Rune",
        "Prism",
        "Ember",
        "Quintess",
        "Aludel",
        "Mordant",
        "Salaman",
        "Jazia",
    ],
]

barber_surgeon_tables = [
    {
        "name": "How have you “improved” yourself?",
        "options": {
            1: """You have a replacement eye that can magnify objects, acts as a telescope,
and provides minimal night vision. You cannot wear anything metal on
your head, and strong magnets make you deprived.""",
            2: """One foot is mostly metal (kick, d6), and you treat some Tough Terrain
as Easy. Carry an Oil Can (6 uses). Without a daily application you are
deprived and noisy.""",
            3: """One of your fingers has been swapped, the bone replaced by gold and
iron. Take a Hook and a Screwdriver that can attach to the fingertip.""",
            4: """Both ears have been surgically enhanced, tripling your hearing. You can
focus on a specific sound at a great distance, such as a conversation. You
wear an ear flap to protect against sudden loud noises (WIL save to avoid
temporary paralysis).""",
            5: """Your chest is lined with alchemical sigils, toughening the skin (1 Armor).
Wearing other metallic armor nullifies the effect.""",
            6: """One arm is fully metal, and comes off at the shoulder. It can be used as a
weapon (d8, bulky when not attached) and can move independently if you
are within sight of it.""",
        },
    },
    {
        "name": "What rare tool is essential to your work?",
        "options": {
            1: """<b>Regrowth Salve</b> Regrows a body part over the course of a day (1 use).""",
            2: """<b>Graftgrub</b> A small worm that can fuse inanimate objects with parts
of the body (1 use).""",
            3: """<b>Woundwax</b> Heals wounds from fire or chemicals (restoring full STR),
but nothing else (2 uses).""",
            4: """<b>Quicksilver</b> A stimulant. Go first in combat, and automatically pass any
WIL saves for one hour. Addictive: Save STR or become
deprived after 24 hours without it (4 uses).""",
            5: """<b>Pneuma
Pump</b> Portable iron lungs (bulky). Enables life-saving surgery, or
underwater breathing.""",
            6: """<b>Lodestone</b> Draws out dangerous elements from the body, and acts as
a powerful magnetic force.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Amputation Knife (d6)",
        "Bandages (3 uses)",
        "Leech (restores 1 STR, 3 uses)",
        "Stained Medical Finery (petty)",
    ],
    # profile
    """You walk the line between healer and harrower, knowing the frailty of the flesh
but also the secrets that lay within.<br>With the right tools, life and death are merely
words.""",
    # names
    [
        "Wilmot",
        "Patch",
        "Lancet",
        "Sawbones",
        "Theo",
        "Cutwell",
        "Humor",
        "Landsford",
        "Goodeye",
        "Johanna",
    ],
]


beast_handler_tables = [
    {
        "name": "What creature is your specialty?",
        "options": {
            1: "Arachnids</b>: Take a Quick-Flame Rod and an Oil Can (6 uses). It can destroy a large spider nest in seconds.",
            2: "<b>Felines</b>: Take a sack of Whiskerwort. Its odor can calm and control even the largest of cats.",
            3: "<b>Canines</b>: Take a wreath of Wolfsbane and a Large Net. Also effective against werewolves!",
            4: "<b>Birds</b>: Take a Warble-Whistle (3 charges). It can imitate any bird call, and can even be used to send simple messages.  Recharge: Feed a baby bird as its mother would, then blow.",
            5: "<b>Rodents</b>: Take a Windpipe that emits a high-pitched sound that only rodents can hear. So long as you play, they will follow. Even to their deaths.",
            6: "<b>Serpents</b>: Take a Warming Stone that generates an irresistible heat, and a vial of Antitoxin (2 uses).",
        },
    },
    {
        "name": "What do creatures of the wild understand that your kind do not?",
        "options": {
            1: """There is far more to the world than meets the eye. With quiet
concentration, you can borrow the senses of a nearby creature of your
specialty.""",
            2: """The behavior of beasts is a language in itself. When observing beasts of
your specialty, you gain insight into weather patterns and impending
disasters.""",
            3: """The pulse of the hunt is a powerful impulse. You have a sense for when
predators, even those not of your specialty, are near.""",
            4: """You know some lands intimately. Your chance of becoming lost in a
terrain dominated by the beasts of your specialty is reduced by one step
(e.g. 4-in-6 becomes 3-in-6).""",
            5: """Nature’s symphony can be heard if you attune to its rhythm. When
surrounded by creatures of your specialty they can alert you to
approaching danger before it arrives.""",
            6: """Survival is about adaptability. Once per day, you may take on a simple
feature from a creature of your speciality (webbed fingers, night vision,
etc.). Add a Fatigue each time.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Leather Whip (d6)",
        "Soporific Darts (STR save or fall asleep, 6 uses)",
        "Lure",
        "Rope (25ft)",
    ],
    # profile
    """You alone can walk among the creatures of the wild, fearless and in control.
    <br>You share a connection with animals that others can only dream of...so long as you
don’t become their snack.""",
    # names
    [
        "Amara",
        "Wulf",
        "Mireille",
        "Soren",
        "Freki",
        "Aster",
        "Gerrik",
        "Boreas",
        "Delphine",
        "Matheus",
    ],
]

bonekeeper_tables = [
    {
        "name": "What did you take from the dead?",
        "options": {
            1: """<b>Paired Sudo-Collars:</b> Highly unethical metal collars with a subject-object relationship. If
you can get another living being to wear one, they pretty much do what you want. Make a
opposed WIL save every day to maintain control.""",
            2: """<b>Hummingbird Knife:</b> (D6, Vorpal) Vibrates at subsonic frequencies. Illegal.""",
            3: """<b>Loyal Sidekick: Create a freelancer. You’ve been through thick and thin together. Think
about how you met.""",
            4: """<b>Hacking Sleeve:</b> Mechanized gauntlet with tools to hack, slice, and infiltrate just about
any system or mechanical device. 1 fatigue when successfully used.""",
            5: """<b>Custom Cape:</b> (Reaction rolls are always one category higher) Flamboyant design of your
choice. Looking good is part of the job.""",
            6: """<b>Moon Gum:</b> Tastes great. Causes intense hallucinations for 1d6 hours and is effectively
immobilizing. Pretty colors… (6 sticks left)""",
        },
    },
    {
        "name": "What tool was invaluable in your work?",
        "options": {
            1: """<b>A Crow-Shaped Amulet</b>. You can ask a question of the dead, but must add a <b>Fatigue</b> each time.""",
            2: """A <b>mortal wound</b> from a freed revenant. You were healed, but the
disfigurement has made you a pariah. You require neither air nor
sustenance, but are still subject to pain and death. Trapped between, the
dead see you as one of their own.""",
            3: """A <b>Blood Pail</b> <em>(bulky)</em> from a local death-cult. Empty its contents to
summon a creature built from items buried below (bones, rocks, pottery,
etc). It obeys your command, but if destroyed you permanently lose 1d4
STR. It has 6 HP, 1 Armor, 13 STR, 11 DEX, 4 WIL, shard fists (d8). <b>Recharge</b>:
Fill the bucket with the blood of a dying warrior.""",
            4: """A <b>Burial Wagon</b> (+6 slots) from your last job. It came with a stubborn old <b>Donkey</b> (+4 slots, +2 slots if pulling wagon, <em>slow</em>).""",
            5: """
The Detect Magic <b>Spellbook</b>, stolen from an ancient library. Your family
worked in service to an obscure underworld deity, but you lost your faith.
Though exiled, you continue to serve, even as an apostate.
<em><b>Detect Magic</b>: You can see or hear nearby magical auras</em>.""",
            6: """
A <b>Plague Doctor’s Mask</b>, after its owner succumbed to the disease that
wiped out everyone you once knew. They should have kept it on.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Lantern",
        "Oil Can (6 uses)",
        "Stake (d6)",
        "Chains (10ft)",
    ],
    # Profile
    """You are a shepherd to the departed. You listen to the final whispers of the dead as
they descend into the cold, unyielding earth.<br>You know that to fully celebrate the
gift of life, we must honor its finale as well.""",
    # names
    [
        "Rook",
        "Ebon",
        "Moro",
        "Yew",
        "Pall",
        "Leth",
        "Nix",
        "Barnaby",
        "Vesper",
        "Leder",
    ],
]

cutpurse_tables = [
    {
        "name": "What was your last big job?",
        "options": {
            1: """A noble’s summer home. The place was full of fancy wine (+20gp) but not much else. Take <b>Fence Cutters</b>.""",
            2: """A bank (you were caught). You bear a brand only visible by firelight, and
anyone that sees the mark can ask you for a beer. Take <b>Retractable Wires</b>.""",
            3: """A guild warehouse. Take a <b>Ladder</b> (<em>bulky</em>, 10ft) and <b>Blinding Powder</b> (1 use).""",
            4: """
Moneylender. Someone beat you to the job, but left behind a <b>Scroll</b> of
<em>Arcane Eye</em> (petty).
<em><b>Arcane Eye</b></em>: You can see through a magical floating eyeball that flies around at your command.""",
            5: """Constable’s quarters. You escaped, but left some friends behind. Take
<b>Strong Silk Rope</b> and a queasy feeling.""",
            6: """A university. You were seen, but not pursued. You still don’t know why.
Take <b>Smoke Pellets</b> (3 uses).""",
        },
    },
    {
        "name": "What helps you steal?",
        "options": {
            1: """<b>Catring</b> 2 charges. Climb up walls and fall safely. Recharge: Place the ring on a stray cat’s tail.""",
            2: """<b>Gildfinger</b> 1 charge. A finger glove that mimics any mundane key.
Recharge: Bundle it with at least 100gp for a night.""",
            3: """<b>Glimpse
Glass</b> 3 charges. A monocle that lets you see through walls or
other obstructions. It shatters after the last use.""",
            4: """<b>Sweetwhistle1 charge</b>. Listeners hear a soft, familiar voice in the
distance that they cannot resist following. Recharge: Lose
a dear memory (describe it).""",
            5: """<b>Vagrant’s
Veil</b> 1 charge. Wear it to blend seamlessly into crowds,
appearing as a simple pauper. Recharge: Donate all the
day’s winnings to the poor (Petty).""",
            6: """<b>Smokestack
Marble</b> 3 uses. Crush to release a dense cloud of smoke that
follows you (Petty).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Twin Daggers (d6+d6, bulky)",
        "Padded Leather (1 Armor)",
        "Lockpicks",
        "Black Outfit (petty)",
    ],
    # profile
    """You live in the grey space between those who have power and
those who don’t. You find opportunity where others see
only chaos. With nimble fingers, you unburden both the
richest merchant and the lowliest guard.""",
    # names
    [
        "Sable",
        "Lyra",
        "Eamon",
        "Salina",
        "Elara",
        "Freya",
        "Isolde",
        "Sparrow",
        "Ivy",
        "Silas",
    ],
]

field_warden_tables = [
    {
        "name": "What got the better of you?",
        "options": {
            1: """A voracious swarm of pests that swallowed crops and animals alike. With
nothing to defend, you left. Take <b>Gale Seed Extract</b> (3 uses). Ingesting one
lets you sprint with a speed four times your regular rate. Afterward you
add two <b>Fatigue</b>.""",
            2: """A crop spirit, angered by a poor tithing. The fires consumed nearly
everything, and afterwards you were able to gather a pouch of <b>Fireseeds</b>
(d8, <em>blast</em>, 4 uses).""",
            3: """An antlered, toothy demon that nearly ended you. Take a <b>blood-stained
bone knife</b> (d6). On critical damage, its next attack becomes <em>enhanced</em>
from contact with blood.""",
            4: """<em>The Withering</em>, a type of stem rot from <b>The Roots</b>. Take a <b>Diseased Crop</b>
(6 uses) that decays any plant it touches.""",
            5: """Wolves, or so you thought. You are now a <b>Werewolf</b> [8 HP, 15 STR, 14 DEX,
claws (d6+d6) or bite (d8)]. Your WIL remains the same. You can turn at
will (once per day) but must make a WIL save to revert. Anyone left alive
from your attacks must make a WIL save to avoid infection.""",
            6: """Crop thieves. Not all of them survived, but you were outnumbered. Take a
+d4 HP and a <b>Hilted Broadsword</b> (d8, <em>bulky</em>).""",
        },
    },
    {
        "name": "What tool saved your life?",
        "options": {
            1: """<b>Bloodvine Whip</b> d8 damage. On Critical Damage it drains the target’s
blood, granting the weapon’s next attack the blast quality.""",
            2: """<b>Clatter Keeper</b> A hand-cranked device that emits a loud noise, frightening
away most creatures.""",
            3: """<b>Sun Stick</b> Provides ample warmth and light for up to one hour (1
use). <b>Recharge:</b> Leave in heavy sunlight for a full day.""",
            4: """<b>Root Tether</b> When thrown, binds up to a wolf-sized creature to the soil
for a short time.""",
            5: """<b>Greenwhistle</b> A small flute that calms plants, making passage through
areas heavy with plant life a bit easier.""",
            6: """<b>Everbloom Band</b> A circlet adorned with flowers that never wilt. On taking
<b>Critical Damage</b> the flowers dissolve into dust, but you
act as if your save succeeded (STR loss still occurs).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Brigandine (1 Armor, <em>bulky</em>)",
        "Sling (d6)",
        "Hand Axe (d6)",
        "Repellent (state the creature, 3 uses)",
    ],
    # profile
    """Protectors of the harvest, defense against pests, thieves, and beasts. A position of
great honor, while it lasts: many guardians do not live out their natural lives.
Roll a second time on the <b>Bonds</b> table.""",
    # names
    [
        "Seed",
        "Thresh",
        "Dibber",
        "Sow",
        "Stalk",
        "Harrow",
        "Cobb",
        "Flax",
        "Briar",
        "Rye",
    ],
]

fletchwind_tables = [
    {
        "name": "How did you earn your bow?",
        "options": {
            1: """<b>War</b>. If you are first to attack, your bow gains the blast property for the
first round.""",
            2: """<b>Falconry</b>. You keep a falcon [3 hp, 5 STR, 16 DEX, 4 WIL, claws (d6+d6),
bite (d6)]. It only eats live game.""",
            3: """<b>Hunting.</b> When taking the Supply (pg. 80) action your ability to secure
Rations increases by one step (e.g. 1d4 becomes 1d6).""",
            4: """<b>Tournaments.</b> Attacks with your bow are enhanced if the target is
immobile.""",
            5: """<b>Training.</b> If you are the first to attack, melee attacks against you are
impaired until you take STR damage.""",
            6: """<b>Scouting.</b> When taking the Travel (pg. 80) action, your presence decreases
the chance of getting lost by one step (e.g. 4-in-6 becomes 3-in-6).""",
        },
    },
    {
        "name": "What kind of wood is your bow made from?",
        "options": {
            1: """<b>Western Yew</b> (d6, <em>bulky</em>). Can be wielded as a blunt weapon (d6). Noisy.""",
            2: """<b>Sessile Oak</b> (d8, <em>bulky</em>). Slams into targets. On critical damage, something is torn off.""",
            3: """<b>Stone Pine</b> (d6, <em>bulky</em>). Produces one use of Sticky Sap per day. It is highly explosive.""",
            4: """<b>White Ash</b> (d6, <em>bulky</em>). Can be used in place of a shield in melee combat (+1 Armor).""",
            5: """<b>Striped Bamboo</b> (d6). Collapsible, it only requires one slot (but still requires both hands).""",
            6: """<b>Wych Elm</b> (d6, <em>bulky</em>). Protects the bearer from poisons and toxins, so long as they are holding it.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Bow (see table)",
        "Serrated Knife (d6)",
        "Boiled Leather (1 Armor)",
        "Heartroot Salve (restores 1d4 STR, 1 use)",
    ],
    # profile
    """You strike from afar, but that does not make you a coward. You are a musician,
the song of your bowstring nought but a warning, singing the silent promise of a
quick death.""",
    # names
    [
        "Flint",
        "Feather",
        "Crier",
        "Thunder",
        "Falcon",
        "Pluck",
        "Needle",
        "Warsong",
        "Hawk",
        "Cai",
    ],
]

foundling_tables = [
    {
        "name": "Who took you in?",
        "options": {
            1: """An old hunter. You were both quite happy, until it all ended. Take a
<b>Weathered Longbow</b> (d8, <em>bulky</em>) and a <b>Leather Jerkin</b> (1 Armor).""",
            2: """A wizened apothecary, who taught you the healing arts but maintained a
clinical detachment. Take a <b>Healing Ungent</b> (restores d4 STR).""",
            3: """A druid, who taught you the language of trees. When it came time to leave
you took with you only a <b>Gnarled Staff</b> (d8) and the promise that one day
you would return.""",
            4: """A gruff blacksmith from a sleepy river town. You were always kept at arm’s
length. Now the forge is cold, and you’ve moved on. Take a <b>Smith’s Apron</b>
(petty) and a set of oft-mended <b>Chain Mail</b> (2 Armor, <em>bulky</em>).""",
            5: """A troupe of traveling entertainers. For a time, they were like family to you.
One day you woke up and they were gone with no explanation. Take a
<b>Storybook</b>, a <b>Dagger</b> (d6), and some burning questions.""",
            6: """
The monks of a secluded forest monastery. When their rules became too
strict, you snuck away. Take a <b>Monk’s Habit</b> (warm, petty) and a <b>Spellbook</b>
of <em>Control Plants</em>.<br>
<em><b>Control Plants:</b> Nearby plants and trees obey you and gain the ability to
move at a slow pace.</em>""",
        },
    },
    {
        "name": "What keeps away bad tidings?",
        "options": {
            1: """<b>Pipeweed</b> Your good luck charm. Conversations tend to flow more easily after a smoke (6 uses).""",
            2: """<b>Stink Jar</b> Shattering this jar releases an odor so foul all nearby must
make a STR save or immediately vomit (1 use).""",
            3: """<b>Ivy Worm</b> A green worm often mistaken for a weed. Swallowed
whole, it absorbs any toxins or rot in the body before
exiting through the usual way.""",
            4: """<b>Dream Stone</b> A smooth blue stone that helps recall dreams more clearly.
Overuse can cause dream-addiction.""",
            5: """<b>Drowning Rod</b> A finger-sized wooden stick that doubles in size each time
it is fully submerged in water. It doesn’t shrink back down.""",
            6: """<b>Rabbit’s Foot</b> You were wearing it when they found you. They say it is
the foot of she who left you, and that it protects you from
witch magic.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Salt Pouch",
        "Heirloom Amulet (<em>petty</em>, glows in the presence of magic)",
        "Sling (d6)",
        "Dagger (d6)",
    ],
    # profile
    """An odd birthmark, a strange smell: somehow, the touch of elsewhere still lingers.
You’ll never fit in, at least not where you’re at. Roll on the Omens table, but keep
the results private for now.""",
    # names
    [
        "Faunus",
        "Snowdrop",
        "Wisp",
        "Silverdew",
        "Brim",
        "Solstice",
        "Steeleye",
        "Sileas",
        "Gossamer",
        "Hazel",
    ],
]

fungal_forager_tables = [
    {
        "name": "What strange fungi did you discover?",
        "options": {
            1: """<b>Shrieking Trumpet</b>. When exposed to light it screams so loudly that all
nearby attacks (including your own) are <em>impaired</em> (2 uses).""",
            2: """<b>Torch Fungus.</b> When crushed it creates a heatless light for ten minutes
(3 uses).""",
            3: """<b>Murderous Truffle</b>. Pungent, highly toxic, and very rare (worth 50gp to
assassins). Illegal pretty much everywhere (1 use).""",
            4: """<b>Hellcap.</b> Exposure to its aroma causes intense nausea, even vomiting.
Either way, it clears the room. Bottled (1 use).""",
            5: """<b>Sproutcup.</b> Ingest to shrink down to the size of a mouse (your belongings
stay the same size). You return to normal size within the hour, often in fits
and starts (1 use).""",
            6: """<b>Rootflower.</b> A white fungus found only on corpses deep underground.
Ingest to restore d6 WIL. You will dream of the dead, and their stories
(1 use).""",
        },
    },
    {
        "name": "What keeps you sane, even in utter darkness?",
        "options": {
            1: """<b>Glowsnail</b> Casts a soft, bioluminescent light. Feeds on one ration every two days.  """,
            2: """<b>Silk Moth Shawl</b> A weatherproof blanket, it can also douse a fire without being damaged.  """,
            3: """<b>Milkflower</b> A gentle stimulant. Chewing makes you immune to panic for the next hour (3 uses).  """,
            4: """<b>Luxcompass</b> Hums softly as it moves closer to the Sun. Eventually, the noise becomes unbearably loud.  """,
            5: """<b>Sloth-Tarp</b> A tough and weatherproof fabric, useful for hanging off trees. When inside, take +1 Armor.  """,
            6: """<b>Miner’s Grease</b> Great for dislodging a gem, tool, or limb from a tight crack. Highly explosive (3 uses).  """,
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Sharpened Trowel (d6)",
        "Candle Helmet (+1 Armor, dim, 6 uses)",
        "Rope (25ft)",
        "Metal Pail",
    ],
    # profile
    """You follow the whisperings of the deep earth, the rhythmic pulse of the mycelium
forest that grows beneath the surface. The dark holds no terror for you. Also, you
really love mushrooms.""",
    # names
    [
        "Unther",
        "Woozy",
        "Hilda",
        "Current",
        "Leif",
        "Ratan",
        "Mourella",
        "Lal",
        "Per",
        "Madrigal",
    ],
]

greenwise_tables = [
    {
        "name": "How have The Woods failed you?",
        "options": {
            1: """An ill-tempered forest spirit cursed you for stealing, marking you as an
enemy of their kind. Take a <b>Bezoar Stone</b>. Ingesting it cures any poison
(1 use, unless retrieved).""",
            2: """A close friend, swallowed whole. Now you see their face in any tea you
brew. Take a <b>Soporific Concoction</b> (3 uses).""",
            3: """You were poisoned, losing your sense of taste and smell. You can now
withstand noxious fumes, and always carry Antitoxin (2 uses).""",
            4: """Your radical experiments turned your skin green, and you now gain
nourishment as a plant. You don’t need <b>rations</b>, but a day without
sufficient sunlight and water leaves you deprived.""",
            5: """Your impressive corpseflower won a local contest then promptly killed a
judge. You fled, but not without the <b>Prize Money (100gp)</b> and a warrant
for your arrest.""",
            6: """You created a restorative tincture that also caused accidental infertility.
Take a <b>Healing Potion</b> that completely restores STR. Only you know of its
unintended side-effects.""",
        },
    },
    {
        "name": "What keeps you safe while in The Woods?",
        "options": {
            1: """<b>Amadou</b> A vermillion fungus that catches fire quite easily (3 uses).""",
            2: """<b>Delphinium</b> Breathe water for up to one hour (1 use, but can be divided into fractional doses).""",
            3: """<b>Tacky Stalk</b> A woody reed that hardens into a permanent adhesive when chewed (2 uses).""",
            4: """<b>Wisp Lantern</b> Caged in wrought iron, provides a dim light so long as the wisp is able to feed on nearby pain and fear.""",
            5: """<b>Seed Bomb</b> A canvas sack filled with seeds that explodes on impact.  d6 damage (<em>blast</em>, 3 uses).""",
            6: """<b>Briarvine</b> Entangles any creature up to horse size (STR to break free, reusable).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Iron Pot",
        "Root Knife (d6)",
        "Healing Salve (restores 1d4 STR, 1 use)",
        """Twine Bauble (<em>petty</em>, <em>Ward</em> once per day),<br>
<em><b>Ward</b>: A silver circle 50ft across appears on the ground.
<br>
Choose one species that cannot cross it</em>.""",
    ],
    # profile
    """You delve deep into <b>The Woods</b>, prying its secrets from between rough boughs
and whispering leaves. In this verdant kingdom, you are no mere scholar, but its
confidant as well.""",
    # names
    [
        "Briar",
        "Moss",
        "Fern",
        "Lichen",
        "Root",
        "Willow",
        "Sage",
        "Yarrow",
        "Rowan",
        "Ash",
    ],
]


half_witch_tables = [
    {
        "name": "What did you bring back from the unseelie court?",
        "options": {
            1: """A <b>Black Rose Fiddle</b> (<em>bulky</em>). Its music causes intense sadness and
immobility in nearby mortals (others are merely fascinated). You don’t
know how to play.""",
            2: """<b>Paper Legs</b>. You are extremely light, and can fall a few stories without
getting hurt. Try to avoid tearing them or getting them wet.""",
            3: """A <b>Living Nightmare</b> that dwells within you, but manifests whenever you
are in danger. It has your same Attributes and HP, and attacks with claws
(d8+d8). It disappears on <b>Critical Damage</b> (take 1d4 WIL damage), re-
appearing again on the next full moon.""",
            4: """A <b>Raven Familiar</b> [8 HP, 3 STR, 11 DEX, 13 WIL, beak (d6)]. It speaks as an
intelligent being and is entirely devoted to you.""",
            5: """A <b>Briar Thorn</b>. It can pierce any organic material (quite painfully) but
when removed leaves no trace of the intrusion.""",
            6: """A Fae creature’s <b>True Name</b>. Use it to summon its owner for an act of
great service, but only once. It could also fetch a hefty price, to the right
buyer.""",
        },
    },
    {
        "name": "What concoction do you carry, and what rare ingredients did you gather to make it?",
        "options": {
            1: """<b>Rebirth Ash</b> Remnants of a bark spirit. Sprinkle to reignite a fire that
has died, or return to life a creature that has died only
moments before (3 uses).""",
            2: """<b>Glamour Feather</b> Plume of a firebird. Can make any creature appear
convincingly as someone (or something) else (1 use).""",
            3: """<b>Hawthorn Seed</b> An acorn from the other side, gathered on the spring
equinox. When planted it sprouts a luxurious shelter,
collapsing at moonrise the next day (1 use).""",
            4: """<b>Stonetree Sap</b> Sap obtained in exchange for blood. Hardens when rubbed
on any surface (+1 Armor, 3 uses).""",
            5: """<b>Nightdust Powder</b> Made from the ritual burning of six owls. When tossed in
the air, day turns to night for a short while (2 uses).""",
            6: """<b>Hex Stone</b> Gathered from a river that flows from the other side.
Removed from its iron tin, it can absorb the effects of
an active magical effect. If destroyed, the magic is
released (1 use).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Spellbook (<em><b>Thicket</b>: A thicket of trees and dense brush up to 50ft wide suddenly sprouts up.</em>)",
        "Iron Dagger (d6)",
        "Herbs Pouch (restore 1 STR, 3 uses)",
        "Ghillie Suit",
    ],
    # profile
    """Born of both the mortal world and the unseen, a crossing of veils that makes you
an enigma to many.<br>You are both a conduit and a caution of what happens when two worlds collide.""",
    # names
    [
        "Solena",
        "Veles",
        "Bryn",
        "Sabine",
        "Razvan",
        "Rowena",
        "Galen",
        "Nyx",
        "Vex",
        "Iwan",
    ],
]


hexenbane_tables = [
    {
        "name": "To which order do you belong?",
        "options": {
            1: """<b>Order of the Crossroads</b>. Take a <b>Pocket Leyfinder</b>. It points to nearby ley
lines and other sources of arcane power. If you lose it, the punishment is
death.""",
            2: """<b>Order of the Bleeding Star</b>. Take a <b>Star-Iron mace (d8)</b>. It shines faintly in
darkness, and becomes very hot in the presence of witchcraft.""",
            3: """<b>Order of the Glass Sigil</b>. Take a <b>Short Sword (d8)</b> and Chainmail</b> (2 Armor,
<em>bulky</em>). You have contacts in most towns (the more rural, the better)
willing to provide aid, food, or even weapons.""",
            4: """<b>Order of the Blank Eye</b>. Take a <b>Voidglass Shard</b>. Peer through it to see
invisible marks, creatures, and other magical effects.
Lose the use of your eye for an hour afterwards (you are <em>deprived</em>).""",
            5: """<b>Order of Canaas</b>. Once per day you can change into a wolf. Take a <b>Quicksilver Chain</b>. Without it, you are unable to shift back.""",
            6: """<b>Order of the Silent Veil</b>. Take a <b>Quell Stone</b> (2 uses) wrapped in burlap.
Extinguishes any nearby flames once exposed to air.""",
        },
    },
    {
        "name": "What was your vow?",
        "options": {
            1: """<b>Honesty</b>
Choose a weapon type (blunt, blade, etc). Attacks against
you of this type are impaired. If your vow is broken, you
lose d4 WIL.""",
            2: """<b>Poverty</b>
You carry the Disassemble Spellbook. Only you can use it.
If your vow is broken, it explodes (d12 STR damage).
<br>
<em><b>Disassemble</b>: Any of your body parts may be detached and
reattached at will, without causing pain or damage. You can
still control them.</em> """,
            3: """Selflessness</b> You are immune to magical effects such as charm, hatred,
frenzy, and so on. If you break this vow, you lose d6 WIL.""",
            4: """<b>Mercy</b> Choose a weapon type (blunt, blade, etc). Attacks with
this weapon are enhanced. If your vow is broken, you can
never use that weapon type again.""",
            5: """<b>Charity</b> Once per day you can shrug off a Fatigue. If your vow is
ever broken, you permanently lose one inventory slot.""",
            6: """<b>ValorT</b> he first time you inflict Critical Damage you receive d4
HP, returning to the previous limit at the end of combat. If
your vow is broken, you die.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Vestments of the Order (<em>petty</em>)",
        "Blessed Tinctures",
        "Silver Knife (d6)",
        "Crossbow (d8, <em>bulky</em>)",
    ],
    # profile
    """
    You are a mere digit on the unerring hand of justice. You go where others fear to
tread, unyielding and unbroken.
    """,
    # names
    [
        "Percival",
        "Felix",
        "Isolde",
        "Wolfram",
        "Aldric",
        "Eira",
        "Oswin",
        "Ivor",
        "Brunhilda",
        "Beatrix",
    ],
]

template_tables = [
    {
        "name": "What Keeps You Safe on the Streets?",
        "options": {},
    },
    {
        "name": "Type of Scum",
        "options": {},
    },
    # starting gear
    [],
    # profile
    """""",
    # names
    [],
]
BACKGROUND_TABLES = {
    "Aurifex": aurifex_tables,
    "Barber-Surgeon": barber_surgeon_tables,
    "Beast Handler": beast_handler_tables,
    "Bone Keeper": bonekeeper_tables,
    "Cutpurse": cutpurse_tables,
    "Field Warden": field_warden_tables,
    "Fletchwind": fletchwind_tables,
    "Foundling": foundling_tables,
    "Fungal Forager": fungal_forager_tables,
    "Greenwise": greenwise_tables,
    "Half Witch": half_witch_tables,
    "Hexenbane": hexenbane_tables,
}
