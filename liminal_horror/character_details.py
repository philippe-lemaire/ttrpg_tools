from dataclasses import dataclass
from random import choice


@dataclass
class CharacterDetails:
    style: str
    the_abyss_stare_back: str
    ideology_and_beliefs: str
    physical_trait: str
    mental_trait: str


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
physical_traits = (
    "Athletic ",
    "Bony ",
    "Blunt",
    "Muscular ",
    "Broken ",
    "Gravelly",
    "Curvy ",
    "Chiseled ",
    "Booming",
    "Lanky ",
    "Elongated ",
    "Precise",
    "Small ",
    "Dimpled ",
    "Cryptic",
    "Rigid ",
    "Perfect ",
    "Squeaky",
    "Stout ",
    "Round ",
    "Formal",
    "Towering ",
    "Sharp ",
    "Accented",
    "Robust ",
    "Memorable ",
    "Droning",
    "Ample Body ",
    "Forgettable ",
    "Choppy",
)

mental_traits = (
    "Honest ",
    "Quick to anger ",
    "Abandoned",
    "Honorable ",
    "Lazy ",
    "Defrauded",
    "Cautious ",
    "Pessimistic ",
    "Addicted",
    "Humble ",
    "Nervous ",
    "Demoted",
    "Courageous ",
    "Craven ",
    "Blackmailed",
    "Merciful ",
    "Rude ",
    "Discredited",
    "Disciplined ",
    "Deceitful ",
    "Condemned",
    "Serene ",
    "Vain ",
    "Disowned",
    "Gregarious ",
    "Greedy ",
    "Cursed",
    "Tolerant ",
    "Vengeful ",
    "Exiled",
)


def gen_character_details():
    style = choice(styles)
    abyss = choice(abyss_answers)
    ideology = choice(ideologies)
    physical = choice(physical_traits)
    mental = choice(mental_traits)
    return CharacterDetails(style, abyss, ideology, physical, mental)
