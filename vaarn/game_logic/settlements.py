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

building_types = (
    "Disreputable or Abandoned building",
    "Residential Building",
    "Industrial Building or Workshop",
    "Commercial Building",
    "Religious Site",
    "Minor Government Building",
)

assets_data = (
    (
        "Matter Fabricator",
        "A wonder of the ancient world. Matter fabricators generate mass from thin air, working thousands of times faster than a mortal craftsman could. Most fabricators have but a single object in their repertoire of forms, although some exist that can create more than one thing. The settlement is overrun with the object the fabricator creates: the residents cannot even give them away.",
    ),
    (
        "Beast Breeding Stables",
        "The settlement is known for breeding pack beasts, whether they be burden birds, zorses, weeping lizards, or something even stranger. Healthy and well-trained examples of the animals are available for purchase in all markets and serrais. Races are held weekly, with much betting upon the outcome.",
    ),
    (
        "Oracle’s Abode",
        "The settlement is known as the residence of a Vaarnish Oracle, whose wisdom is unquestioned and whose eccentricites are tolerated. Generate using the table on p.xx.",
    ),
    (
        "Notable Monastery",
        "The settlement is home to a large monastery or temple, which exercises considerable influence over the politics and economy of the settlement. Assume that the monks worship the dominant faith of the settlement.",
    ),
    (
        "Pilgrimage Site",
        "The settlement is built around a notable Vaarnish holy site. It may be the grave of an Autarch, the final resting place of Solar Saint’s bones, or simply home to a fabled fountain or other holy object. Pilgrims descend on the settlement from all across Vaarn, travelling on foot or bearing their sick in litters.",
    ),
    (
        "Famous Tavern",
        "The settlement is home to a tavern that is famous throughout Vaarn, either for the quality of its beverages, the skill of its musicians and acrobats, or else the rudeness and slovenliness of its barkeep.",
    ),
    (
        "Verdant Orchards",
        "The settlement boasts proudly maintained orchards, a prize beyond measure in the arid climate of Vaarn. The water consumption per day is astronomical, but the trees and the fruit they bear is considered worth any price.",
    ),
    (
        "Fighting Pit",
        "The settlement contains a gladiatorial arena, in which professional fighters compete in bloody games of domination. Famed gladiators live luxuriously, while the losers lie ignominiously in sick beds or else are tossed into open graves.",
    ),
    (
        "Hypergeometric Building",
        "The settlement is famed for a hypergeometric building, the magnum opus of a long-perished hypergeometrician. Paradoxical architecture can take many forms, from innocuous looking-houses which are cavernously large on the inside, to aqueducts where water runs uphill or inverted ziggurats where gravity has no purchase. The building may be in active use, or it may be con- sidered dangerous or cursed, shunned by all right-thinking citizens.",
    ),
    (
        "Ancient Spacecraft",
        "The settlement is built around an ancient spacecraft, which either forms part of the infrastructure or is merely a whimsical decorative feature, a reminder of an age when humanity’s ambitions ranged much further than a day’s ride on zorseback. The craft can no longer fly, although the citizens may wish that it could.",
    ),
    (
        "Vault Entrance",
        "Adventurers do not have to travel beyond the settlement’s walls to find an ingress into the fabled vaults of Vaarn: the chrome caverns that honeycomb the Urth lie close to the surface here. The vault entrance may be almost forgotten, accessed by a set of cellar stairs that descend much further than one would expect, or else it may be a vast and imposing structure, equipped with enormous blast doors that open only at the command of the settlement’s rulers. The citizens know the vault lies beneath them, but none venture there. You seem like bolder types.",
    ),
    (
        "Great Waste Pit",
        "The settlement is home to a refuse pit of imperious depth and pungency, large enough to sustain its own ecosystem, a waste pit far exceeding the current day needs of the citizens. The olfactory onslaught is notable from a day’s travel away, and those not inured to the stench walk the streets with masks wrapped around their faces. A despised but vital social undercaste maintains the waste pit and beats back the fungal insurgencies that periodically emerge from it.",
    ),
    (
        "Synth Repair Facility",
        "The synths of Vaarn could once find repair facilities in innumerable places, and were never far from a library of spare parts. This is no longer the case in this last red age, and spare parts are more com- monly wrenched from the husks of recently dead synths. This settlement is one of few that still boasts a functional Synth Repair Facility, with fully operational ReadMe consoles and supercooled storage facilities filled with factory fresh parts. As such the settlement is overrun with damage synths, all clamouring for parts. The settlement’s rulers do not allow access for free.",
    ),
    (
        "Mystic College",
        "The settlement is home to a college for esoteric study. Those seeking to enlarge their minds flock here to study under fabled masters. The streets are filled with blindfolded acolytes trying to navigate using their third eye, and demonstrations of psionic power light up the night sky with unurthly colours. The mystics claim to be divorced from mundane concerns, yet many suspect they have some supernatural influence over the settlement’s government.",
    ),
    (
        "House of Healing",
        "The settlement is home to a great House of Healing, situated at an auspicious confluence of astral pathways or else built above a restorative hot spring. An ancient and venerable order of sur- geon-priests practise the accumulated medical knowledge of a thousand generations. The sick travel here from across Varna and beyond, seeking cures for the rarest and most virulent diseases. They are treated, for a price.",
    ),
    (
        "Master Alchemist’s Workshop",
        "The settlement is home to a Master Alchemist, who plies their trade from a large and well-defended workshop. Wondrous Elixirs (p.xx) of all kinds are brewed here, although the Master Alchemist is well-known for being capricious in their dealings. Those who come bearing rare alchemical components (p.xx) are more likely to be received as guests.",
    ),
    (
        "Grand Theatre",
        "The settlement plays host to a great and imposing theatre, and all citizens are avid thespians or audience members. Every night a play is staged: the tragic dramas of the Fallen Autarchy, experi- mental Neo-Neo-Relativist monologues, the delicate choral satires once beloved of the Lunan artisocracy. The settlement’s government is intertwined with the theatre in some way, perhaps drawing legitimacy from the themes of the plays.",
    ),
    (
        "Pleasure Gardens",
        "The settlement’s pride and joy is an expansive and verdant pleasure garden, planted with ornamental foliage from across Vaarn and beyond it. The settlement’s cultural life revolves around this pleasure garden, and the upkeep is of absolute importance. A vast quantify of water is invested in keeping the garden from withering.",
    ),
    (
        "Stylite’s Pillar",
        "One of the settlement’s residents is a stylite: a religious hermit who dwells atop a colossal pillar. The stylite is considered a tourist attraction, and is given rations via a system of pulleys. The stylite, almost certainly mad and traditionally naked, periodically emerges from their sky-scraping hovel to harangue the crowd below, cursing the settlement’s government and preaching of the end times. It is all good fun.",
    ),
    (
        "Orbital Defence Cannon",
        "The Autarchs in their wisdom erected a vast system of orbital defence cannons that once girdled the entire Urth, sentinels which guarded against incursions by the Lunan empire that lurked in the black gulf overhead. The Autarchs are long dead but a handful of their celestial sentries remain active, ceaselessly scanning the bejewelled firmament for invaders. The settlement is built around one of these cannons, which resembles a vast crowned Autarch head cast from tarnished gold. The cannon’s eyes track the movement of the stars overhead, and it occasionally belches forth clouds of micro-missiles which streak up into the sky in search of perceived invaders. The settlement is generally not approached by air.",
    ),
)

problems_data = (
    (
        "Power Struggle",
        "The settlement’s political system is undergoing an upheaval. Roll again on the government types table (p.xx): the result is the insurgent political system that is trying to replace the dominant one. For every NPC generated in the settlement, roll a die: even numbers indicate that they are loyal to the old system of government, while odd numbers indicate they are openly or covertly supporters of the nascent system.",
    ),
    (
        "Bigotry",
        "The settlement is riven by deep-seated bigotry, expressed by the majority population type towards the minority. If the population is homogeneous, then the bigotry revolves around some even more petty and obscure difference.",
    ),
    (
        "Virulent Disease",
        "A disease (select one from p.xx) runs rampant through the settlement, thwarting all attempts to cure it. Those believed to be infected are shunned from fear, the dead buried in mass graves without normal rituals.",
    ),
    (
        "Nanomachine Infection",
        "A nanomachine infection (select one from p.xx) runs rampant through the settlement, thwarting all attempts to cure it. Those believed to be infected are shunned from fear.",
    ),
    (
        "Unquiet Dead",
        "Those who die within the bounds of the settlement do not stay dead. The cause is unclear, but all burials take place outside the walls.",
    ),
    (
        "Rapacious Local Monsters",
        "The settlement is harried by a nearby lair of monsters. Generate using the table on p.xx, creating the maximum population for the lair type.",
    ),
    (
        "Banditry",
        "The settlement is harried by a group of bandits, who make their camp (p.xx) somewhere nearby. The bandits are cutting off trade to the settlement, and may even make raids inside the walls to take what they please.",
    ),
    (
        "Blood Feud",
        "The settlement is riven by an internal feud between two family groups (for ancestries who do not have families, substitute with voluntary clubs or associations). All social and political life is concentrated on furthering this feud, to the detriment of all other goals.",
    ),
    (
        "Looming Famine",
        "The settlement’s food source is under threat or has already failed, and the stores of food are running perilously low. This may be public knowledge, or it may be concealed by the settlement’s rulers.",
    ),
    (
        "Looming Drought",
        "The settlement’s water source is under threat or has already dried up, and reserves of fresh water are running perilously low. This may be public knowledge, or it may be concealed by the settlement’s rulers.",
    ),
    (
        "No Children",
        "The settlement’s native population is ageing and cannot renew itself, with the normal reproductive processes of the ancestries in question having proven fruitless. The settlement has no children or immature examples of the ancestry. The only population growth comes from travellers or outsiders, who then also find they cannot produce offspring. The cause is unknown, although everyone has theories.",
    ),
    (
        "Quantum Daemon Curse",
        "The settlement is subject to a curse by an angry Quantum Daemon (p.xx), who has levied some improbable and poetic curse upon the citizens.",
    ),
    (
        "Unicorn Infestation",
        "The settlement is infested with Vaarnish Unicorns (p.xx). They breed quickly, eat everything that they can find, and leave piles of glittering dung everywhere. As fast as they can be exterminated they reappear. Everyone is thoroughly sick of them.",
    ),
    (
        "Shared Nightmares",
        "The inhabitants are troubled at night by a shared dream, which has been worsening as the days go by. They believe there is some psychic malevolence at work, but have been unable to discover the source. PCs who sleep in the settlement also begin to experience this nightmare.",
    ),
    (
        "Cacklemaw Extortion",
        "The settlement pays tribute to a Cacklemaw Clan, whose War Mama counts the inhabitants as her under creatures. Cacklemaw Clans are generally nomadic, but they show up to collect tribute at least once a year. A visit is looming, and the demands of the War Mama have ballooned beyond what the settlement can give.",
    ),
    (
        "Witch Hunt",
        "The inhabitants are consumed with obsessive searches for hidden internal enemies, violent social purges that seem to have little basis in reality. Those accused of subversion are given mock trials and ostracised or executed.",
    ),
    (
        "Infiltrators",
        "The settlement has been infiltrated by an outside group or power, and the interlopers are up to no good. Sabotage, impersonation, and paranoid are running rampant. There is suspicion that the seat of government itself has already been infiltrated.",
    ),
    (
        "Religious Reformation",
        "The dominant religion of the settlement is challenged by a newer upstart faith. Roll again on the dominant religion table (p.xx) to discover the nature of the new religion. For every NPC generated in the settlement, roll a die: even numbers indicate that they are believers in the dominant faith, while odd numbers indicate they are openly or covertly supporters of the new religion.",
    ),
    (
        "Faa Vendetta",
        "The settlement is subject to a vendetta by a local Faa Nomad Tribe (p.xx). The Faa nomads refuse to aid anyone connected with the settlement, and may be strangling trade or sabotaging water sources.",
    ),
    (
        "Looming War",
        "The settlement is preparing for open warfare with a neighbouring settlement (either choose one already existing on the map, or generate a more distant rival).",
    ),
)


@dataclass
class Asset:
    name: str
    description: str


class Problem(Asset):
    pass


def gen_asset():
    return Asset(*choice(assets_data))


def gen_problem():
    return Problem(*choice(problems_data))


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
    asset: Asset
    buildings: list
    problem: Problem


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
    asset = gen_asset()
    buildings = [choice(building_types) for _ in range(4)]
    problem = gen_problem()

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
        asset,
        buildings,
        problem,
    )


if __name__ == "__main__":
    print(gen_settlement())
