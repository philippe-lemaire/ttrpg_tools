from random import choice, randint
from dataclasses import dataclass


sizes = (
    "Hamlet",
    "Boomtown (Doubles in size each month for d6 months.)",
    "Village",
    "Large Town",
    "City State (Smaller settlements nearby pay tribute)",
)

water_sources = (
    "Oasis (p.xx)",
    "Atmospheric Condensation Machines",
    "Deep Wells",
    "Underground Aqueduct",
    "Secret Reservoir",
    "Water Recycling Machines",
    "Flows From Hypergeometric Gateway",
    "Holy Relic Weeps Water",
)


water_complications = (
    "Poisonous algae or spilled chemicals",
    "Slow, require repairs; spare parts rare",
    "Slow and arduous to gather water",
    "Blockage or diversion",
    "Beginning to run dry",
    "Require repairs; spare parts rare",
    "Gateway capricious; sometimes closes up",
    "Target of relic thieves",
)


majority_populations = {
    2: "Lithlings",
    3: "Cacklemaw Exiles",
    4: "True-Kin",
    5: "Synths",
    6: "Newbeasts",
    7: "Cacogen",
    8: "Faa Nomads",
    9: "Mycomorphs",
    10: "Neoblooms",
    11: "Planeyfolk",
    12: "Extradimensional Outsiders",
}

minority_populations = {
    2: "Sentient Tame Monsters",
    3: "Planeyfolk",
    4: "Neoblooms",
    5: "Mycomorphs",
    6: "Faa Nomads",
    7: "Cacogen",
    8: "Newbeasts",
    9: "Synths",
    10: "True-Kin",
    11: "Cacklemaw Exiles",
    12: "Lithlings",
}

locations_houses_landmarks = (
    (
        "Base of Huge Statue",
        "Hide Yurts",
        "Ancient Forge",
    ),
    (
        "Amongst Broken War Machines",
        "Clay Brick Huts",
        "Enormous Skull",
    ),
    (
        "Dried-up Lake Bed",
        "Sunken Warren",
        "Arcology Dome (p.xx)",
    ),
    (
        "On Salt Plains",
        "Made from Trash",
        "Slender Silver Tower",
    ),
    (
        "Amongst Rolling Dunes",
        "Plastic Cubes",
        "Radar Dish",
    ),
    (
        "Surrounded by Graves",
        "Grimy Towers",
        "Abandoned Theatre",
    ),
    (
        "Surrounded by Monoliths",
        "Vine-covered Villas",
        "Sacred Catacombs",
    ),
    (
        "Surrounded by Fungal Groves",
        "Golden Domes",
        "Birthplace of Famed Musician",
    ),
    (
        "Surrounded by Dead Trees",
        "Chrome Spindles",
        "Birthplace of Famed Warrior",
    ),
    (
        "Shores of a Toxic Lake",
        "Repurposed Vehicles",
        "Birthplace of Famed Tyrant",
    ),
    (
        "Banks of a Toxic River",
        "Repurposed Weapon Arrays",
        "Petrified Tree",
    ),
    (
        "Amongst Huge Floating Crystals",
        "Moulded From Glass",
        "Wrecked Vehicle (p.xx)",
    ),
    (
        "On a Windswept Hill",
        "Hang From Wires",
        "Forbidden Grave",
    ),
    (
        "Nestled in a Valley ",
        "Atop Colossal Stilts",
        "Large Carnivorous Plant ",
    ),
    (
        "Amongst the Ruins of a Larger Settlement ",
        "Made from Bone",
        "Broken Statue",
    ),
    (
        "Amongst Cactus Groves",
        "Living Biotech Structures",
        "Shunned Shrine",
    ),
    (
        "Amongst Garbage-Strewn Sands",
        "Inside a Cave",
        "Enigmatic Obelisk",
    ),
    (
        "Foot of a Lone Mountain",
        "Inside a Huge Skeleton",
        "Automated Clock Tower",
    ),
    (
        "Amongst Desert Canyons",
        "Atop a Huge Tree",
        "Looming Ruin (p.xx)",
    ),
    (
        "Ancient Bomb Crater",
        "Large Communal Blocks",
        "Memory Crystal Array",
    ),
)

governmenta_governmentb_industry_dominantfaith = (
    (
        "Secretive",
        "Tyranny",
        "Hunting and Scavenging",
        "Church of the Promised Sun",
    ),
    (
        "Bloodthirsty",
        "Synarchism",
        "Agriculture (Fungi)",
        "Church of the Everbleeding Wound",
    ),
    (
        "Decrepit",
        "Noocracy",
        "Agriculture (Cacti)",
        "Vaa, Blue Goddess of Empty Spaces",
    ),
    (
        "Paranoid",
        "Theocracy",
        "Agriculture (Seven-Fruit Trees)",
        "Seekers of Eyeless Wisdom",
    ),
    (
        "Decadent",
        "Aristocracy",
        "Glassmaking",
        "The Binary Devotion",
    ),
    (
        "Unstable",
        "Gerontocracy",
        "Metalworking",
        "Titan Cults",
    ),
    (
        "Psychic",
        "Oligarchy",
        "Mining (Glowstone)",
        "Autarch Cult (see p.xx)",
    ),
    (
        "Diseased",
        "Commune",
        "Mining (Plastics)",
        "Church of Sevenscore Moons",
    ),
    (
        "Nostalgic",
        "Kleptocracy",
        "Mining (Sky-seeking Stone)",
        "Hidden Ghoul Cult",
    ),
    (
        "Eccentric",
        "Technocracy",
        "Mining (Synth Parts)",
        "Worship Local Monster (p.xx)",
    ),
    (
        "Feud-riven",
        "Monarchy",
        "Leatherworking",
        "Worship a Void Saint",
    ),
    (
        "Peaceful",
        "Kritarchy",
        "Breeding Packbeasts",
        "Worship a Fungal Saint",
    ),
    (
        "Collapsing",
        "Matriarchy",
        "Breeding Fighting Beasts",
        "Worship a local Petty God (p.xx)",
    ),
    (
        "Incompetent",
        "Patriarchy",
        "Pottery",
        "Worship Azathoth, the Daemon Sultan",
    ),
    (
        "Drunken",
        "Democracy",
        "Carpet Weaving",
        "Worship a Quantum Daemon (p.xx)",
    ),
    (
        "Militaristic",
        "Kratocracy",
        "Herding (Lizards)",
        "Brotherhood of the Black Sun",
    ),
    (
        "Gloomy",
        "Ochlocracy",
        "Herding (Zoxen)",
        "Worship a Bomb",
    ),
    (
        "Ruthless",
        "Sortition",
        "Herding (Land Parrots)",
        "Worship a Planeyman",
    ),
    (
        "Cheerful",
        "Kakistocracy",
        "Herding (Giant Snails)",
        "Worship Giant Animal",
    ),
    (
        "Manic",
        "Hive-Mind",
        "Brewing",
        "Militant Atheists",
    ),
)

governemnt_definitions = {
    "Tyranny": "The settlement is firmly under the boot of a sole tyrant. All decisions are made by this individual, who allows no dissent. All military, legal, economic, cultural, and religious institutions serve the will of the tyrant.",
    "Synarchism": "The settlement is ruled by a secret society. The mechanisms by which this is carried out may vary. There may be a public ‘mayor’ or ‘monarch’ who is merely a puppet for the true rulers. Alternately, the existence of the ruling group is public knowledge, but the identity of the members is not. For an extra twist, the members of this secret ruling society may not know one another’s identities.",
    "Noocracy": "The settlement is ruled by a council of the wisest residents. It is up to you exactly how the population quantifies ‘wisdom’ and who is judged to possess it.",
    "Theocracy": "The settlement is ruled according to strict religious tenets. The dominant faith is also the controlling political entity. Religious prohibitions and taboos are enforced by the state, and resid- ents who do not profess the faith are persecuted.",
    "Aristocracy": "The settlement is ruled by a class of landed hereditary aristocrats. While the nominal political structure might be democratic, in practise only those from an aristocratic family have any hope of governing.",
    "Gerontocracy": "The settlement is ruled by its oldest residents. Authority and social standing are directly correlated with old age. The political culture is likely to be calcified and resistant to change.",
    "Oligarchy": "The settlement is ruled by its wealthiest residents. Authority and social standing are directly correlated with material possessions. The politics and social life of the settlement are obsessed with accumulating the resource that makes one appear wealthy (this is probably not money, roll on the Trade Goods table (p.xx) for inspiration)",
    "Commune": "The settlement is governed by a non-hierarchical council of equals, who meet regularly to vote on matters of community concern. Possessions and labour are divided (at least in theory) totally equally. While there are likely some voices who are much louder in the council than others, there is no single authority figure.",
    "Kleptocracy": "The settlement is ruled by thieves. This not metaphorical: you have to be an accomplished thief to be part of the ruling apparatus. Authority is gained by demonstrating your thieving prowess, either through organised trials or just by stealing from other communities.",
    "Technocracy": "The settlement is ruled by the technologically adept. They may be a small caste of science-mystics who cow the populace with their knowledge, programmers of an ancient AI which makes all the actual decisions, or simply a group who know how an ancient machine works and leverage that knowledge into political power.",
    "Monarchy": "The settlement is ruled by a hereditary monarch, who claims unbroken descent from a line of royalty stretching into antiquity. The truth of this claim is probably false, but it keeps every- one happy to pretend the monarch is descended from the ancient Autarchs. The monarch may be strong politically (in which case see Tyranny) or weak and controlled by others (in which case see Oligarchy or Synarchism).",
    "Kritarchy": "The settlement is ruled by judges and the legal apparatus, who both make the law and pass judgement upon those who violate it. The text of the law may have been written long in the past, or it may be an ever-evolving document. In either case the penalties for breaking the law are serious.",
    "Matriarchy": " The settlement is ruled by women, with particular authority given to the eldest and most experienced. If the population is made up of ancestries that do not have a gender binary, then they assign authority based on some other set of perceived traits.",
    "Patriarchy": "The settlement is ruled by men, with particular authority given to the eldest and most experienced. If the population is made up of ancestries that do not have a gender binary, then they assign authority based on some other set of perceived traits.",
    "Democracy": "The settlement is ruled by elected officials. The elections may not be fair, the franchise may not be extended to all residents, and the officials may be incompetent and corrupt, but the candle of democracy still burns amongst the blue desolation.",
    "Sortition": "The settlement is ruled by selected officials, who are chosen by lottery. To really spice up the system, they are also deselected at random times, meaning the leadership class is constantly in flux. The settlement’s political culture is likely to be chaotic, contradictory, and short-termist.",
    "Kratocracy": "The settlement is ruled by the strongest. At any time one may challenge the current leader to a trial of strength, and the winner will be placed in charge. Ambitious citizens rise at dawn to begin training, lifting huge weights and grunting loud enough to wake the dead.",
    "Ochlocracy": "The settlement is ruled by mobs. Although there may be another form of nominal authority, they are cowed by the riotous population and go along with whatever the mob demands on that day. Mass brawls, vandalism, and arson are accepted ways of settling political disputes.",
    "Kakistocracy": "The settlement is ruled by the most foolish and least qualified citizens. How exactly this unusual state of affairs came to pass is not recorded, as the reign of these Fool Autarchs has been turbulent indeed, but the arrangement has held for several generations. Looking foolish and acting recklessly have become prized traits, and social gatherings inevitably devolve into competitive displays of lunacy.",
    "Hive-Mind": "The settlement is ruled by a psychic gestalt mind. Most if not all of the residents are but appendages of a Hive-Mind. The Hive-Mind may be rational and benign or irrational and malignant, actively seeking new hosts to inhabit. In either case, no other source of authority can coexist with such an entity.",
}


@dataclass
class Settlement:
    size: str
    water_source: str
    water_source_complication: str
    majority_population: str
    minority_population: str
    location: str
    houses: str
    local_landmark: str
    gov1: str
    gov2: str
    government_definition: str
    industry: str
    dominant_faith: str


def gen_settlement():
    size = choice(sizes)
    water_index = randint(0, 7)
    water_source = water_sources[water_index]
    water_source_complication = water_complications[water_index]
    majority_population = majority_populations[randint(1, 6) + randint(1, 6)]
    minority_population = minority_populations[randint(1, 6) + randint(1, 6)]
    location = choice(locations_houses_landmarks)[0]
    houses = choice(locations_houses_landmarks)[1]
    local_landmark = choice(locations_houses_landmarks)[2]
    gov1 = choice(governmenta_governmentb_industry_dominantfaith)[0]
    gov2 = choice(governmenta_governmentb_industry_dominantfaith)[1]
    government_definition = governemnt_definitions.get(gov2, "not found")
    industry = choice(governmenta_governmentb_industry_dominantfaith)[2]
    dominant_faith = choice(governmenta_governmentb_industry_dominantfaith)[3]

    return Settlement(
        size,
        water_source,
        water_source_complication,
        majority_population,
        minority_population,
        location,
        houses,
        local_landmark,
        gov1,
        gov2,
        government_definition,
        industry,
        dominant_faith,
    )


if __name__ == "__main__":
    print(gen_settlement())
