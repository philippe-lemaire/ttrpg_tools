from random import choice, sample
from dataclasses import dataclass

oasis_data = (
    (
        "Very Blue",
        "Date Palms",
        "Trading Caravan",
        "Pay Toll",
    ),
    (
        "Leaks from Machinery",
        "Flamingos",
        "Trading Caravan",
        "No Bloodshed",
    ),
    (
        "Incredibly Clear",
        "Towering Rock",
        "Trading Caravan",
        "Moonlit Sacrifices",
    ),
    (
        "Umber and Silty",
        "Rusted War Machine",
        "Trading Caravan",
        "No Bathing",
    ),
    (
        "Still and Glassy",
        "Faa Nomads",
        "Autarch Statue",
        "Ritual Combat",
    ),
    (
        "Black and Muddy",
        "Faa Nomads",
        "Flowering Bushes",
        "Vow of Silence",
    ),
    (
        "Almost Gone",
        "Ibis",
        "Faa Nomads",
        "Ruled by Chance",
    ),
    (
        "Full of Fish",
        "Lurking Crocodiles",
        "Hegemony Rangers",
        "Sacred to Men",
    ),
    (
        "Tastes Sour",
        "Black Obelisks",
        "Bounty Hunters",
        "Sacred to Women",
    ),
    (
        "Algae-choked",
        "Decaying Buildings",
        "Titan Cultists",
        "Consult Computer",
    ),
    (
        "Fetid",
        "Addax Herd",
        "Wandering Mystics",
        "Consult Oracle",
    ),
    (
        "Full of Plastic",
        "Solar Panels",
        "Travelling Circus",
        "Must be Naked",
    ),
    (
        "Rusty Red",
        "Arcology Dome",
        "Knight Peregrine",
        "Must be Veiled",
    ),
    (
        "Warm and Bubbling",
        "Crystalline Growths",
        "Escaped Slaves",
        "An Animal Is Holy",
    ),
    (
        "Champagne Coloured",
        "Fungal Growths",
        "Sunburnt Exiles",
        "An Animal Is Profane",
    ),
    (
        "Deep and Silent",
        "Broken Pillars",
        "Pilgrim Monks",
        "Laughter is Prohibited",
    ),
    (
        "Inside a Cave",
        "Grave",
        "Synths",
        "Sacred to Petty God",
    ),
    (
        "Healing Properties",
        "Wrecked Synths",
        "Cacklemaw Exiles Drug Ritual",
    ),
    (
        "Sugary Sweet",
        "Mud Holes",
        "Exultant in Disguise",
        "Water Ritual",
    ),
    (
        "Mildly Psychedelic",
        "Sacred Caves",
        "Famous Musician",
        "Fasting",
    ),
)


@dataclass
class Oasis:
    the_water: str
    whats_there: str
    whos_there: str
    custom: str

    def __repr__(self):
        return f"""The water is {self.the_water.capitalize()}, and there are {self.whats_there.lower()} here..
        <br>
        {self.whos_there.capitalize()} are present.
        <br>
        The custom is: {self.custom.lower()}.
        """


def gen_oasis():
    the_water = choice(line[0] for line in oasis_data)
    what = sample([line[1] for line in oasis_data], 2)
    who = sample([line[2] for line in oasis_data], 2)
    custom = choice(line[3] for line in oasis_data)
    what = " and ".join(what)
    who = " and ".join(who)
    return Oasis(the_water=the_water, whats_there=what, whos_there=who, custom=custom)
