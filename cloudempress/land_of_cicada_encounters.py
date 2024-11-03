regions = ["The Breadbasket", "The Weeds", "The Thickwood", "The Rustbucket"]

breadbasket_encounters = {
    25: "Nothing",
    40: "1d10 Farmerling Harvesters",
    50: "1d10 Farmerling Militia Members",
    60: "2d10 Cloudling Soldiers",
    70: "A Trading Courier",
    80: "1d10 Spore keepers",
    84: "1d5 Couriers carrying corpses in funeral urns",
    88: "1d10 Juvenile Imago",
    91: "1d5 Full-grown Imago",
    94: "Spore Keepers searching for Spike Head (pg. 18), who is hiding nearby.",
    97: "The Headcutter (pg. 16)",
    99: "The Cloud Empress in disguise with her bodyguard Skull (pg. 40)",
}

weeds_encounters = {
    25: "Nothing",
    40: "2d10 Cloudling soldiers",
    50: "2d10 Saboteurs of the Order of the Broken Bread",
    60: "1d5 Wanderlings",
    70: "2d10 Full grown Imago",
    80: "2d10 Huskers",
    84: "A trading Courier",
    88: "1d5 Cloudling deserters",
    91: "2d10 Cloudling commandos",
    94: "1d10 Cloudling soldiers vomiting blue liquid",
    97: "Prince Bug and 1d100 Imago (pg. 34)",
    99: "The Cloud Empress in disguise with her bodyguard Skull (pg. 40)",
}

thickwood_encounters = {
    25: "Nothing",
    40: "2d10 Full grown Imago",
    50: "1d10 Brood Monks",
    60: "1d10 Big game hunters",
    70: "1d10 Wild packsquabs",
    80: "1d5 Ancient Imago",
    84: "3d10 Imago Nymphs",
    88: "2d10 Cloudling explorers",
    91: "A Hermit",
    94: "A lost Courier",
    97: "1d100 Juvenile Imago",
    99: "The Cloud Empress in disguise with her bodyguard Skull (pg. 40)",
}


rustbucket_encounters = {
    25: "Nothing",
    40: "3d10 Disposables",
    50: "2d10 servitors",
    60: "1d100 crabrats",
    70: "1d10 Sellsword treasure hunters",
    80: "A trading Courier",
    84: "2d10 Disposables in religious reverie",
    88: "1d10 Farmerling scrappers",
    91: "1d5 full grown Imago destroying their surroundings with telekinesis",
    94: "Oola (pg. 44) vainly searching for signs of the Bone-skin giants",
    97: "Vanni (pg. 50) speaking sympathetically to some long-dead proxies he’s murdered",
    99: "Vanni (pg. 50) supervising the work of oblivious Disposables",
}


cloud_empress_encounters = {
    regions[0]: breadbasket_encounters,
    regions[1]: weeds_encounters,
    regions[2]: thickwood_encounters,
    regions[3]: rustbucket_encounters,
}


moods = (
    "Generous",
    "Friendly",
    "Curious",
    "Needy",
    "Disinterested",
    "Wary",
    "Afraid",
    "Defensive",
    "Aggressive",
    "Cruel",
)
