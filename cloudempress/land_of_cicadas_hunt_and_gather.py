from .land_of_cicada_encounters import regions
from .roll import roll_d10, get_key

breadbasket_data = {
    "provisions": {
        1: 3,
        5: 2,
        8: 1,
        10: "Nothing",
    },
    "good_food_and_drink": {
        1: "Rock candy (2 servings) ",
        2: "Loaf of freshly baked sourdough bread (6 servings)",
        3: "Heirloom tomatoes (4 servings)",
        4: "Mixed berry pie (5 servings)",
        5: "Farm eggs (x6)",
        6: "Grape cider (4 servings)",
        7: "Two pounds of white cheese (3 servings)",
        8: "Hen-duck meat (5 servings)",
        10: "Nothing",
    },
    "shelter": {
        1: "Empty grain silo (safe)",
        2: "Barn full of packsquabs (safe)",
        3: "Waystation (safe)",
        4: "Ancient tractor (safe)",
        5: "Vacant camper (safe)",
        6: "Windmill",
        7: "Cornfield",
        8: "Ditch",
        10: "Nothing",
    },
}

weeds_data = {
    "provisions": {
        1: 3,
        3: 2,
        7: 1,
        10: "Nothing",
    },
    "good_food_and_drink": {
        1: "Prairie turcken (2 servings)",
        2: "Military chocolate (6 servings) ",
        3: "Fried potato wedges (6 servings)",
        4: "Silver dollar pancakes x10 (4 servings) ",
        5: "Instant coffee (12 servings)",
        6: "Boar beef sausages (3 servings)",
        7: "River Catfish (3 servings)",
        10: "Nothing",
    },
    "shelter": {
        1: "Bunker (safe)",
        2: "Abandoned tank (safe)",
        3: "Farmhouse (safe)",
        4: "Collapsing barn",
        5: "Thopter wreck",
        6: "Trench",
        7: "Crater hole",
        10: "Nothing",
    },
}
thickwood_data = {
    "provisions": {
        2: 3,
        6: 2,
        9: 1,
        10: "Nothing",
    },
    "good_food_and_drink": {
        1: "Apples (6 savings)",
        2: "Shrine cake (2 servings)",
        3: "Deer-dog meat (12 servings)",
        4: "Molasses (2 servings)",
        5: "Psychedelic mushrooms (2 servings) ",
        6: "Crawdads (2 servings) ",
        7: "Wild forest turcken (3 servings) ",
        8: "Catfish (2 servings)",
        9: "Fresh greens (3 servings)",
        10: "Nothing",
    },
    "shelter": {
        1: "Hermit’s hole (safe)",
        2: "Giant roots (safe)",
        3: "Ancient Imago husk (safe)",
        4: "Empty skull of a giant (safe)",
        5: "Massive hollow tree (safe)",
        6: "Brood monk shrine",
        7: "Creek-bed",
        8: "Imago hole",
        9: "Open palm of a giant",
        10: "Nothing",
    },
}

rustbucket_data = {
    "provisions": {
        2: 3,
        6: 2,
        7: 1,
        10: "nothing",
    },
    "good_food_and_drink": {
        1: "dehydrated snack cakes (2 servings)",
        2: "container of chocolate syrup (7 servings) ",
        3: "crabrat (8 servings) ",
        4: "wild onion (2 servings) ",
        5: "lemon (1 serving) ",
        6: "salad greens (3 servings)",
        7: "teabags (10 servings)",
        10: "nothing",
    },
    "shelter": {
        1: "abandoned apartment (safe)",
        2: "collapsed tower (safe)",
        3: "storage unit (safe)",
        4: "transportation tunnel (safe)",
        5: "factory line",
        6: "sewer",
        7: "bushes",
        10: "nothing",
    },
}


data = {
    regions[0]: breadbasket_data,
    regions[1]: weeds_data,
    regions[2]: thickwood_data,
    regions[3]: rustbucket_data,
}


class Hunt_and_gather_result:
    def __init__(self, region):
        d = data.get(region)
        self.provisions = d["provisions"][get_key(roll_d10(), d["provisions"])]
        self.good_food_and_drink = d["good_food_and_drink"][
            get_key(roll_d10(), d["good_food_and_drink"])
        ]
        self.shelter = d["shelter"][get_key(roll_d10(), d["shelter"])]
