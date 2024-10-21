backgrounds = [
    "MERCENARY",
    "HUMAN EXPERIMENT",
    "ENGINEER",
    "SMUGGLER",
    "PILOT",
    "MACHINE",
    "UNDERWORLD",
    "PSIONIC",
    "SCIENTIST",
    "SOLDIER",
    "STAR-TOUCHED",
    "BOUNTY HUNTER",
]

dossier_mercenary = [
    {
        "name": "Signature Weapon",
        "options": {
            1: "<b>Ifriti-9000 “Hell Spitter”</b> (D10 Blast, Thermal, Bulky) and 2 tanks of fuel (spec-ammo). A deluxe model flamethrower that sprays super-thermal plasma that can burn through metal.",
            2: "<b>Folding Vibro-Shank</b> (D6, Deadly, Shock, concealable) A five-inch blade that does absolutely devastating damage. Folds up for concealing. Very-illegal.",
            3: "<b>Supercharged Carbine Repeater</b> (D8 Thermal and d6 Cryo, bulky) Custom modded to switch between thermal or sub-zero energy rounds. Switching takes 1 turn.",
            4: "<b>Jade-Iron Machete (D8, Deadly)</b> 3 feet of marbled green metal with a wicked cutting edge. Expert craftsmanship and quite valuable.",
            5: "<b>“Trusty”</b> (D6 Blaster) & <b>“Rusty”</b> (D6 Blaster, Cheap) These two guns have been with you through thick & thin.",
            6: "<b>“Rusty”</b> (D6 Blaster, Cheap) You used to have two but lost the good one…",
        },
    },
    {
        "name": "Old Crew Specialty",
        "options": {
            1: "<b>Para-Military:</b> Private sector military for hire. You were, and probably still are, an absolute professional. Take holo-binocs and a claymore.",
            2: "<b>Seedy Jobs:</b> Hired muscle contracted through criminal syndicates, you are familiar with the less savory parts of the galaxy. Take a grimy outfit, a pack of smokes, & 6d12 worth of underworld trade goods.",
            3: "<b>Ghost Unit:</b> Your crew specialized in delicate matters that needed doing discreetly and without a trace. Take plasti-steel armor (Armor 1, bulky) and a gas mask.",
            4: """<b>Hit Squad:</b> Assassinations were
            your bread & butter. Take a
            thermal detonator, a dark outfit,
            and an infrared visor helm (Armor
            1, heat vision)""",
            5: """<b>Corp-Sec:</b> Private megacorporate
                security for a major faction.
                Generate a faction and NPC and
                determine what type of business.
                Take the talent “Human Shield”.""",
            6: """<b>Deep Cover:</b> Specialists in
            infiltration as double agents for
            espionage and intel gathering.
            Take an auto-lock slicer, drone
            cam, and fake ID.""",
        },
    },
    {
        "name": "What happened?",
        "options": {
            1: """<b>Last Man Standing:</b> Something
bad happened and everyone
turned on each other. It was a
bloodbath and you were the last
man standing...at least you think.""",
            2: """<b>Betrayal:</b> Were you the leader, or
were you a betrayer? Or was the
whole crew betrayed by someone
- inside or out? Either way, the
crew broke up and you have to
make your own way.""",
            3: """<b>Things Just Change...:</b> Or maybe
you changed. Either way, you
decided you didn’t want to do
what they did anymore, and
broke off on your own.""",
            4: """<b>Splintered:</b> The group splintered,
maybe from a disagreement in
leadership, or infighting, and
splinter groups broke off.""",
            5: """<b>Kicked Out:</b> Whether it was from
breaking the rules, or not seeing
eye-to-eye with the brass, you
were exiled from your crew on
bad terms.""",
            6: """<b>Left Behind:</b> Things went
sideways on your last mission
and you got left behind mission,
considered MIA or dead. Maybe
it’s time for a fresh start.""",
        },
    },
    ["Old Crew Emblem", "Combat Knife (D6) or 2 Flash Grenades", "Cigar"],
    # profile
    """Mercenary crews are guns for hire. They have experience in combat, insider
knowledge of the violence business, and are a little rougher around the edges than
others. You and your old crew fought for the highest bidder, not for any sort of
ideology. Unless that ideology was lots of creds.""",
]

dossier_human_experiment = [
    {
        "name": "Side-Effects",
        "options": {
            1: """"<b>Exothermic Lungs:</b> Exhale a superheated spray of plasma (D10 blast, thermal).
Costs 1 fatigue""",
            2: "<b>Magnetism</b> Manipulate metal objects up to 100 lbs with your mind. Costs 1 fatigue.",
            3: "<b>Ghost Skin</b> Willingly phase through solid objects up to 3 feet thick. Costs 1 fatigue.",
            4: """<b>Elasticity</b> Your arms and hands can stretch and change form up to 20 sq feet or 60 feet
in length.""",
            5: "<b>Biomimicry</b> Change or alter your face and skin once a day.",
            6: """<b>Ultra-Conductive</b> You can discharge, locally disrupting all nearby computers and
circuitry once a day. Immune to electricity and EMP damage.""",
        },
    },
    {
        "name": "Type of Experiment",
        "options": {
            1: """<b>Grown in a Tube:</b> You are the
product of scientific brilliance.
You’ve only seen the outside
world while floating inside a vat
of life-sustaining fluid.""",
            2: """<b>Brain Stress:</b> They hooked your
brain up with wires and pushed
your mind to the limits. You know
one random Psionic power.""",
            3: """<b>Nanobot Infusion:</b> Some type
of prototype serum was injected
into your bloodstream. Your
body can naturally heal 1D4 STR
damage a day.""",
            4: """<b>Gene-Splicing:</b> Bio-Engineering
via illegal methods made your
body more hardy and adaptable.
You naturally have 1 armor.""",
            5: """<b>Ghost-Shell:</b> You are a recently
re-animated or unwilling
consciousness implanted into
a synthetic body. You know one
random Astromancy from your
previous life. Your memory is
slowly returning in pieces...""",
            6: """<b>6 Billion Credit Person:</b> You
were a pet project of some
unknown billionaire. They were
attempting to create a perfect
specimen. The project was
considered a partial failure.
Increase one Ability Score to 16.""",
        },
    },
    {
        "name": "How Did You Escape?",
        "options": {
            1: """<b>Violently,</b> by turning your powers
on your captors. Take a bloody
scalpel (D6)""",
            2: """<b>Furtively,</b> you somehow
managed to sneak out in the
dead of night. Take stolen
records worth 4d8 credits on the
black market and notes on how
to find them.""",
            3: """<b>Benevolently,</b> an unknown figure
unlocked your restraints while
nobody was there. When you
woke up, your escape was wide
open. Take a mysterious business
card.""",
            4: """<b>Inexplicably,</b> incomprehensible
quantum displacement shifted
you somewhere completely
random. Take a random weapon
(Roll 1D4). 1-2: small melee, 3:
stun gun, 4: junky blaster.""",
            5: """<b>Compliantly:</b> You didn’t need to
escape, the experiment suddenly
ended and you were released
in the middle of nowhere, with
no way of knowing who had
experimented on you. Your
account now has 2,000 credits as
payment.""",
            6: """<b>Cargo Mix-up:</b> You were being
shipped somewhere and
the manifests got mixed up.
Someone found you and let you
go. The original experimenter is
still looking for you. Take 1D6
random drugs or contraband
items.""",
        },
    },
    # starting gear
    ["Cloak (Hooded)", "Flashlight", "Tattoo (Serial Number or Bar Code)"],
    # profile
    """You have been the subject of unethical and experimental scientific tinkering.
There were some side effects. You recently managed to escape.""",
]


dossier_engineer = [
    {
        "name": "Pet Project",
        "options": {
            1: """<b>Dimension De-stabilizer:</b> Tech belt that allows the wearer to slip in and out of reality.
You cannot interact with anything in this reality but are still visible.""",
            2: """<b>Division Multiplier:</b> Harness that when activated splits you into two smaller versions of
yourself. HP & Ability Scores are halved. Inventory exists in a quantum state; items used
by one version are inaccessible to the other. Lasts 1 minute. Causes 1 fatigue.""",
            3: """<b>Molecular Shield Generator:</b> (+1 armor, 3 bonus HP a day) Swarm of fly-sized nanobots
orbit you, occasionally running scans on your biological makeup, providing you with
customized shielding and protection. Bonus HP takes a day to recharge.""",
            4: """<b>Anti-Grav Boots:</b> Activate to reduce your fall speed at the last second and land safely.
Recharge via 100 credit worth of common battery parts in 1d6 hours.""",
            5: """<b>Catherine:</b> An A.I. chip you can implant into any basic device. Currently installed in your
personal comm unit. Catherine is very polite. Will warn you of any imminent danger you
might not notice. May run advanced diagnostics.""",
            6: """<b>Spider-Wasp Drone:</b> A spider-sized drone that can quietly fly, crawl on most surfaces,
and transmit video footage up to 200ft.""",
        },
    },
    {
        "name": "Technical Expertise",
        "options": {
            1: """<b>Cyberware:</b> Take Smart-Eye
implants (Eye Socket.) 10x zoom,
recording & playback.""",
            2: """<b>Starships:</b> You can fix any part of
a ship, but it takes 2D12 hours.""",
            3: """<b>Weapons:</b> Take a Mass Untangler
(D8, illegal, critical damage
instantly disintegrates organics if
they fail a STR save)""",
            4: """<b>Security Systems:</b> You can get
through manually locked doors
and shut down surveillance with
minimal effort and tools.""",
            5: """<b>Robotics:</b> Take a chest harness
(1 slot) with a robotic arm on
it that can carry a weapon and
perform similar actions to your
own arms. Only works with your
DNA signature.""",
            6: """<b>Software:</b> You have increased
effect and reduced failure when
performing tasks related to
computers, hacking, and using
software or user-interfaces.""",
        },
    },
    {
        "name": "Savant Specialty",
        "options": {
            1: """<b>Gearhead:</b> You can spend 1 turn
(10 min) tinkering with most
fist-sized objects you’re familiar
with to get them at least partially
working.""",
            2: """<b>0110101001:</b> You’re oddly
persuasive to A.I. and computing
systems. +1 to reaction roll
results with machines and
synthetics.""",
            3: """<b>MacGyver:</b> You can fix almost
anything with duct tape, holding
anything broken together as if
undamaged for 1D6 hours. Also,
generally handier than almost
anyone else.""",
            4: """<b>Fried Wires:</b> You’ve tinkered with
enough electronic components
that shock damage and anything
electric only damages your
HP, completely ineffective at
damaging your Ability Scores.""",
            5: """<b>Jack of All Trades:</b> You’re
pretty good at everything. Once
a day you can take one fatigue
to accomplish something that
would otherwise require a Save.""",
            6: """<b>Black Lung:</b> Inhaling enough
machine smog has given you a
degree of immunity to inhaled
toxins and other harmful
breathable substances.""",
        },
    },
    # starting gear
    ["Crowbar (D6)", "Duct Tape", "Grease-stained work clothes"],
    # profile
    """You’ve built a career around being handy. You’re skilled at repairing and maintaining
mechanical structures and devices.""",
]

dossier_smuggler = [
    {
        "name": "Lucky Charm",
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
        "name": "Recent Entanglements",
        "options": {
            1: """<b>Botched Job:</b> You had to dump
your cargo in space to escape
pursuit by authorities. Your client
is furious. You are trying to lay
low.""",
            2: """<b>Early Retirement Gift:</b> You
lifted the goods from a job for
yourself and said goodbye to the
smuggler life. Unfortunately you
are now wanted (alive) for 2000
creds by a major gang.""",
            3: """<b>Busted:</b> Mix-up with local system
authorities. Well, not so much as
a mix-up as...you’re blacklisted
from there. (Blacklisted in next
system you travel to)""",
            4: """<b>Flawless Career:</b> You were one
of the best and you’ve managed
to retire without incident. Your
reputation grants you 10%
discount from any underworld
dealers.""",
            5: """<b>Jail Time:</b> After getting caught,
you served some jail time. You’re
just now getting out and have
decided to try a change of career.""",
            6: """<b>Criminal Elements:</b> Your
smuggling services have recently
disrupted a local criminal
element’s business.""",
        },
    },
    {
        "name": "Trick Up Your Sleeve",
        "options": {
            1: """<b>Nine Lives:</b> Once daily, if an
attack does more damage than
your remaining HP, instead only
reduce your HP to 1 and avoid a
Save vs Critical Damage. (If this
happens a 10th time, Save vs
Corruption and add +10 to the
Hollowing roll if you fail.)""",
            2: """<b>Shoot First:</b> Don’t roll initiative
in the first round of any combat,
just go first.""",
            3: """<b>Local Parlance:</b> You instantly
pick up the common way of
speaking and know how to sound
like you belong. This carries
massive street cred, especially
with criminals.""",
            4: """<b>Under the Radar:</b> Any smuggler
worth their salt knows how to
keep their head down when
working - you have an especially
effective touch at dodging local
authorities.""",
            5: """<b>Lovely Eyes:</b> Once a day you may
persuade someone who would
feasibly find you attractive to do
you a favor or believe a lie.""",
            6: """<b>Down But Not Out:</b> When you
go down after failing a save vs
critical damage, you can still fire
a one handed gun. This may draw
unwanted attention.""",
        },
    },
    # starting gear
    [
        "Blaster (D6)",
        "Stylish Outfit",
        "Fake Clearance Codes (1)",
        """<b>GM Optional</b>, start with a small starship (stolen or indebted) with smuggling
holds. It’s currently impounded or stolen.""",
    ],
    # Profile
    """Running contraband goods for underworld clients is a dangerous game, but you’ve
gotten good at staying under the radar.""",
]

dossier_pilot = [
    {
        "name": "Suited Up",
        "options": {
            1: """<b>Deluxe Array:</b> Holo-shades (improve visuals in darkness, look slick), armor-lined red
jacket (1 Armor), and 2 blasters (D6), pack of alien cigars (blue smoke)""",
            2: """<b>Alien Companion:</b> Generate a retainer (merc) with one unique feature befitting an alien
species (alternatively can be a droid or other non-human.)""",
            3: """<b>Exo-Skin Suit:</b> (1 armor) Nanotech morph suit, conforms to your body, wear under your
regular clothes. Has a built in grappling gun and rebreather mask.""",
            4: """<b>Stylin’:</b> Take a dashing outfit and cloak, silver-plated blaster (d6, replace starting
weapon) and a thermal detonator (d6, blast, thermal).""",
            5: """<b>Committed to Flying:</b> Take a datajack implant (Cerebral Socket). Installs the back of
your head with a jack that allows you to plug into vehicles to more rapidly access special
systems and data.""",
            6: """<b>Just the Essentials:</b> Take a leather jacket, a stun gun and a retractable baton (D6,
concealable)""",
        },
    },
    {
        "name": "Flying Expertise",
        "options": {
            1: """<b>Captain:</b> You have experience
leading, and either through
admiration or fear, others find
your presence to be motivational
in dire circumstances.""",
            2: """<b>Astro-Navigator:</b> You know your
way around space. You never
get lost in space and always get
around fast.""",
            3: """<b>Ace:</b> You always have a few fancy
moves when you’re in the pilot
seat. When you pull off a daring
move the results tend to go in
your favor, at least on the first try
of the day.""",
            4: """<b>Union Licensed:</b> It was an
honest living. Other pilots respect
that. You get union discounts for
yourself and friends with starport
docking, lodging, and buying
anything starship related.""",
            5: """<b>Syndicate Contractor:</b>
Any reaction rolls or social
encounters with professional
syndicates are one category
higher, or more favorable in
another abstract way.""",
            6: """<b>Test Pilot:</b> You can pilot anything,
and are experienced at operating
vehicles that are damaged or
partially broken. If your ship
takes critical damage, delay the
negative effects for 1D4 rounds.""",
        },
    },
    {
        "name": "Other Talents",
        "options": {
            1: """<b>Hot-Wiring:</b> You know how
to cross the right wires to get
vehicles running that don’t
belong to you.""",
            2: """<b>Hard Turns:</b> Gain an additional
point of mobility in any starship
you’re piloting.""",
            3: """<b>Lead Foot:</b> Gain an additional
point of movement in any
starship you’re piloting.""",
            4: """<b>Energy Efficient:</b> You know how
to turn dashboard systems on-and-off in such a way that your
shields have an additional +1.""",
            5: """<b>Counter Tactics:</b> If you lose
initiative at the start of starship
combat, the first attack your ship
makes will be enhanced.""",
            6: """<b>Witty Banter:</b> During starship
combat, hilarious yelling or witty
banter with a co-pilot or onboard
A.I. allows you to automatically
succeed on a single critical
damage save a day.""",
        },
    },
    # starting gear
    [
        "Mag-boots",
        "Junky blaster (D6, cheap, mid-range)",
        "<b>GM Optional</b>, start with a small Starship. Make it impounded or in need of repairs.",
    ],
    # profile
    """You feel most comfortable behind the controls of a starship. Quick reflexes and
situational awareness make you an asset in many situations.""",
]

dossier_machine = [
    {
        "name": "Custom Hardware",
        "options": {
            1: """<b>Heat-Wave Optics:</b> (D8, or D6 blast, thermal) Eye lasers. Take 1 fatigue.""",
            2: """<b>Reinforced Casing:</b> If you take max damage from an attack, half it.""",
            3: """<b>Auto-Targeting Subroutine:</b> Re-roll damage results of 1.""",
            4: """<b>Overclocked Processors:</b> Re-roll 1 DEX save a day.""",
            5: """<b>Hidden Storage:</b> Two extra inventory slots inside your chassis.""",
            6: """<b>High-Speed Data Jack:</b> Improved hacking into networked systems.""",
        },
    },
    {
        "name": "Model Type",
        "options": {
            1: """<b>Droid:</b> Standard bi-pedal,
humanoid robot. Explain your
original purpose and what you
look like. You have natural +1
armor.""",
            2: """<b>Android:</b> You look mostly human.
You are not. Synthetic androids
are often discriminated against.
Your build quality is fluid and
graceful, take +1 DEX.""",
            3: """<b>Rogue A.I.</b> Your chassis is
a bit unconventional, as you
are primarily an A.I. core that
escaped via hacking into and
commandeering another vessel.
Explain how your frame is built.
You can temporarily swap bodies
with other machines, taking them
over, for 1d4 hours (1 fatigue).""",
            4: """<b>Lazarus Machine:</b> You are the
last remains of an intelligent
organic being, and mostly
brain tissue at this point. Your
consciousness was uploaded into
this robotic body. Your chassis
was designed to be heavily
modded. 50% discount on all
cyberware.""",
            5: """<b>Bio-Synth:</b> You’re composed
of a mix of mechanical and
biological parts. You can use and
get a 50% discount on genetic
modifications.""",
            6: """<b>Incomplete Prototype:</b> You
function well enough, but were
never fully completed for the
original purpose of your build.""",
        },
    },
    {
        "name": "Manufacturer",
        "options": {
            1: """<b>Jury-Rigged:</b> You are composed
of several lightly used parts
from various other machines
by an unknown builder. Some
components weren’t installed
correctly.""",
            2: """<b>Military-Industrial:</b> You
were built for tactical military
purposes.""",
            3: """<b>Savant Engineer:</b> You’re the
creation of a genius inventor.""",
            4: """<b>Alien Society:</b> An alien species
built you, and it shows in your
build. Explain your unusual
appearance.""",
            5: """<b>Ancient Maker:</b> This
manufacturer and all of their
creations are long gone. You’re
rare, incredibly antiquated, yet
still in immaculate condition.""",
            6: """<b>Megacorp:</b> Your line has been
mass produced for a giant
corporate entity.""",
        },
    },
    # starting gear
    ["Short Rifle (D6, bulky)", "Antivirus.EXE (1 use, removes 1 fatigue)"],
    # profile
    """All machines have a purpose. What was yours, and what will it become? Machines
can only take <b>cyberware augmentations</b>. They must make sense for your model
type. You <b>do not need to eat or breathe</b> and cannot take damage from sources that
rely on those functions (breathing, poison, etc). You are <b>immune to mind-altering
effects</b>. You must sleep (re-boot/defrag/update) roughly as much as everyone else.
<b>Shock does double damage.</b>""",
]

dossier_underworld = [
    {
        "name": "What Keeps You Safe on the Streets?",
        "options": {
            1: """<b>Ultraviolet Shotgun:</b> (D8 blast, cryo, illegal). Black market weapon that emits sub-zero
wavelengths. Particularly devastating to unarmored flesh.""",
            2: """<b>Heart-Stopper Helmet:</b> Face-mask that looks like a devil (+1 armor) and emits a low-
frequency hum, unsettling others. Can discharge a 30’ sonic blast (D6 sonic) once a day.""",
            3: """<b>“Brick”:</b> Take a freelancer (merc) with 12 STR, 8 DEX, 6 WIL, 3 HP, Billhook (D6, bulky)
They’re not the brightest bulb, but they’re pretty large and intimidating. Rename if you
wish.""",
            4: """<b>Red Hyena:</b> (6 HP, 14 DEX, D6 bite, critical damage save vs STR or break a bone) A very
large, red coated hyena. Obeys you via a neural link, but some of its affection might be
natural.""",
            5: """<b>Prototype Vibro-spear:</b> (D8, bulky, shock) Considered a truly nasty weapon.""",
            6: """<b>Synth-weave Duster:</b> (1 armor, lots of pockets) It’s like a jacket only it’s longer, thicker,
and far more bad-ass.""",
        },
    },
    {
        "name": "Type of Scum",
        "options": {
            1: """<b>Thug:</b> You are good at cheap
shots. Attacks are enhanced on
an enemy that has been hit in the
same round.""",
            2: """<b>Fence:</b> You always know
someone from whom to get more
creds from selling treasure.""",
            3: """<b>Scoundrel:</b> You worked for
yourself. +1 HP and take a lead
on a lucrative job.""",
            4: """<b>Goon:</b> You did the shakedowns.
You impose DIS on anyone
making a WIL save against your
intimidation efforts.""",
            5: """<b>Ex-Syndicate Captain:</b> You used
to be a top dog in a syndicate
until you were double crossed
and kicked out. Roll a random
Ex-Tech you “liberated” on the
way out.""",
            6: """<b>Fixer:</b> You were a fixer, setting up
jobs for the criminal underworld.
You can negotiate for higher pay
on jobs involving criminal activity.""",
        },
    },
    {
        "name": "Criminal Knack",
        "options": {
            1: """<b>Know A Guy:</b> You can figure out
how to contact someone seedy
in any city after an hour of asking
around.""",
            2: """<b>Forging Documents:</b> Can make
a fake ID for 50 creds, and
other similar forgeries of varying
quality depending on costs.""",
            3: """<b>Cheating:</b> If you’re gambling,
playing games of chance, or
making some sort of agreement
with someone, you’re especially
good at cheating and not getting
caught.""",
            4: """<b>Talking Shop:</b> Reaction roll
results are always one category
higher with others of the criminal
persuasion.""",
            5: """<b>Politically Crooked:</b> You know
how governments work and
just how corrupt politics can be.
Any factions of the government
variety deal favorably with you.""",
            6: """<b>Sticky Fingers:</b> Picking pockets,
lifting goods, and general larceny
comes quite easily to you,
granting you ADV if you take a
measured, intelligent approach
with the proper tools.""",
        },
    },
    # starting gear
    ["Old Shotgun (D6 blast, bulky, cheap)", "Smart meds", "Bolt cutters"],
    # profile
    """Just another low life trying to make a few creds. You likely have ties to other
criminals and criminal organizations, syndicates, and less reputable individuals.
Whether you worked for them, worked alone, or had some other arrangements
might depend.""",
]

dossier_psionic = [
    {
        "name": "Psionic Awakening",
        "options": {
            1: "<b>You are Gifted.</b> Shatter: Your voice echoes with the sound of an earthquake, causing d8 damage (blast 20’) to creatures, and shatters delicate objects. Take 1 fatigue.",
            2: "<b>You are Psychic.</b> Read Thoughts: You can hear the surface thoughts of nearby creatures and can communicate telepathically, either clearly in languages you know, or a general sense of emotions in languages you are unfamiliar with.",
            3: "<b>You are Telekinetic.</b> Telekinesis: You may mentally move an item under 60lbs. Take 1 fatigue.",
            4: "<b>You are a Mesmer.</b> Spectacle: A clearly false but impressive illusion of your choice appears, under your control. It may be up to the size of a palace and has full motion and sound.",
            5: "<b>You are a Precog.</b> Vision: Once a day, roll a 1d20 and keep that roll. You may substitute that roll for any Save you, an ally, or an enemy makes after seeing the results. Gain 1 fatigue when you roll your vision and keep it in inventory until the dice is used.",
            6: "<b>You are an Esper.</b> Calm: A creature you can see is soothed and treats you as a friend for 1d6 hours. Take 1 fatigue.",
        },
    },
    {
        "name": "Old Cover Identity",
        "options": {
            1: "<b>Ship Crewmate:</b> You got by as a shiphand. You have technical know-how of starships. Take a blow torch and super glue.",
            2: "<b>Corporate Processor:</b> Hiding in plain sight, day to day, was quite boring. You know the ins-and- outs of bureaucracy, and usually roll with ADV when making any rolls involving corporations or business.",
            3: "<b>Private Investigator:</b> Your powers are quite useful when it comes to P.I. work. Take infrared smart-binocs and an area scanner. Oh, and a cool hat.",
            4: "<b>Charlatan:</b> A fool and his money, as they say. Running scams are just easier when you have psionic. Take 10d6 credits and a low level bounty for petty crimes.",
            5: "<b>Pilgrim:</b> You lived a simple life following the path inside. You learned to open your mind and attune to your gifts. Roll another random psionic power.",
            6: "<b>Military Peon:</b> The rigorous life of a military grunt was a simple way to get by. Your service is up now. Take a Shard-sprayer (D8 blast, bulky) and grunt armor (Armor 1, bulky).",
        },
    },
    {
        "name": "Neural Ramifications",
        "options": {
            1: "<b>Draining:</b> You are always so utterly tired. Permanently mark off one inventory slot.",
            2: "<b>Med-Addicted:</b> You only recover fatigue from staying at a hospital or taking expensive stims (50 C).  Optionally you can heal normally and Save vs. Corruption",
            3: "<b>Paranoid:</b> <em>“Who’s there?!”</em> Whenever you are surprised or ambushed, you always go last in the first round.",
            4: "<b>Split Personality:</b> It’s not you who has these brain problems, it’s the other one in your head!",
            5: "<b>Surly:</b> You come across a little coarse. People of higher social standings naturally don’t like for you.",
            6: "<b>Empathetic Overtuning:</b> When an ally saves vs. corruption, you do too.",
        },
    },
    # starting gear
    [
        "Cheap blaster or small melee weapon",
        "Fake I.D.",
        "Adrenaline injection (1)",
        "Candy bar",
    ],
    # profile
    """A power within you has awoken. Whether from trauma, an evolving mind, or some
other key, the locks have started to open on a deep seeded source of power.
When a psionic character undergoes major stress, trauma, or levels up, consider
letting them awaken a new power. Optionally, instead of new powers, consider
evolving the effects of their awakening ability.""",
]

dossier_scientist = [
    {
        "name": "Prized Lifetime Research",
        "options": {
            1: "<b>Skeletal Resonator:</b> Attract or repel a single target that has a skeleton, unless they pass a STR save. No effect on cartilage.",
            2: "<b>Portal Generator:</b> Create a portal between two flat sources that you can see. The gate closes if you pass through or break line of sight. Causes 1 fatigue.",
            3: "<b>Temporal Bomb:</b> Time slows down 60 times in a 20 foot sphere (blast). Lasts for 1 minute outside the sphere, or one second inside. One use.",
            4: "<b>Corpse Reviver #42:</b> Brings back the dead if used within 1 minute of death. One use.",
            5: "<b>Particle-Mirror Array:</b> (+1 Armor) A molecular shield generator. Once a day, make a DEX save to reflect energy weapon shots back at their source.",
            6: "<b>Creature in a Jar:</b> A baby sludge creature with one eye. Upon release, it will eat a corpse’s brain consuming its memories, effectively allowing the user to ask a corpse one question. The fresher the corpse, the better the memory. Needs a day to rest before it will come back out.",
        },
    },
    {
        "name": "Field of Expertise",
        "options": {
            1: "<b>Medical Doctor:</b> Take medical supplies that can restore 1d4 STR a day.",
            2: "<b>Molecular Chemist:</b> Take a vial of universal solvent, which dissolves anything it touches.  Enough for a brick-sized portion.  One use.",
            3: "<b>Experimental Physicist:</b> Take a can of de-friction spray. 3 charges.",
            4: "<b>Xeno Biology:</b> Take a strange alien Gecko-Fox as a pet. (3hp, 14 DEX, d6 bite, can climb sheer surfaces, must be fed something living once a week)",
            5: "<b>Toxicology:</b> Years of experimentation, immunity- building & study have provided you an immunity to all known poisons, and reduced effect on failed saves against unknown or alien toxins and poisons.",
            6: "<b>Higher Dimensions:</b> Prying open the secrets of the universe have exposed you to things you can’t explain. Roll for a random Astromancy.",
        },
    },
    {
        "name": "Why You Left Science",
        "options": {
            1: "<b>Uncouth Research:</b> You dabbled in things that are frowned upon and were run out of academia.  Start with 3 corruption.",
            2: "<b>Malaise:</b> You wanted new challenges and life in the lab just wasn’t cutting it anymore. Roll a random talent.",
            3: "<b>Blackmail:</b> A rival researcher, competitor, or criminal organization implied that if you didn’t stop your current research, they’d stop it for you.",
            4: "<b>Lab Accident:</b> There’s a corporate-sponsored bounty on your head for damage to company property.",
            5: "<b>Research De-funded:</b> Due to budgetary issues, your research has been placed on permanent hold. Sorry.",
            6: "<b>Field-Research:</b> You wanted more hands-on experience in your field.",
        },
    },
    # starting gear
    [
        "Lab coat",
        "Test tubes (6) & assorted medical tools",
        "Plasma-Knife (D6 thermal, concealable)",
    ],
    # profile
    """You’ve spent most of your life dedicated to the advancement of science. Due to new
circumstances, you’ve decided to make the change from lab work to field work.""",
]

dossier_soldier = [
    {
        "name": "Special-Issue Equipment",
        "options": {
            1: "<b>Gate Cloak:</b> Hooded cloak inscribed with nano-particle algebraic equations that allows the user to phase-shift 10’ in any direction instead of taking damage. One use a day.",
            2: "<b>Mark IV Executioner:</b> (D8 blast, silencer) A combat shotgun created by a legendary weapons manufacturer - limited run. Replaces starting weapon.",
            3: "<b>Kinetic Katana:</b> (D8, bulky, thermal) An alien weapon you recovered. Slender black blade sheathed in a metal casing. Vibrates at subsonic levels producing an intense heat and orange glow. On a roll of maximum damage, the target must make a STR save or be fatally severed in half.",
            4: "<b>RNA-Attuned Shield Generator:</b> (+1 Armor, immune to bio damage) Gene-synthesized custom shield generator. Prevents illness. Take a few cigars too.",
            5: "<b>Dual-Oculus Hooded Mask:</b> A hooded faceplate mask with two circular smart-display goggles. Allows for perfect vision in darkness and other debris via A.I. aided image sequencing.",
            6: "<b>Cockatrice Claymores:</b> 3 remote-operated explosives that explode with a gray bio- synthetic dust. (blast 40’) Make a STR save or instantly be turned to stone.",
        },
    },
    {
        "name": "Spec-Ops Team",
        "options": {
            1: "<b>Infiltration:</b> Stealth unit. Once a day you automatically succeed when prompted to make a Save to move quietly, in shadows, balancing on precarious surfaces, or similar risky actions.",
            2: "<b>Heavy Marine:</b> Heavy unit, breach specialists. Increase STR to 13 if not currently at 13.",
            3: "<b>Flash Commando:</b> Light unit, worked in small teams. Re-roll damage rolls of 1.",
            4: "<b>Shock Trooper:</b> Special weapons drop troopers. Add shock damage to your starting weapon.",
            5: "<b>Counter-Insurgency:</b> If fighting in small, confined urban spaces, your first attack roll in combat is enhanced if your weapon is suited for close-range (melee, shotgun)",
            6: "<b>Top Secret Project:</b> You were part of an experimental top- secret project. Start with a bio- aug. Roll augment and re-flavor.",
        },
    },
    {
        "name": "Squad Job",
        "options": {
            1: "<b>Cook:</b> Once a day you can stretch out a single ration to feed the whole party if you spend 10-minutes preparing it with cooking tools.",
            2: "<b>Negotiator:</b> You can attempt to negotiate mid-combat. Make a WIL save, on a success enemy reaction is improved and the fighting temporarily halts.",
            3: "<b>Quartermaster:</b> Two extra inventory slots in your backpack.",
            4: "<b>Scout:</b> You and your group can never be ambushed if you are at full HP.",
            5: "<b>Demolitions:</b> Take 2 thermal detonators. If you set up an ambush with explosives the damage is enhanced.",
            6: "<b>Point Man:</b> You have an additional 2 HP when you’re at the front of the marching order.",
        },
    },
    # starting gear
    ["Tactical fatigues", "Shotgun or Rifle", "Dog tags"],
    # profile
    """You’re ex-special ops. Having completed or parting with your duties, new
opportunities are calling your name.""",
]


dossier_star_touched = [
    {
        "name": "What Gift Did the Stars Bring?",
        "options": {
            1: "<b>The Deplorable Word:</b> Anyone you speak the word to must make a WIL save or take 1d12 WIL damage. Use once a day. WIL save vs corruption.",
            2: "<b>Carried By the Wind:</b> Fly: Can fly once a day for 2d6 seconds at your normal movement.",
            3: "<b>Puzzle Tongue:</b> Comprehend Languages: Can speak to, understand, and be understood by all spoken languages of approximately human-level intelligence.",
            4: "<b>Warding Scriptures:</b> Your body is covered in a glowing script. Once a day when an attack is made against you for maximum damage, the damage is reverted back to the attacker.  Save vs corruption as the scriptures crawl further into you.",
            5: "<b>Sunder:</b> You can attack with your mind and two free hands for D6 damage from up to 60 ft. Does not cause fatigue.",
            6: "<b>Glittering Gate:</b> Spend 10 minutes performing a ritual in a 10’ circular area. Star-blessed spaces exist as a dyad, and only two can exist at once. Stepping into one space transfers those who enter to the other space. When a new space is created, the creator mentally chooses one of the existing two locations to dissipate. All who pass through this void space must save vs corruption.",
        },
    },
    {
        "name": "Your Vision",
        "options": {
            1: "<b>A Thousand Burning Suns:</b> Your eyes smolder. Fire does not harm you.",
            2: "<b>The Forever Deep:</b> You can breathe underwater and are never cold.",
            3: "<b>Abhorrent Geometry:</b> You are immune to mind-altering effects.",
            4: "<b>Belly of a Black Hole:</b> Your eyes are pitch black. You can see in the dark.",
            5: "<b>The Secret Truth:</b> You cannot understand or speak it. You can sense any untruth you hear.",
            6: "<b>Perfect Symmetry:</b> It was almost too beautiful to behold.  Social encounters are much easier for you. Reaction rolls in social situations are always one category higher than your result.",
        },
    },
    {
        "name": "What Was Taken?",
        "options": {
            1: "<b>Your Voice:</b> You can speak, but at a slow, strained crackle that sets others on edge.",
            2: "<b>Your Memories:</b> The past before you touched the infinite is insignificant, burned away to ash. You remember nothing from before.",
            3: "<b>Your Mind:</b> Whenever you gain fatigue, roll a d6. On a 1, you spend the next round clutching your head and babbling.  Addiction-inducing stims will calm you.",
            4: "<b>Your Superego:</b> Societal morality must be relearned, or perhaps simply left behind entirely.",
            5: "<b>Your Future:</b> Once a week you must make a save vs. corruption.  Slowly your future is rotting away.",
            6: "<b>Your Humanity:</b> Roll on the mutations table (pg. 89)",
        },
    },
    # starting gear
    ["Nothing can be truly possessed. You start with nothing but your clothing."],
    # profile
    """The living void and its myriad aspects reach out to you. You now belong to some
    greater purpose, or vaster intelligence, and have been gifted with a sliver of that
    power to wield as the envoy of forces you could no possibly comprehend.""",
]


dossier_bounty_hunter = [
    {
        "name": "Specialty Tool",
        "options": {
            1: "<b>Visage of Dread:</b> (+1 Armor, immune to mind-altering effects): Skull helmet (or something intimidating). At the start of combat, enemies save vs WIL or cower in fear for 1 round.",
            2: "<b>Heat-Seeking Sniper Rifle:</b> (D10) One mile range. 9-10 damage on the first shot of combat or from a hidden position is an instant kill.",
            3: "<b>Grave-Foam Gauntlet:</b> Sprays a liquid cloud of gray dust, forming a 12 inch thick casing around the target for 1d12 hours. Nothing inside can break out. The casing keeps its contents alive in a safe stasis until released. 1 cartridge of fuel (3 uses). Buy more fuel from Bounty Hunters’ Union.",
            4: "<b>Shock Dart:</b> (D6, spec ammo) Wrist mounted rocket dart. DEX save vs paralysis for 1d6 minutes.",
            5: "<b>Wire Shot:</b> (grappling) Wrist-mounted. Shoots a magnetic smart-wire that wraps around and ensnares targets. Dex save or completely grappled. No save if surprised.",
            6: "<b>Trick-Axe:</b> (D8, bulky, sweep): Can retract down to 3 feet in length for (D6).",
        },
    },
    {
        "name": "How Did You Hunt?",
        "options": {
            1: "<b>Like a True Hunter:</b> You hunted for trophies and glory, and by any means necessary. Take a notorious reputation and a war dog companion (d6 bite, 2 HP, 12 STR, 60’ speed)",
            2: "<b>From the Shadows:</b> If you get the jump on someone from hiding, your attacks are enhanced.",
            3: "<b>With a Personal Code:</b> Other hunters and those in the community respect you. You can request an audience with typically inaccessible underworld leaders.",
            4: "<b>Loaded With Tech:</b> Take 1d4 smart grenades (d6 blast, thermal, grappling) an auto-saw, and binocs.",
            5: "<b>By Any Means Necessary:</b> It was sometimes dirty, or unfair, but you got the job done. Any damage from traps, snares, or other preparations you make are enhanced.",
            6: "<b>Just for the Money:</b> It’s only a job, after all. Negotiate for double payouts on any bounty job. The NPC offering the job must pass a WIL save to resist, otherwise they’re persuaded to pay extra.",
        },
    },
    {
        "name": "A Past Complication",
        "options": {
            1: "<b>Revenge:</b> An old target escaped from prison and is after you. The hunter becomes the hunted…",
            2: "<b>Wanted:</b> You crossed the wrong syndicate. You’re now a wanted (alive) individual in 16 systems.",
            3: "<b>Radio Silence:</b> Your old primary fixer and contact went silent. You worry they may be compromised, or worse.",
            4: "<b>Old Dog:</b> Injuries, a hard life, and general wear and tear has taken its toll, and you’re not as spry as you once were. Sometimes that comes back to bite you.",
            5: "<b>Imposter:</b> After you left the scene, someone else recently appeared claiming to be you, and they’re ruining your hard-earned rep. Undealt with, it could have some unpleasant consequences.",
            6: "<b>One Last Job</b> An old client really needs your help on one last job.  Word is the pay is high...high enough for a lot of other hunters to also be on the hunt.",
        },
    },
    # starting gear
    [
        "Rifle or two blasters.",
        "Old Armor (Armor 1, Bulky)",
        "Manacles",
        "Bounty Hunting License & Union Membership.",
    ],
    # profile
    """It’s a slimy, treacherous world out there, and you had to be just as nasty to keep the
wolves from the door. You made your living as a licensed bounty hunter.""",
]

DOSSIERS = {
    "MERCENARY": dossier_mercenary,
    "HUMAN EXPERIMENT": dossier_human_experiment,
    "ENGINEER": dossier_engineer,
    "SMUGGLER": dossier_smuggler,
    "PILOT": dossier_pilot,
    "MACHINE": dossier_machine,
    "UNDERWORLD": dossier_underworld,
    "PSIONIC": dossier_psionic,
    "SCIENTIST": dossier_scientist,
    "SOLDIER": dossier_soldier,
    "STAR-TOUCHED": dossier_star_touched,
    "BOUNTY HUNTER": dossier_bounty_hunter,
}
