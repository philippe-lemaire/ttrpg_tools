from random import choice
from dataclasses import dataclass

codex_appearances = (
    "A goblet so black it drinks in light, the inner rim of which is inlaid with spiralling equations.",
    "The dried skin of a toad, tattooed with hypergeometric proofs.",
    "A book cast from iron, the pages of which must be turned with a mechanical crank.",
    "A tablet carved from pale lunar stone, which feels as light as a feather.",
    "A tall hat scaled with coins, the inverse sides of which are carved with hypergeometric sigils.",
    "A lump of pink crystal, veined with hypergeometric glyphs when one holds it up to the light.",
    "The foot-long fang of a gigantic Ur-Snake, carved with frantic equations.",
    "A broken mirror, which displays the equation as though written upon the observer’s reflected face.",
    "A lump of amber; the contorted shapes of insects trapped within spell out the equation’s proofs.",
    "A ring set with polychrome gemstones; the equation is printed on the inner curve, hiding it while worn.",
    "A child’s drawing tablet, the equation scribbled in chalk amongst naive doodles.",
    "An ancient set of binoculars; when raised to the eyes all one can see is the hypergeometric proof, written across the sky in mile-high letters of divine fire.",
    "A black book the size of a thumbnail yet heavy as sin; the pages must be turned with tweezers.",
    "A human heart, blue with putrescence yet still beating; the equation is written upon the muscle with luminous ink.",
    "A chrome skull, its brain cavity filled with scraps of burned paper on which the equation is repeated endlessly.",
    "A broken sword, the blade molten and warped into the shape of hypergeometric proofs.",
    "An ordinary looking wine-jar, sealed with a stopper made from black wax. Remove the stopper and a voice whispers from within the jar, endlessly repeating the equation.",
    "A dining plate, painted with innumerable dancing blue and red figures; stare at the plate with an empty mind and an equation begins to emerge from the whirl of colour.",
    "An ornate lady’s fan, on which the equation is painted in the flowery court script of the Fallen Autarchy.",
    "An infinite möbius strip made from ancient parchment; the equation is written along the paradoxical coiling faces",
)

equations_data = (
    (
        "Antithetical Copy",
        "Creates a daemonic, insanely evil copy of a target entity. The copy is alive and violently opposed to the existence of the original -if it makes physical contact with the original, both entities are explosively destroyed. The antithesis crumbles to ash after [INT] hours.",
    ),
    (
        "Diminish",
        "The reader or another targeted entity shrinks to half of their original size and mass. This effect lasts [INT] hours.",
    ),
    (
        "Erase Paradox",
        "Targeted Hypergeometric or Outsider-type entity must EGO save vs 10 + [INT]. On failure the entity accepts the fundamental implausibility of their presence and ceases to exist.",
    ),
    (
        "Exchange Coordinates",
        "The reader swaps physical positions with a targeted entity.",
    ),
    (
        "Expand",
        "The reader or another targeted entity grows to double their original size and mass. This effect lasts [INT] hours.",
    ),
    (
        "Flatten",
        "The reader or another targeted entity is transformed into a 2D hypergeometric entity. This effect lasts [INT] hours.",
    ),
    (
        "Golem",
        "Imbues a nearby inanimate object with mobility and sentience. It obediently serves you for [INT] hours.",
    ),
    (
        "Imperfect Copy",
        "Creates [INT] copies of a target entity. They are colourless and lifeless, resembling sculptures made from ash.",
    ),
    (
        "Increase Gravity",
        "Target entity feels the effects of gravity at ten times the usual force. They are unable to move or fight. This lasts [INT] combat rounds.",
    ),
    (
        "Invert Gravity",
        "Target entity has its gravitational polarity reversed for [INT] combat rounds, falling towards the sky. When the effect ends, they take d8 falling damage for each round they fell skywards.",
    ),
    (
        "Kinetic Ward",
        "Creates an invisible wall of hypergeometric force that negates all physical attacks. The barrier can protect one entity for [INT] combat rounds, or [INT] entities for one combat round.",
    ),
    (
        "Perfect Copy",
        "Creates a perfect copy of a target entity. The copy resembles the original in all respects. It crumbles to ash after [INT] hours.",
    ),
    (
        "Phase",
        "The reader or another targeted entity is placed out of sync with the material realm. They are visible but cannot touch anything (except other phased entities). This effect lasts [INT] combat rounds.",
    ),
    (
        "Portal",
        "The reader creates a pair of portals, linking two flat surfaces that they can see. The portals persist for [INT] combat rounds.",
    ),
    (
        "Return Fixed Coordinates",
        "The reader and/or [INT] other entities are transported to a predetermined point in space. The codex only connects to this pre-written point in space.",
    ),
    (
        "Return Random Coordinates",
        "The reader and/or [INT] other entities are transported to a random point in space which the reader has previously occupied.",
    ),
    (
        "Singularity",
        "Creates a miniature black hole for [INT] combat rounds, which draws in all unsecured entities in the room. Anything engulfed by the singularity is destroyed. Living beings must STR save vs 10 + [INT] to avoid being drawn into the black hole.",
    ),
    (
        "Stasis",
        "A single entity is stranded outside the flow of time for [INT] combat rounds. They cannot be moved, harmed, or interacted with in any way.",
    ),
    (
        "Summon",
        "The reader plucks a creature from the manifold halls of creation. Roll on the Monster Generator tables (p.xx) to determine the nature and disposition of the entity.",
    ),
    (
        "Vanish",
        "The reader or another targeted entity is no longer visible in the normal spectrum of light. Infrared vision will still detect the hidden entity. This effect lasts [INT] hours.",
    ),
)

mishaps_data = (
    (
        "Antithesis",
        "Births a daemonic, insanely evil copy of the reader, with their Level and HP. The copy is violently opposed to the existence of the reader - if it makes physical contact with the reader, both entities are explosively destroyed. The antithetical copy exists for [INT] combat rounds.",
    ),
    (
        "Brainstorm",
        "The reader’s muddled thoughts are actualised as polychrome lightning, which pours from their eyes and mouth. Everyone nearby takes 2d6 electrical damage, DEX save for half damage.",
    ),
    (
        "Chroma-shadow",
        "The reader’s shadow permanently shifts in hue, becoming pinkish-orange.",
    ),
    (
        "Codex Collapse",
        "The hypergeometric codex collapses in on itself, vanishing from existence",
    ),
    (
        "Entropy-withered",
        "The reader’s body twists and decays under the effect of entropic hypergeometric forces. They lose d6 maximum HP and cannot regain it.",
    ),
    (
        "Giant Item",
        "An item in the reader’s inventory is subjected to hypergeometric forces, becoming enormous. The item’s weight in slots triples. Roll d10 to determine the slot affected. The change is permanent.",
    ),
    (
        "Gigantism",
        "The reader’s body grows uncontrollably in size, swelling to fill the room they are inside. All other occupants must evacuate or be crushed. If this happens outdoors, they continue to grow for the entire duration of this mishap. The growth lasts [INT] hours, followed by a steady deflation.",
    ),
    (
        "Inverted Anatomy",
        "A hypergeometric flux places the reader’s internal organs on the outside of their body and their clothing inside. Their AV score is now 10, and they take doubled damage from all sources. This effect lasts [INT] days.",
    ),
    (
        "Inverted Fate",
        "The reader’s destiny is inverted. All failed Saves and attack rolls are successes and all successful Saves and attack rolls are failures. This effect lasts [INT] days.",
    ),
    (
        "Labyrinth Pox",
        "The reader contracts Labyrinth Pox, a hypergeometric ailment (p.xx).",
    ),
    (
        "Lost Past",
        "The reader permanently loses a chunk of their history. The PC loses a single Level, and must subtract d8 HP from their maximum. They must reduce their Ability scores by three points.",
    ),
    (
        "Petrified",
        "The reader’s body freezes under the weight of crushing hypergeometric force. The reader is unable to move or act for [INT] hours.",
    ),
    (
        "Planeyfied",
        "The reader becomes a 2D hypergeometric being. Refer to the Planeyfolk ancestry (p.xx) for special rules. This effect lasts [INT] days.",
    ),
    (
        "Quantum Daemon",
        "A paradoxical quantum daemon (p.xx) is called into existence. It is displeased about this and wishes the reader ill.",
    ),
    (
        "Revelation",
        "The reader witnesses a terrible vista in a higher-order dimension, taking d6 damage to INT, PSY, and EGO.",
    ),
    (
        "Shrunken Head",
        "The reader’s head is subjected to hypergeometric forces, becoming minute. Their body retains its size. The PC gains a Wound: Shrunken Head. They lose d6 INT, PSY and EGO and cannot wear helmets or hats.",
    ),
    (
        "Space-Time Vortex",
        "A mispronunciation creates a rupture in the fabric of space and time. The vortex begins vomiting forth inanimate debris and living creatures. Roll once on the local encounter table each combat round: the creature is ejected from the vortex at high velocity, along with rubble or other inanimate debris (DEX save to avoid).",
    ),
    (
        "Spirit Hand",
        "The reader’s left hand is permanently drawn into a hypergeometric dimension adjacent to our own. Their left arm ends in a strange blue fissure and the missing hand feels as though it is immersed in cold television static. Take d10 DEX damage. Unarmed attacks with the missing hand take on the hypergeometric damage property.",
    ),
    (
        "The Yellow Door",
        "The reader develops a yellow hypergeometric door in their forehead. The door is locked and cannot be opened. The effect is permanent.",
    ),
    (
        "Tiny Item",
        "An item in the reader’s inventory is subjected to hypergeometric forces, becoming tiny and totally useless. The item’s weight in slots is reduced to nothing. Roll d10 to determine the slot affected. The change is permanent.",
    ),
)


@dataclass
class HyperGeometryMishap:
    name: str
    effect: str


def gen_hypergeometry_mishap():
    return HyperGeometryMishap(*choice(mishaps_data))


@dataclass
class Equation:
    name: str
    effect: str

    def __repr__(self):
        return f"<b>{self.name}</b>. {self.effect}"


@dataclass
class HyperGeometryCodex:
    appearance: str
    equation: Equation

    def __repr__(self):
        return f"<b>Hypergeometry Codex</b>.<br>Appearance: {self.appearance} <br>Equation: {self.equation}"


def gen_codex():
    appearance = choice(codex_appearances)
    name, effect = choice(equations_data)
    return HyperGeometryCodex(appearance, Equation(name, effect))
