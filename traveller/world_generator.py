from roll import traveller_roll, get_key


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


class World:
    def __init__(self, profile, temp_roll):
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
    profile = f"{starport_quality_roll}{size_roll}{atmosphere_roll}{hydrographics_roll}{population_roll}"
    return World(profile, temp_roll)


if __name__ == "__main__":
    world = gen_world()
    print(world.diameter)
    print(world.atmosphere_composition)
    print(world.hydrographic_description, world.hydrographic_percentage)
    print(world.temperature)
    print(world.population)
