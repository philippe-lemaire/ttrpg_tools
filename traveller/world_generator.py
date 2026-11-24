from roll import traveller_roll


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


class World:
    def __init__(self, profile):
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
        # hydrographics
        self.hydrographics = hydrographics_table[profile[3]]
        self.hydrographic_percentage, self.hydrographic_description = self.hydrographics

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
    # hydrographics roll

    if size_roll in "01":
        hydrographics_roll = "0"
    elif atmosphere_roll in "01ABCDEF":
        hydrographics_roll = to_hex(
            traveller_roll() - 7 + from_hex(atmosphere_roll) - 4
        )
    else:
        hydrographics_roll = to_hex(traveller_roll() - 7 + from_hex(atmosphere_roll))
    # fix negative hydrographics roll
    if hydrographics_roll.startswith("X"):
        hydrographics_roll = "0"
    # fix too high hydrographics roll
    if from_hex(hydrographics_roll) > 10:
        hydrographics_roll = "A"
    profile = f"{starport_quality_roll}{size_roll}{atmosphere_roll}{hydrographics_roll}"
    return World(profile)


if __name__ == "__main__":
    world = gen_world()
    print(world.diameter)
    print(world.atmosphere_composition)
    print(world.hydrographic_description, world.hydrographic_percentage)
