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
