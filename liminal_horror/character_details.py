from dataclasses import dataclass
from random import choice


@dataclass
class CharacterDetails:
    style: str
    the_abyss_stare_back: str
    ideology_and_beliefs: str
    physique: str
    face: str
    speech: str
    virtue: str
    flaw: str
    misfortune: str


styles = (
    "All Business, All the Time",
    "Streetwear",
    "Band Tees",
    "Paint it Black",
    "Athleisure",
    "Crisp and Ironed",
    "Casual Comfort",
    "Authentic Vintage",
    "All the Rage",
    "Work Uniform",
    "Oversized Hoodie",
    "Island Floral",
    "Everything Tailored",
    "Function Over Fashion",
    "Cargo Pockets",
    "Jeans and Tees",
    "Trapped in 2009",
    "Grunge Minimalist",
    "Y2K",
    "Denim on Denim",
)

abyss_answers = (
    "You lost a loved one under mysterious circumstances.",
    "The evidence online is too much to be ignored.",
    "You witnessed something in the darkness.",
    "You survived an attack you cannot explain.",
    "Something is lurking in your dreams.",
    "Someone close to you is pulling you in, or pushing you away.",
    "Cult activity (perhaps they recruited someone significant).",
    "You may be a card carrying member of a secret society.",
    "You read something not meant for mortal minds.",
    "You haven’t yet, that’s what session 1 is for!",
)

ideologies = (
    "Everything has a rational explanation rooted in science.",
    "Individuals can make a difference.",
    "You ascribe to a specific political ideology.",
    "A specific religion guides you.",
    "Morality is black and white.",
    "You believe in fate and it directly impacts your life.",
    "Belief in higher powers such as astrology, spirituality, etc.",
    "Free will is the only truth.",
    "There are deep truths that others are not aware of. The answers are out there.",
    "You believe in the power of community.",
)
physiques = (
    "Athletic",
    "Muscular",
    "Curvy",
    "Lanky",
    "Small",
    "Rigid",
    "Stout",
    "Towering",
    "Robust",
    "Ample Body",
)

faces = (
    "Boney",
    "Broken",
    "Chiseled",
    "Elongated",
    "Dimpled",
    "Perfect",
    "Round",
    "Sharp",
    "Memorable",
    "Forgettable",
)

speeches = (
    "Blunt",
    "Gravelly",
    "Booming",
    "Precise",
    "Cryptic",
    "Squeaky",
    "Formal",
    "Accented",
    "Droning",
    "Choppy",
)


virtues = (
    "Honest ",
    "Honorable ",
    "Cautious ",
    "Humble ",
    "Courageous ",
    "Merciful ",
    "Disciplined ",
    "Serene ",
    "Gregarious ",
    "Tolerant ",
)


flaws = (
    "Quick to anger ",
    "Lazy ",
    "Pessimistic ",
    "Nervous ",
    "Craven ",
    "Rude ",
    "Deceitful ",
    "Vain ",
    "Greedy ",
    "Vengeful ",
)

misfortunes = (
    "Abandoned",
    "Defrauded",
    "Addicted",
    "Demoted",
    "Blackmailed",
    "Discredited",
    "Condemned",
    "Disowned",
    "Cursed",
    "Exiled",
)


def gen_character_details():
    style = choice(styles)
    abyss = choice(abyss_answers)
    ideology = choice(ideologies)
    physique = choice(physiques)
    face = choice(faces)
    speech = choice(speeches)
    virtue = choice(virtues)
    flaw = choice(flaws)
    misfortune = choice(misfortunes)
    return CharacterDetails(
        style, abyss, ideology, physique, face, speech, virtue, flaw, misfortune
    )
