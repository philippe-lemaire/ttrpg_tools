import random
from .roll import find_key
from dataclasses import dataclass

colony_details = {
    1: (
        "Motifs élaborés tracés dans la fourrure",
        "Labyrinthe de tunnels défensifs, piégés",
        "Désastre, tous se préparent à partir",
        "Paysans aux cultures très hautes",
    ),
    2: (
        "Sous l'emprise de plantes étranges",
        "Auberge confortable et bien équipée",
        "Mariage, les rues jonchées de fleurs",
        "Bûcherons avec scies et baudriers",
    ),
    3: (
        "Refusent de traiter avec des étrangers",
        "Chapelle taillée dans un bois noir",
        "Préparation d’une grande fête",
        "Pêcheurs rudes et balafrés, avec filets et frêles esquifs",
    ),
    4: (
        "Avides de nouvelles du lointain",
        "Jardin aux champignons, pour méditer",
        "Une épidémie s'est répandue",
        "Champignonnières sombres et humides",
    ),
    5: (
        "Une fourrure soignée porte malheur",
        "Crâne de bœuf, investi par une guilde",
        "Entrepôt est envahi d'insectes",
        "Grains séchant sur toutes les surfaces planes",
    ),
    6: (
        "Portent des habits finement brodés",
        "Un fouillis de taudis très serrés",
        "Jour de marché, fermiers en nombre",
        "Fromages forts, affinés pendant plusieurs saisons",
    ),
    7: (
        "Affinent des années un fromage fort",
        "Des maisons en bois suspendues",
        "Les souris se sautent à la gorge",
        "Jardins remplis d'herbes rares. Les espaces de séchage sont sous bonne garde.",
    ),
    8: (
        "Visages cachés par des capuches",
        "Portail orné, gardé par des statues",
        "Groupe se forme pour attaquer une bête",
        "Ruches et apiculteurs sous camail.",
    ),
    9: (
        "Appauvris par la dîme du seigneur chat",
        "Temple secret du culte chauve-souris",
        "Des enfants ont disparu",
        "Marchands et commerçants ayant souvent besoin de protection",
    ),
    10: (
        "Coupent rituellement leur queue",
        "Perchoir de pigeonnier",
        "Un noble fait une demande frivole",
        "Tailleurs de pierre, les pierres viennent d’une carrière proche",
    ),
    11: (
        "Chassent de grandes bêtes",
        "Entrepôt, rempli de conserves",
        "Troupe de théâtre itinérante arrive",
        "Moulin à farine activé par une large roue à eau",
    ),
    12: (
        "Parents d’une même matriarche",
        "Dock caché pour bateaux fluviaux",
        "Funérailles, rues recouvertes de fumée",
        "Mine de fer, d'argent ou d’étain",
    ),
    13: (
        "Cuisinent d'excellentes tartes",
        "Moulin à laine, pales en tissu éclatant",
        "Arnaqueur prépare un grand coup",
        "Élevage de vers à soie et travail de la soie",
    ),
    14: (
        "Echappés d'un laboratoire, naïfs",
        "Une machine humaine, en service",
        "Scarabée dressé devient fou",
        "Tunneliers et explorateurs des souterrains",
    ),
    15: (
        "Paressent au bord de l’eau",
        "Un pont en bois rejoint la colonie ",
        "Requête impossible d'une émissaire fée",
        "Poterie cuite au four aux couleurs joyeuses",
    ),
    16: (
        "Experts en exploration de grottes",
        "Tour tortueuse incroyablement haute ",
        "Plante à croissance rapide tout près",
        "Travail de la laine aux couleurs vives",
    ),
    17: (
        "Creusent de gigantesques tunnels",
        "Magnifique jardin fleuri ",
        "Un héritage précieux a été volé",
        "Excellente école mais enfants turbulents",
    ),
    18: (
        "Elèvent des vers à soie",
        "Moulin à aubes ",
        "Seigneur chat demande une lourde dîme",
        "Un marché très animé",
    ),
    19: (
        "Connus pour leurs écoles",
        "Statue d'un héros passé, à l'abandon ",
        "Menace humaine imminente et mortelle",
        "Une pile d'ordure puante patiemment explorée",
    ),
    20: (
        "En bons termes avec un prédateur",
        "Marché florissant ",
        "Tour de sorcier arrive, à dos de tortue",
        "Ébenisterie, magnifique mobilier de bois précieux",
    ),
}


name_prefixes = [
    "Chêne",
    "Baie",
    "Saule",
    "Souche",
    "Pin",
    "Lune",
    "Vert",
    "Noir",
    "Pierre",
    "Colline",
    "Figue",
    "Pomme",
    "Marais ",
    "Chouette ",
    "Renard ",
    "Gland",
    "Cuivre ",
    "Voleur",
    "Tomme",
    "Fosse",
    "Rose",
    "Cuivre ",
    "Cher",
    "Tronc",
]


name_suffixes = [
    "mas",
    "ville",
    "moulin",
    "vallon",
    "bois",
    "cité",
    "val",
    "source",
    "cendre",
    "buisson",
    "point",
    "éclat",
    "fort",
    "colline",
    "tour",
    "ferme",
    "pont",
    "porte",
    "crique",
    "mare",
    "nid",
    "gué",
    "tombe",
    "feu",
]


colony_size = {
    1: "Ferme/Manoir (1-3 familles)",
    2: "Croisement (3-5 familles)",
    3: "Hameau (50-150 souris)",
    4: "Village (150-300 souris)",
    5: "Ville (300-1000 souris)",
    6: "Cité (1000+ souris)",
}


def roll_colony_size():
    rolls = [random.randint(1, 6) for die in range(2)]
    kept = min(rolls)
    return colony_size.get(kept), kept


governance_types = {
    2: "Les Doyens de la Communauté servent de guides",
    4: "La communauté est dirigée par un Chevalier, ou un noble mineur",
    6: "La Communauté est dirigée par une guilde",
    8: "Communauté libre, gouvernée par un conseil de souris des villes",
    10: "Communauté dirigée par une famille noble",
    12: "La Communauté est le siège d’une Baronie",
}

tavern_names_a = [
    "Blanc·he",
    "Vert·e",
    "Noir·e",
    "Rouge",
    "Argenté·e",
    "Tordu·e",
    "Amical·e",
    "Caché·e",
    "Rusé·e",
    "de Verre",
    "Épineux·se",
    "Cassé·e",
]

tavern_names_b = [
    "Le Scarabée",
    "Le Renard",
    "Le Coin",
    "Le Noyau",
    "Le Rat",
    "Le Fromage",
    "L'Aigle",
    "Le Ver",
    "L'Abeille",
    "La Lanterne",
    "La Rose",
    "Le Chevalier",
]

tavern_specialties = [
    "Carottes épicées",
    "Bouillon de ver de terre",
    "Tarte aux myrtilles",
    "Fromage au goût âcre",
    "Bouillie d’orge",
    "Steak de poisson de rivière",
    "Pommes cuites",
    "Émietté de pattes d'insectes frites",
    "Tartines beurrées de pain frais",
    "Bonbons trouvés",
    "Graines grillées au miel",
    "Ragoût de champignons",
]


@dataclass
class Colony:
    inhabitants: str
    element_of_note: str
    event: str
    industry: str
    name: str
    size: str
    governance: str
    tavern_name: str
    tavern_specialty: str


def generate_colony_obj():
    inhabitants, element_of_note, event, industry = [
        colony_details.get(random.randint(1, 20))[n] for n in range(4)
    ]
    name = f"{random.choice(name_prefixes)} {random.choice(name_suffixes)}"
    size, rolled_size = roll_colony_size()
    governance_roll = random.randint(1, 6) + rolled_size
    governance = governance_types.get(find_key(governance_roll, governance_types))
    tavern_name = f"{random.choice(tavern_names_b)} {random.choice(tavern_names_a)}"
    tavern_specialty = random.choice(tavern_specialties)
    return Colony(
        inhabitants,
        element_of_note,
        event,
        industry,
        name,
        size,
        governance,
        tavern_name,
        tavern_specialty,
    )


if __name__ == "__main__":
    print(generate_colony_obj())
