from dataclasses import dataclass

elixir_sample_data = (
    (
        "1-3",
        "Babel Beer",
        "A sapient creature’s tongue",
        "1",
        "Allows drinker to fleetingly understand and speak the languages known by the tongue’s owner. However, they will do so in the slurring, incoherent manner of one intoxicated.",
    ),
    (
        "4-6",
        "Lumensoup",
        "The fur of a Lambent Lynx (p.xx)",
        "1",
        "Drinker’s flesh begins to glow. They can be used as a light source underground, but cannot hide. Lasts 8 Exploration Turns.",
    ),
    (
        "7-9",
        "Oblivion Brew",
        "A Memory Eater’s stomach (p.xx)",
        "1",
        "Drinker forgets the last hour of their life.",
    ),
    (
        "10-12",
        "Glassflesh Paste",
        "A Glass Tiger’s skin (p.xx)",
        "1",
        "Apply to flesh to become transparent for 4 Exploration Turns. You take minimum damage from beam weapons.",
    ),
    (
        "13-15",
        "Fellowship Potion",
        "A Psy-Owl’s brain (p.xx)",
        "1",
        "Drinker believes all nearby creatures to be their firm friends. This delusion lasts for a day, or until events force them to re-examine their belief.",
    ),
    (
        "16-18",
        "Greentongue Potion",
        "A Neobloom’s voxpod (p.xx)",
        "1",
        "Allows drinker to understand and speak the slow tongue of plants. Allow one Exploration Turn per question. This effect lasts for a day.",
    ),
    (
        "19-21",
        "False Death Draught",
        "An Amaranthine Death-Worm’s fangs (p.xx)",
        "1",
        "Drinker falls into a state of deathly paralysis. To all but most advanced bio-scanners, they appear dead. Lasts 6 exploration turns.",
    ),
    (
        "22-24",
        "Windsong Potion",
        "A Windweird’s larynx (p.xx)",
        "1",
        "Drinker can sing to quiet or raise the winds. They may change the local weather (p.xx) at will. Lasts 6 Exploration Turns.",
    ),
    (
        "25-27",
        "Doppeldraught",
        "The flesh of a Dopplegeller (p.xx)",
        "2",
        "Drinker vomits up a jelly-clone of themselves. It resembles them but is translucent and mute. It will follow instructions, but dissolves after 4 Exploration Turns..",
    ),
    (
        "28-30",
        "Spineskin Syrup",
        "The quills of a Quill-Spider (p.xx)",
        "2",
        "Drinker explosively grows quills, gaining +2 AV and destroying their current clothing. Missed melee attacks against them deal d4 damage. The quills shed after 4 Exploration Turns.",
    ),
    (
        "31-33",
        "Hilarious Strength",
        "The tooth of a Harlequin Serpent (p.xx)",
        "2",
        "Drinker gains +5 STR and loses -5 EGO. They cannot stop laughing, giving DIS on Encounter rolls. Lasts 4 Exploration Turns.",
    ),
    (
        "34-36",
        "Squishflesh Balm",
        "A Squishwolf’s skin (p.xx)",
        "2",
        "Drinker becomes jellylike and flexible. DIS on physical Saves, but can fit through narrow gaps and immune to crushing or fall damage. Lasts 4 Exploration Turns.",
    ),
    (
        "37-39",
        "Metallovore Potion",
        "A Yurling’s stomach (p.xx)",
        "2",
        "Drinker can eat and digest metal, which counts as a food ration. Effect lasts 6 Exploration Turns.",
    ),
    (
        "40-42",
        "Plating Potion",
        "A Plated Beetle’s carapace (p.xx)",
        "2",
        "Drinker gains +5 AV for 6 Exploration Turns. ",
    ),
    (
        "43-45",
        "Glittercough Tonic",
        "Unicorn meat (p.xx)",
        "2",
        "Drinker can excrete a cloud of glitter, forcing all targets to DEX Save vs Blindness for 4 rounds.",
    ),
    (
        "44-46",
        "Growth Serum",
        "A Pseudo-Giant’s pituatary gland (p.xx)",
        "2",
        "Drinker grows to double their current size, doubling their HP, STR, and CON. Lasts 4 Exploration Turns.",
    ),
    (
        "47-50",
        "Magnetic Stew",
        "A Magneticrab’s shell (p.xx)",
        "3",
        "Drinker becomes powerfully magnetic, and can irresistbly draw metal objects towards themselves. Lasts 4 Exploration Turns.",
    ),
    (
        "51-53",
        "Death Draught",
        "An Amaranthine Death-Worm’s fangs (p.xx)",
        "3",
        "Drinker is immediately reduced to 0 HP.",
    ),
    (
        "54-56",
        "Pupeteer Potion",
        "A Nerve-Crawler’s core (p.xx)",
        "3",
        "Drinker extrudes parasitic neural tissue which bonds them to another living creature. Target must EGO Save or become their puppet. Effect lasts",
    ),
    (
        "57-59",
        "Fakeface Paste",
        "The face of a Face Dancer (p.xx)",
        "3",
        "Apply to one’s own face to attain the art of Face Dancing. Your face can take on the form of any you have observed. The face remains convincing for one day.",
    ),
    (
        "60-61",
        "Skulk Salve",
        "The synth-skin of a Subtle Stalker (p.xx)",
        "3",
        "Apply to flesh or objects to make them invisible to all spectrums of light for the next 4 Exploration Turns.",
    ),
    (
        "62-63",
        "Berserker Brew",
        "A Cacklemaw’s liver (p.xx)",
        "3",
        "Drinker enters a state of battle frenzy.They deal and receive double damage and must always attack the closest living being. They must EGO Save to exit this frenzy.",
    ),
    (
        "64-65",
        "Phasing Potion",
        "A Phase Panther’s heart (p.xx)",
        "3",
        "Drinker phases out of reality, becoming incorporeal and invincible. Lasts 4 Exploration Turns.",
    ),
    (
        "66-67",
        "Lithification Syrup",
        "A Lithling’s crystalline flesh (p.xx)",
        "3",
        "Drinker’s flesh turns to living crystal. They gain +5 AV and the Mineral creature type, including all damage immunities (see p.xx). The effect lasts 6 Exploration Turns.",
    ),
    (
        "68-69",
        "Geneshock Tonic",
        "The heart of a Cacogen (p.xx)",
        "4",
        "Drinker gains a new, permanent mutation, matching that of the heart’s original owner.",
    ),
    (
        "70-71",
        "Regeneration Serum",
        "The flesh of a Regenerator (p.xx)",
        "4",
        "Drinker regains d6 HP per combat round, unless damaged by fire or acid. The effect lasts for 6 Exploration Turns.",
    ),
    (
        "72-73",
        "Obsession Philtre",
        "The fang of a Gorgon (p.xx)",
        "4",
        "Drinker falls madly in love with the next character they see. The effect lasts as long as they stay within sight of their love object.",
    ),
    (
        "74-75",
        "Broodling Broth",
        "The egg-sac of a Brood Mother (p.xx)",
        "4",
        "Drinker’s stomach distends grotesquely. They birth d6 Broodlings [Lvl 0 (1 hp), AV 12, Bite (d4)]. The Broodlings are somewhat like spiders and somewhat like their host. They are loyal to their ‘mother’ and follow them until killed.",
    ),
    (
        "76-77",
        "Biothermal Amplifier Tonic",
        "The chemglands of a Thermasaur (p.xx)",
        "4",
        "Drinker gains two Mystic Gifts: Pyrokinesis and Cyrokinesis. They are immune to damage caused by extreme heat or cold. These effects last for one day.",
    ),
    (
        "78-79",
        "Lazarus Tonic",
        "The black heart of a Lazarus Guard (p.xx)",
        "4",
        "A dead biological creature may be restored to life with this thick black tonic, at the cost of one Level.",
    ),
    (
        "80-81",
        "Kalotoxin Injector",
        "The stinger of a Kalopede (p.xx)",
        "4",
        "Target is transformed into a work of Fine Art (p.xx), with no Save possible.",
    ),
    (
        "82-83",
        "Bifurcating Brew",
        "The head of a Jollyhoss (p.xx)",
        "4",
        "Drinker splits into two hypergeometric halves, which each have half the character’s max HP. They can move and act independently. If one half dies, it will ressurect with full HP while the other half lives. Lasts 4 Exploration Turns.",
    ),
    (
        "84-85",
        "Hollowheart Hooch",
        "The heart of a Hollow Bride (p.xx)",
        "5",
        "Drinker permanently gains 2 new hypergeometric Item Slots, located inside their chest. This effect can increase slot capacity beyond the 20 slot maximum.",
    ),
    (
        "86-87",
        "Autarch’s Ambrosia",
        "The preserved heart of an Autarch (p.xx)",
        "5",
        "Drinker permanently gains +1 to the Ability of their choice.",
    ),
    (
        "88-89",
        "Metamorphic Syrup",
        "The slurry of a Metamorphic Sludge (p.xx)",
        "5",
        "Drinker is permanently changed into a new, random creature. Generate their bodytype using the monster generators on p.xx.",
    ),
    (
        "90-91",
        "Cloning Jelly",
        "The flesh of an Echopraxist (p.xx)",
        "5",
        "Anything smeared with the gel is replicated perfectly, down to the smallest detail. The clone is a new permanent entity, and is not under the control of the original.",
    ),
    (
        "92-93",
        "Transcendence Tonic",
        "The brain of a Mystic (p.xx)",
        "5",
        "Drinker gains a new, permanent Mystic Gift, matching that of the brain’s original owner.",
    ),
    (
        "94-95",
        "Recursive Infusion",
        "The eye of a Fractalisk (p.xx)",
        "5",
        "Drinker gains a new Mystic Gift: Recursive Gaze. A single target fixed with the Recursive Gaze must repeat their action they just took, with no save allowed. This effect is broken if the PC’s gaze is interrupted.",
    ),
    (
        "96-98",
        "Planeyfication Potion",
        "The heart of a Planeyperson (p.xx)",
        "5",
        "Drinker permanently becomes a hypergeometric entity. They gain the Hypergeometric creature type and follow the special rules given for the Planeyfolk Ancestry (p.xx)",
    ),
    (
        "99-100",
        "Immortality Injector",
        "The mercurial war- flesh of a Quicksilver Exterminator (p.xx)",
        "5",
        "A creature injected with this fizzing froth of nanomachinery cannot die. It can be damaged beyond recognition, but the life will not leave its frame.This effect lasts for one day.",
    ),
)


@dataclass
class Elixir:
    dice_roll: str
    name: str
    component: str
    potency: int
    effect: str


def gen_elixirs(max_potency=3):
    elixirs = [Elixir(*line) for line in elixir_sample_data]
    # pass through potencies as strings and turn them to ints
    for el in elixirs:
        el.potency = int(el.potency)
    if max_potency >= 5:
        return elixirs
    return [el for el in elixirs if el.potency <= max_potency]
