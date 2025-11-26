from random import sample
from dataclasses import dataclass

mutation_data = (
    (
        "Acid Blood",
        "Your blood is caustic. Creatures that attack you in melee suffer d4 acid damage when they damage you.",
    ),
    (
        "Adhesive Touch",
        "Your hands and feet are like those of a gecko. You can climb any surface and crawl across ceilings.",
    ),
    (
        "Albino",
        "Your body has no pigmentation. You must carry a sunshade (1 slot) or suffer DIS on all Saves during daylight hours.",
    ),
    (
        "Antlers",
        "You have antlers like an elk or moose. Make an extra +d6 melee attack when you charge.",
    ),
    (
        "Analgesia",
        "You are unable to feel pain. You do not know your maximum or current HP; the Referee tracks both.",
    ),
    (
        "Armoured Skin",
        "Your body is protected by natural armour. Add +2 to your base AV.",
    ),
    (
        "Backwards Head",
        "Your head can swivel backwards like an owl’s. You cannot be ambushed.",
    ),
    (
        "Backwards Legs",
        "Your legs are backwards. DIS when fleeing and sneaking.",
    ),
    (
        "Beak",
        "Make an extra d6 melee attack. ADV on reaction rolls when encountering bird-like creatures.",
    ),
    (
        "Bioelectricity",
        "Your unarmed melee attack causes +d6 electrical damage.",
    ),
    (
        "Bioluminescence",
        "Your flesh produces a faint glow. You always have a light source. DIS to hide at night.",
    ),
    (
        "Blind",
        "You cannot see and must navigate by sound and scent. DIS on ranged attacks, ADV when fighting in the dark. Cancels effects of other visual mutations.",
    ),
    (
        "Body Barbs",
        "Your flesh is studded with sharp barbs. Opponents who miss melee attacks against you suffer damage equal to your Level.",
    ),
    (
        "Bulbous Eyes",
        "Your eyes are enormous. DIS on Saves to avoid blindness.",
    ),
    (
        "Centaur",
        "You have the lower body and legs of a horse. +2 CON, +4 max items slots (24 total).",
    ),
    (
        "Chameleon Skin",
        "Your skin always matches its surroundings. ADV to conceal yourself.",
    ),
    (
        "Claws, Crab",
        "One hand is a huge crab-like claw. Your unarmed attack deals d8 damage. You cannot use two-handed weapons.",
    ),
    (
        "Claws, Retractable",
        "You have retractable feline claws. Your unarmed attack deals d6 damage.",
    ),
    (
        "Clubfoot",
        "One foot is larger and heavier than the other. DIS when fleeing and sneaking.",
    ),
    (
        "Compound Eyes",
        "Your eyes are like those of a fly. +1 DEX.",
    ),
    (
        "Crest, Bone",
        "You have a large bony crest on your head. +1 AV. Cannot wear helmets.",
    ),
    (
        "Crest, Feathers",
        "You have a crest of feathers on your head. +1 EGO. Cannot wear helmets.",
    ),
    (
        "Crown, Horns",
        "You have a crown of horns on your head. +1 AV. Cannot wear helmets.",
    ),
    (
        "Crown, Coral",
        "You have a coral-like crown on your head. +1 AV. Cannot wear helmets.",
    ),
    (
        "Crown, Eyestalks",
        "You have a crown of eyestalks on your head. +1 PSY. Cannot wear helmets.",
    ),
    (
        "Cyclops Eye",
        "You have a single huge eye. You have poor depth perception. DIS on Saves vs blindness.",
    ),
    (
        "Detachable Head",
        "Your head can detach from your body and move of its own accord for as long as you can hold your breath.",
    ),
    (
        "Detachable Limb",
        "A single limb can detach from your body and move of its own accord. If separated from your body it cannot ‘see’ and must proceed by touch alone.",
    ),
    (
        "Double Muscled",
        "Your limbs have an extra pair of muscles. +2 STR, ADV when fleeing or pursuing.",
    ),
    (
        "Echolocation",
        "You can ‘see’ in pitch darkness using echoes. You cannot be blinded and have ADV when fighting in the dark.",
    ),
    (
        "Exposed Organs",
        "You suffer double damage from slashing or piercing attacks.",
    ),
    (
        "Extra Arms",
        "You have an extra pair of arms. You can make an extra melee or ranged attack each turn, if equipped with a second weapon.",
    ),
    (
        "Extra Eyes",
        "You have d3 extra eyes on your forehead. +1 PSY for each.",
    ),
    (
        "Extra Head",
        "You have an extra head. ADV on INT, PSY and EGO Saves. You can survive one decapitation.",
    ),
    (
        "Extra Heart",
        "+2 CON, +5 max HP.",
    ),
    (
        "Extra Legs",
        "You have a pair of extra legs. +2 CON, ADV on Saves relating to pursuits.",
    ),
    (
        "Extra Liver",
        "ADV on Saves vs poisons and TOX attacks.",
    ),
    (
        "Eyestalks",
        "Your eyes extend out of their sockets on stalks.",
    ),
    (
        "Fangs, Venomous",
        "You have a poisonous bite (d6 TOX).",
    ),
    (
        "Feathers",
        "You have feathers instead of hair. ADV to reaction roll when encountering feathered creatures.",
    ),
    (
        "Frog Tongue",
        "Your tongue is extremely long and sticky. DEX save to snatch weapons from foe’s hands.",
    ),
    (
        "Fur",
        "You are covered in fur. ADV to reaction roll when encountering furry creatures.",
    ),
    (
        "Gills",
        "You have gills and can breathe underwater. You must drink double rations of water each day or become Deprived.",
    ),
    (
        "Gliding Membranes",
        "You have membranes between your arms and torso and can glide for short distances.",
    ),
    (
        "Goat Legs",
        "You have the legs and hooves of a goat. You can walk up sheer surfaces.",
    ),
    (
        "Headless",
        "You have no head; your face is on your torso. You cannot wear helmets or hats.",
    ),
    (
        "Heightened Hearing",
        "You have extremely sharp hearing. You suffer no ill-effects from blindness or darkness and cannot be ambushed.",
    ),
    (
        "Heightened Immune System",
        "Your immune system is the envy of all. ADV on Saves vs diseases and poisons.",
    ),
    (
        "Hook, Climbing",
        "You have hook-like protrusions on your limbs. ADV to climbing and acrobatics.",
    ),
    (
        "Hopper",
        "You have a single, powerful leg. You can leap huge distances.",
    ),
    (
        "Horns, Ram",
        "You have ram-like horns. You can make an extra d6 melee attack. ADV on reaction rolls when encountering other horned creatures.",
    ),
    (
        "Horns, Rhino",
        "You have a single rhino-like horn. When you charge into melee range, add +d10 to your damage roll.",
    ),
    (
        "Huge Beard",
        "You have a gigantic, fast-growing beard that resists all attempts to tame it.",
    ),
    (
        "Huge Brain",
        "Your head is enormous. +2 to INT. You cannot wear helmets or hats.",
    ),
    (
        "Humpback",
        "You have a hump like that of a camel, which stores water. You can go seven days without drinking water.",
    ),
    (
        "Infravision",
        "You can detect heat signatures and can see warm-blooded creatures in total darkness.",
    ),
    (
        "Ink Ducts",
        "You can spray out ink like a squid, causing an opponent to DEX save vs blindness. You can do this a number of times per day equal to your Level.",
    ),
    (
        "Insulated Skin",
        "Your skin is resistant to heat and cold. Take half damage from extreme temperatures.",
    ),
    (
        "Kangaroo Pouch",
        "You have a torso-pouch like a kangaroo’s. +2 max item slots (22 max).",
    ),
    (
        "Larynx Darts",
        "You can cough bony barbs from a discreet orifice in your neck. Treat as a concealed d4 ranged weapon that cannot run out of ammunition.",
    ),
    (
        "Leaves",
        "You have leaves instead of hair. Regain d4 HP per hour when resting in sunlight.",
    ),
    (
        "Malleable Body",
        "Your body is rubbery and malleable; you can fit into tight gaps. Take half damage from bludgeoning attacks.",
    ),
    (
        "Malleable Face",
        "Your face is malleable; you can imitate the faces of others given time.",
    ),
    (
        "Mane, Hair",
        "You have a lion-like mane of hair around your neck. +1 EGO.",
    ),
    (
        "No Ears",
        "You have no external ears; just holes.",
    ),
    (
        "Obligate Carnivore",
        "You must eat raw meat each day or become Deprived.",
    ),
    (
        "Patterned Skin",
        "Your skin is striped or spotted. +1 EGO.",
    ),
    (
        "Pleasant Fragrance",
        "Your scent is pleasing to all. +1 EGO.",
    ),
    (
        "Poison Spur",
        "You have a poison spur on your wrist. Your unarmed attack deals d6 TOX damage.",
    ),
    (
        "Powerful Jaws",
        "You can bite through metal. Add +d6 to melee attack damage.",
    ),
    (
        "Prehensile Feet",
        "Your feet can grip objects like hands. +1 DEX.",
    ),
    (
        "Prehensile Hair",
        "Your hair can grip objects like a hand. +1 DEX.",
    ),
    (
        "Quills",
        "You have quills coating your body. Add +2 to your AV. Opponents who miss melee attacks against you suffer damage equal to your Level. You cannot wear other armour.",
    ),
    (
        "Scaly Skin",
        "Your skin is thick and scaly. Add +1 to your AV.",
    ),
    (
        "Silk Production",
        "You can produce strands of sticky web. Make an opposed DEX save to wrap an enemy in web, paralysing them until they succeed at a DEX save.",
    ),
    (
        "Skeletal Frame",
        "Your body is incredibly light. -2 STR and -2 CON. You take double damage from bludgeoning and crushing attacks.",
    ),
    (
        "Slimy Skin",
        "You are coated in slime. ADV to escape grab attacks and enclosing traps.",
    ),
    (
        "Slug Body",
        "You have a single slimy tail-foot and leave a trail of mucus. -2 DEX, can stick to sheer surfaces.",
    ),
    (
        "Small Stature",
        "Your body is child-sized and will never grow larger. DIS on all STR saves.",
    ),
    (
        "Snout",
        "You have a snout-like, animalistic face. ADV to reaction rolls with Newbeasts.",
    ),
    (
        "Stilt Legs",
        "You have long stilt-like legs. ADV in chases and pursuits, can wade quickly through flooded areas. You are the default target for ranged attacks.",
    ),
    (
        "Strange-Hued Eyes",
        "Your eyes are an unnatural colour.",
    ),
    (
        "Strange-Hued Hair",
        "Your hair is an unnatural colour.",
    ),
    (
        "Strange-Hued Skin",
        "Your skin is an unnatural colour.",
    ),
    (
        "Tail, Club",
        "You have a club-like, heavy tail. Make an extra d8 crushing melee attack per round.",
    ),
    (
        "Tail, Prehensile",
        "You have a long, thin tail that can grip objects. +2 DEX.",
    ),
    (
        "Tail, Scorpion",
        "You have a segmented stinging tail like a scorpion’s. Make one extra attack per round (d6 TOX).",
    ),
    (
        "Tentacles, Arms",
        "You have tentacles instead of arms. -3 STR, +3 DEX.",
    ),
    (
        "Tentacles, Hair",
        "You have stinging tentacles instead of hair. At melee range you can make a d6 TOX attack instead of your normal attack.",
    ),
    (
        "Toxic Flesh",
        "Your flesh is toxic when eaten (d10 TOX).",
    ),
    (
        "Transparent Skin",
        "Your skin is transparent and your muscles and veins can be seen. Take double damage from Beam attacks.",
    ),
    (
        "Trunk",
        "You have an elephant-like trunk, which can hold and manipulate objects. +1 DEX.",
    ),
    (
        "Tusks",
        "You have tusks like a boar. +D6 melee damage.",
    ),
    (
        "Ultravision",
        "You have eyes that see beyond the normal spectrum of light. You can see otherwise invisible creatures and objects. You cannot be blinded.",
    ),
    (
        "Vestigial Wings",
        "You have vestigial, unusable wings.",
    ),
    (
        "Vocal Mimic",
        "You can perfectly mimic voices or sounds you have heard.",
    ),
    (
        "Warty Skin",
        "Your skin is thick and warty. Add +1 to your AV.",
    ),
    (
        "Webbed Digits",
        "Your hands and feet are webbed like a frog’s.",
    ),
    (
        "Whiskers",
        "You have sensitive whiskers like a cat. +1 PSY.",
    ),
    (
        "Wings",
        "You have wings that allowed you to fly freely. When airborne you are the default target for ranged attacks.",
    ),
)


@dataclass
class Mutation:
    name: str
    description: str


def get_mutations(k):
    mutations = sample(mutation_data, k)
    return [Mutation(name, description) for name, description in mutations]


def get_mutations_list():
    return [Mutation(*data) for data in mutation_data]
