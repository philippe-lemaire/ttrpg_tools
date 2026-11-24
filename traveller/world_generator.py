from .roll import traveller_roll, get_key, roll_d66
import random


def to_hex(n):
    return hex(n)[2:].upper()


def from_hex(c):
    return int(c, 16)


size_table = {
    "0": ("Less than 1,000km", "Negligible"),
    "1": ("1,600km", "0.05"),
    "2": ("3,200km", "0.15"),
    "3": ("4,800km", "0.25"),
    "4": ("6,400km", "0.35"),
    "5": ("8,000km", "0.45"),
    "6": ("9,600km", "0.7"),
    "7": ("11,200km", "0.9"),
    "8": ("12,800km", "1.0"),
    "9": ("14,400km", "1.25"),
    "A": ("16,000km", "1.4"),
}

atmosphere_table = {
    "0": (
        "None",
        "0.00",
        "Vacc Suit",
    ),
    "1": (
        "Trace",
        "0.001 to 0.09",
        "Vacc Suit",
    ),
    "2": (
        "Very Thin, Tainted",
        "0.1 to 0.42",
        "Respirator, Filter",
    ),
    "3": (
        "Very Thin",
        "0.1 to 0.42",
        "Respirator",
    ),
    "4": (
        "Thin, Tainted",
        "0.43 to 0.7",
        "Filter",
    ),
    "5": (
        "Thin",
        "0.43 to 0.7",
        None,
    ),
    "6": (
        "Standard",
        "0.71-1.49",
        None,
    ),
    "7": (
        "Standard, Tainted",
        "0.71-1.49",
        "Filter",
    ),
    "8": (
        "Dense",
        "1.5 to 2.49",
        None,
    ),
    "9": (
        "Dense, tainted",
        "1.5 to 2.49",
        "Filter",
    ),
    "A": (
        "Exotic",
        "Varies",
        "Air Supply",
    ),
    "B": (
        "Corrosive",
        "Varies",
        "Vacc Suit",
    ),
    "C": (
        "Insidious",
        "Varies",
        "Vacc Suit",
    ),
    "D": (
        "Very Dense",
        "2.5+",
        None,
    ),
    "E": (
        "Low",
        "0.5 or less",
        None,
    ),
    "F": (
        "Unusual",
        "Varies",
        "Varies",
    ),
}

hydrographics_table = {
    "0": (
        "0%–5%",
        "Desert world",
    ),
    "1": (
        "6%–15%",
        "Dry world",
    ),
    "2": (
        "16%–25%",
        "A few small seas",
    ),
    "3": (
        "26%–35%",
        "Small seas and oceans",
    ),
    "4": (
        "36%–45%",
        "Wet world",
    ),
    "5": (
        "46%–55%",
        "A large ocean",
    ),
    "6": (
        "56%–65%",
        "Large oceans",
    ),
    "7": (
        "66%–75%",
        "Earth-like world",
    ),
    "8": (
        "76%–85%",
        "Only a few islands and archipelagos",
    ),
    "9": (
        "86%–95%",
        "Almost entirely water",
    ),
    "A": (
        "96%–100%",
        "Waterworld",
    ),
}

temperature_table = {
    2: (
        "Frozen",
        "-51º or less",
        "Frozen world. No liquid water, very dry atmosphere.",
    ),
    4: (
        "Cold",
        "-51º to 0º",
        "Icy world. Little liquid water, extensive ice caps, few clouds.",
    ),
    9: (
        "Temperate",
        "0º to 30º",
        " Temperate world. Earth-like. Liquid & vaporised water are common, moderate ice caps.",
    ),
    11: (
        "Hot",
        " 31º to 80º",
        "Hot world. Small or no ice caps, little liquid water. Most water in the form of clouds.",
    ),
    12: ("Boiling", "81º+", "Boiling world. No more ice caps, little liquid water."),
}

population_table = {
    "0": (
        "None",
        "0",
        "—",
    ),
    "1": (
        "Few",
        "1+",
        "A tiny farmstead or a single family",
    ),
    "2": (
        "Hundreds",
        "100+",
        "A village",
    ),
    "3": (
        "Thousands",
        "1,000+",
        "—",
    ),
    "4": (
        "Tens of thousands",
        "10,000+",
        "Small town",
    ),
    "5": (
        "Hundreds of thousands",
        "100,000+",
        "Average city",
    ),
    "6": (
        "Millions",
        "1,000,000+",
        "—",
    ),
    "7": (
        "Tens of millions",
        "10,000,000+",
        "Large city",
    ),
    "8": (
        "Hundreds of millions",
        "100,000,000+",
        "—",
    ),
    "9": (
        "Billions",
        "1,000,000,000+",
        "Present day Earth",
    ),
    "A": (
        "Tens of billions",
        "10,000,000,000+",
        "—",
    ),
    "B": (
        "Hundreds of billions",
        "100,000,000,000+",
        "Incredibly crowded world",
    ),
    "C": (
        "Trillions",
        "1,000,000,000,000+",
        "World-city",
    ),
}

government_table = {
    "0": (
        "None",
        "No government structure. In many cases, family bonds predominate.",
        "Family, clan, anarchy ",
        "None",
    ),
    "1": (
        "Company/Corporation",
        "Ruling functions are assumed by a company managerial elite and most citizenry are company employees or dependants.",
        "Corporate outpost, asteroid mine, feudal domain",
        "Weapons, Drugs, Travellers",
    ),
    "2": (
        "Participating Democracy",
        "Ruling functions are reached by the advice  and consent of the citizenry directly.",
        "Collective, tribal council, comm-linked consensus",
        "Drugs",
    ),
    "3": (
        "Self-Perpetuating Oligarchy",
        "Ruling functions are performed by a restricted minority, with little or no input from the mass of citizenry.",
        "Plutocracy, hereditary ruling caste",
        "Technology, Weapons, Travellers",
    ),
    "4": (
        "Representative Democracy",
        "Ruling functions are performed by elected representatives.",
        "Republic, democracy",
        "Drugs, Weapons, Psionics",
    ),
    "5": (
        "Feudal Technocracy",
        "Ruling functions are performed by individuals for persons who agree to be ruled by them. Relationships are based the performance of technical activities that are mutually beneficial.",
        "Those with access to advanced technology tend to have higher social status",
        "Technology, Weapons, Computers",
    ),
    "6": (
        "Captive Government",
        "Ruling functions are performed by an imposed leadership answerable to an outside group.",
        "A colony or conquered area",
        "Weapons, Technology, Travellers",
    ),
    "7": (
        "Balkanisation",
        "No central authority exists; rival governments complete for control. Law level refers to the government nearest the starport.",
        "Multiple governments, civil war",
        "Varies",
    ),
    "8": (
        "Civil Service Bureaucracy",
        "Ruling functions are performed by government agencies employing individuals selected for their expertise.",
        "Technocracy, Communism",
        "Drugs, Weapons",
    ),
    "9": (
        "Impersonal Bureaucracy",
        "Ruling functions are performed by agencies that have become insulated from the governed citizens.",
        "Entrenched castes of bureaucrats, decaying",
        "Technology, Weapons, Drugs, Travellers, Psionics",
    ),
    "A": (
        "Charismatic Dictator",
        "Ruling functions are performed by a agencies directed by a single leader who enjoys the overwhelming confidence of the citizens.",
        "Revolutionary leader, messiah, emperor",
        "None",
    ),
    "B": (
        "Non-Charismatic Leader",
        "A previous charismatic dictator has been replaced by a leader through normal channels.",
        "Military dictatorship, hereditary kingship",
        "Weapons, Technology, Computers",
    ),
    "C": (
        "Charismatic Oligarchy",
        "Ruling functions are performed by a select group of members of an organisation or class that enjoys the overwhelming confidence of the citizenry.",
        "Junta, revolutionary council",
        "Weapons",
    ),
    "D": (
        "Religious Dictatorship",
        "Ruling functions are performed by a religious organisation without regard to the specific individual needs of the citizenry.",
        "Cult, transcendent philosophy, psionic group mind",
        "Varies",
    ),
    "E": (
        "Religious Autocracy",
        "Government by a single religious leader having absolute power over the citizenry.",
        "Messiah",
        "Varies",
    ),
    "F": (
        "Totalitarian Oligarchy",
        "Government by an all-powerful minority which maintains absolute control through widespread coercion and oppression.",
        "World church, ruthless corporation",
        "Varies",
    ),
}

cultural_differences_d66_table = {
    "11": "Sexist – one gender is considered subservient or inferior to the other.",
    "12": "Religious – culture is heavily influenced by a religion or belief systems, possibly one unique to this world.",
    "13": "Artistic – art and culture are highly prized. Aesthetic design is important in all artefacts produced on world.",
    "14": "Ritualised – social interaction and trade is highly formalised. Politeness and adherence to traditional forms is considered very important. ",
    "15": "Conservative – the culture resists change and outside influences.",
    "16": "Xenophobic – the culture distrusts outsiders and alien influences. Offworlders will face considerable prejudice.",
    "21": "Taboo – a particular topic is forbidden and cannot be discussed. Travellers who unwittingly mention this topic will be ostracised.",
    "22": "Deceptive – trickery and equivocation are considered acceptable. Honesty is a sign of weakness.",
    "23": "Liberal – the culture welcomes change and offworld influence. Travellers who bring new and strange ideas will be welcomed.",
    "24": "Honourable – one’s word is one’s bond in the culture. Lying is both rare and despised.",
    "25": "Influenced – the culture is heavily influenced by another, neighbouring world. Roll again for a cultural quirk that has been inherited from the culture.",
    "26": "Fusion – the culture is a merger of two distinct cultures. Roll again twice to determine the quirks inherited from these cultures. If the quirks are incompatible, then the culture is likely divided.",
    "31": "Barbaric – physical strength and combat prowess are highly valued in the culture. Travellers may be challenged to a fight or dismissed if they seem incapable of defending themselves. Sports tend towards the bloody and violent.",
    "32": "Remnant – the culture is a surviving remnant of a once-great and vibrant civilisation, clinging to its former glory. The world is filled with crumbling ruins and every story revolves around the good old days.",
    "33": "Degenerate – the culture is falling apart and is on the brink of war or economic collapse. Violent protests are common and the social order is decaying.",
    "34": "Progressive – the culture is expanding and vibrant. Fortunes are being made in trade; science is forging bravely ahead.",
    "35": "Recovering – a recent trauma, such as a plague, war, disaster or despotic regime has left scars on the culture.",
    "36": "Nexus – members of many different cultures and species visit here.",
    "41": "Tourist Attraction – some aspect of the culture or the planet draws visitors from all over civilised space.",
    "42": "Violent – physical conflict is common, taking the form of duels, brawls or other contests. Trial by combat is a part of their judicial system.",
    "43": "Peaceful – physical conflict is almost unheard- of. The culture produces few soldiers and diplomacy reigns supreme. Forceful Travellers will be ostracised.",
    "44": "Obsessed – everyone is obsessed with or addicted to a substance, personality, act or item. This monomania pervades every aspect of the culture.",
    "45": "Fashion – fine clothing and decoration are considered vitally important in the culture. Underdressed Travellers have no standing here.",
    "46": "At war – the culture is at war, either with another planet or polity, or is troubled by terrorists or rebels.",
    "51": "Unusual Custom: Offworlders – space travellers hold a unique position in the culture’s mythology or beliefs and travellers will be expected to live up to these myths.",
    "52": "Unusual Custom: Starport – the planet’s starport is more than a commercial centre; it might be a religious temple or be seen as highly controversial and surrounded by protestors.",
    "53": "Unusual Custom: Media – news agencies and telecommunications channels are especially strange here. Getting accurate information may be difficult.",
    "54": "Unusual Customs: Technology – the culture interacts with technology in an unusual way. Telecommunications might be banned, robots might have civil rights or cyborgs might be property.",
    "55": "Unusual Customs: Lifecycle – there might be a mandatory age of termination or anagathics might be widely used. Family units might be different, with children being raised by the state or banned in favour of cloning.",
    "56": "Unusual Customs: Social Standings – the culture has a distinct caste system. Travellers of a low social standing who do not behave appropriately will face punishment.",
    "61": "Unusual Customs: Trade – the culture has an odd attitude towards some aspect of commerce, which may interfere with trade at the spaceport. For example, merchants might expect a gift as part of a deal or some goods may only be handled by certain families.",
    "62": "Unusual Customs: Nobility – those of high social standing have a strange custom associated with them; perhaps nobles are blinded, must live in gilded cages or only serve for a single year before being exiled.",
    "63": "Unusual Customs: Sex – the culture has an unusual attitude towards intercourse and reproduction. Perhaps cloning is used instead or sex is used to seal commercial deals.",
    "64": "Unusual Customs: Eating – food and drink occupies an unusual place in the culture. Perhaps eating is a private affair or banquets and formal dinners are seen as the highest form of politeness.",
    "65": "Unusual Customs: Travel – Travellers may be distrusted or feted, or perhaps the culture frowns on those who leave their homes.",
    "66": "Unusual Custom: Conspiracy – something strange is going on. The government is being subverted by another group or agency.",
}

starport_class_table = {
    2: "X",
    4: "E",
    6: "D",
    8: "C",
    10: "B",
    11: "A",
}


class World:
    def __init__(self, profile, temp_roll=9):
        self.profile = profile
        # size, 2nd letter in the profile
        self.size = size_table.get(profile[1])
        self.diameter, self.gravity = self.size
        # atmosphere
        self.atmosphere = atmosphere_table[profile[2]]
        (
            self.atmosphere_composition,
            self.atmosphere_pressure,
            self.atmosphere_survival_gear_required,
        ) = self.atmosphere
        # temperature
        k = get_key(temp_roll, temperature_table)
        self.temperature = temperature_table[k]
        (
            self.temperature_type,
            self.temperature_average,
            self.temperature_description,
        ) = self.temperature
        # hydrographics
        self.hydrographics = hydrographics_table[profile[3]]
        self.hydrographic_percentage, self.hydrographic_description = self.hydrographics
        # population
        self.population = population_table[profile[4]]
        (
            self.population_inhabitants,
            self.population_range,
            self.population_description,
        ) = self.population
        # government
        self.government = government_table[profile[5]]
        (
            self.government_type,
            self.government_description,
            self.government_example,
            self.government_contraband_example,
        ) = self.government

        # cultural difference
        cultural_difference_roll = roll_d66()
        self.cultural_difference = cultural_differences_d66_table[
            cultural_difference_roll
        ]

        if cultural_difference_roll == "26":
            set_of_valid_keys = sorted(
                set(cultural_differences_d66_table.keys()) - {"26"}
            )
            keys = random.sample(set_of_valid_keys, 2)
            fused = [cultural_differences_d66_table.get(k) for k in keys]
            self.cultural_difference = "\n".join([self.cultural_difference] + fused)

        # Law Level
        self.law_level = profile[-2]
        # starport
        self.star_port = profile[0]
        # tech_level
        self.tech_level = profile[-1]

    def __repr__(self):
        return self.profile


def gen_world():
    # size 2D -2
    size_roll = to_hex(traveller_roll() - 2)
    # starport quality, hardcoded for now
    starport_quality_roll = "7"
    # atmosphere 2D -7 + Size
    atmosphere_roll = to_hex(traveller_roll() - 7 + from_hex(size_roll))
    # fix negative atmosphere
    if atmosphere_roll.startswith("X"):
        atmosphere_roll = "0"
    # temperature roll
    # Atmosphere 0 or 1: No modifiers, but
    # temperature swings from roasting during the day to frozen at night.
    # Atmosphere 2 or 3:
    # DM-2
    # Atmosphere 4, 5 or E: DM-1
    # Atmosphere 6 or 7:DM+0
    # Atmosphere 8 or 9:DM+1
    # Atmosphere A, D or F: DM+2
    # Atmosphere B or C: DM+6
    base_temp_roll = traveller_roll()
    temperature_dm = 0
    if atmosphere_roll in "23":
        temperature_dm = -2
    elif atmosphere_roll in "45E":
        temperature_dm = -1
    elif atmosphere_roll in "89":
        temperature_dm = +1
    elif atmosphere_roll in "ADF":
        temperature_dm = +2
    elif atmosphere_roll in "BC":
        temperature_dm = +6
    temp_roll = base_temp_roll + temperature_dm
    # deal with extreme values
    if temp_roll < 0:
        temp_roll = 0
    if temp_roll > 12:
        temp_roll = 12

    # hydrographics roll
    # apply DM from temperature
    hydrographics_roll_dm = 0
    if atmosphere_roll not in "DF":
        if temp_roll >= 10 and temp_roll <= 11:
            hydrographics_roll_dm = -2
        elif temp_roll >= 12:
            hydrographics_roll_dm = -6
    if size_roll in "01":
        hydrographics_roll = "0"
    elif atmosphere_roll in "01ABCDEF":
        hydrographics_roll = to_hex(
            traveller_roll() - 7 + from_hex(atmosphere_roll) - 4 + hydrographics_roll_dm
        )
    else:
        hydrographics_roll = to_hex(
            traveller_roll() - 7 + from_hex(atmosphere_roll) + hydrographics_roll_dm
        )

    # fix negative hydrographics roll
    if hydrographics_roll.startswith("X"):
        hydrographics_roll = "0"
    # fix too high hydrographics roll
    if from_hex(hydrographics_roll) > 10:
        hydrographics_roll = "A"

    # Population 2D-2

    population_roll = to_hex(traveller_roll() - 2)

    # Government 2D - 7 + population roll
    if population_roll == "0":
        government_roll = "0"
    else:
        government_roll = to_hex(traveller_roll() - 7 + from_hex(population_roll))
    # Fix potential extreme government roll
    if government_roll.startswith("X"):
        government_roll = "0"
    elif from_hex(government_roll) > 15:
        government_roll = "F"

    # Law level Law Level is determined by rolling 2D–7 and adding the Government code.

    law_level_roll = to_hex(traveller_roll() - 7 + from_hex(government_roll))
    # fix extreme values
    if law_level_roll.startswith("X"):
        law_level_roll = "0"
    elif from_hex(law_level_roll) > 15:
        law_level_roll = "F"

    # star port
    # DM+1 if the planet’s Population is 8–9
    # DM+2 if the planet’s Population is 10+
    # DM–1 if the planet’s Population is 3–4
    # DM–2 if the planet’s Population is 2–
    star_port_dm = 0
    if population_roll in "89":
        star_port_dm = 1
    elif population_roll in "ABCDEF":
        star_port_dm = 2
    elif population_roll in "34":
        star_port_dm = -1
    elif population_roll in "012":
        star_port_dm = -1
    star_port_roll = traveller_roll() + star_port_dm
    star_port_key = get_key(star_port_roll, starport_class_table)
    star_port_rating = starport_class_table[star_port_key]

    # tech level
    star_port_influence_on_tech_level_table = {"A": 6, "B": 4, "C": 2, "X": -4}
    star_port_influence_on_tech_level = star_port_influence_on_tech_level_table.get(
        star_port_rating, 0
    )
    size_roll_influence_on_tech_level_table = {"0": 2, "1": 2, "2": 1, "3": 1, "4": 1}
    size_roll_influence_on_tech_level = size_roll_influence_on_tech_level_table.get(
        size_roll, 0
    )
    atmosphere_roll_influence_on_tech_level = (
        1 if atmosphere_roll in "01234ABCDEF" else 0
    )
    hydrographics_influence_on_tech_level = 1 if hydrographics_roll in "09A" else 0
    if hydrographics_roll == "A":
        hydrographics_influence_on_tech_level += 1
    population_influence_on_tech_level = 1 if population_roll in "1234589A" else 0
    if population_roll == "9":
        population_influence_on_tech_level += 1
    if population_roll == "A":
        population_influence_on_tech_level += 3
    government_influence_on_tech_level_table = {
        "0": 1,
        "5": 1,
        "7": 2,
        "D": -2,
        "E": -2,
    }
    government_influence_on_tech_level = government_influence_on_tech_level_table.get(
        government_roll, 0
    )
    tech_level_dm = (
        star_port_influence_on_tech_level
        + size_roll_influence_on_tech_level
        + atmosphere_roll_influence_on_tech_level
        + hydrographics_influence_on_tech_level
        + population_influence_on_tech_level
        + government_influence_on_tech_level
    )
    tech_level_roll = to_hex(random.randint(1, 6) + tech_level_dm)
    # final profile string
    profile = f"{star_port_rating}{size_roll}{atmosphere_roll}{hydrographics_roll}{population_roll}{government_roll}{law_level_roll}{tech_level_roll}"

    return World(profile, temp_roll)


"""
if __name__ == "__main__":
    world = gen_world()
    print(world.diameter)
    print(world.atmosphere_composition)
    print(world.hydrographic_description, world.hydrographic_percentage)
    print(world.temperature)
    print(world.population)
    print(world.government)
    print(world)
    print(world.cultural_difference)
"""
