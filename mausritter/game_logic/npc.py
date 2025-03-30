import random
from .roll import roll

first_names = [
    "Absinthe",
    "Achillée",
    "Ada",
    "Agapanthe",
    "Agate",
    "Agnès",
    "Aloès",
    "Andromède",
    "April",
    "Argémone",
    "Armoise",
    "Azalée",
    "Bardane",
    "Belladonna",
    "Brie",
    "Brynn",
    "Cassiopée",
    "Cerise",
    "Citronnelle",
    "Claire",
    "Dahlia",
    "Dauphinelle",
    "Elsa",
    "Émeraude",
    "Érin",
    "Fraise",
    "Genièvre",
    "Grace",
    "Gwendoline",
    "Iris",
    "Jacinthe",
    "Lavande",
    "Lila",
    "Magnolia",
    "Marguerite",
    "Marjolaine",
    "Minnie",
    "Noisette",
    "Odette",
    "Olive",
    "Opale",
    "Perle",
    "Rita",
    "Rose",
    "Safran",
    "Sandy",
    "Sassafras",
    "Suzanne",
    "Violette",
    "Yeuse1. ",
    "Acacia",
    "Albert",
    "Algernon",
    "Ambroise",
    "Aneth",
    "Anis",
    "Antonio",
    "Arsène",
    "Aubépin",
    "Auguste",
    "Basile",
    "Béric",
    "Bill",
    "Boldo",
    "Bourgeon",
    "Brie",
    "Café",
    "Cassien",
    "Clive",
    "Colby",
    "Corné",
    "Demi-sel",
    "Edmond",
    "Elmer",
    "Ernest",
    "Estragon",
    "Fenouil",
    "Festus",
    "Fievel",
    "Francis",
    "Gaspard",
    "Gilles",
    "Horace",
    "Jacques",
    "Konrad",
    "Laurel",
    "Laurier",
    "Lorenz",
    "Mich",
    "Nuphar",
    "Oliver",
    "Orin",
    "Pavot",
    "Poivre",
    "Ripitchip",
    "Robin",
    "Séneçon",
    "Simon",
    "Stilton",
    "Warren",
]

last_names = [
    "Blanc",
    "Cerf-volant",
    "Confiseur",
    "Danger",
    "Dindon",
    "Faiseur",
    "Froid d’hiver",
    "Météo",
    "Monnaie",
    "Neige",
    "Nœuds",
    "Noir",
    "Pêcheur",
    "Pépite",
    "Piquant",
    "Semeur",
    "Soleil d’été",
    "Taquine-chat",
    "Tunnelier",
    "Voltigeur",
]
signs = [
    "de l’Étoile",
    "de la Roue",
    "du Gland",
    "de la Tempête",
    "de la Lune",
    "de la Mère",
]
dispositions = [
    "Brave/Imprudente",
    "Travailleuse/Sans imagination",
    "Indiscrète/Têtue",
    "Généreuse/Irascible",
    "Sage/Mystérieuse",
    "Réconfortante/Inquiète",
]


class NPC_Mouse:
    def __init__(self):
        # name
        self.first_name = random.choice(first_names)
        self.last_name = random.choice(last_names)
        self.name = f"{self.first_name} {self.last_name}"
        # social position and price
        social_positions = [
            "Pauvre",
            "Commune",
            "Commune",
            "Souris des Bourgs",
            "Souris des Guildes",
            "Souris noble",
        ]
        payments = [
            roll("d6"),
            10 * roll("d6"),
            10 * roll("d6"),
            50 * roll("d6"),
            100 * roll("d4"),
            1000 * roll("d4"),
        ]
        social_index = random.randint(0, 5)
        self.social_position = social_positions[social_index]
        self.payment = f"{payments[social_index]}p"
        # birthsign

        sign_index = random.randint(0, 5)
        self.sign = signs[sign_index]
        self.dispositions = dispositions[sign_index]
        # details
        details = {
            1: ["Regard mélancolique", "Toilettage constant", "Liberté", "Parent"],
            2: [
                "Habits clairs et rapiécés",
                "Obsédée par la météo",
                "Sécurité",
                "Frère/Sœur",
            ],
            3: ["Couronne de marguerites", " Très énergique", "Fuite", "Cousine"],
            4: [
                "Vêtements sales",
                "A voyagé, très instruite",
                "Excitation",
                "Cousine au 2ème degré",
            ],
            5: [
                "Grand chapeau souple",
                "Maudit par un sorcier",
                "Pouvoir",
                "Grand-parent",
            ],
            6: [
                "Graines plein les poches",
                "S'effraie facilement",
                "Sens",
                "lien de parenté, mais ne le sait pas",
            ],
            7: ["Bâton de marche", "Honte d'anciens crimes", "Santé", "Mariée"],
            8: [
                "Porte une épée rouillée",
                "Aime la compétition",
                "Richesse",
                "Anciens amants",
            ],
            9: [
                "Fourrure rebelle",
                "Ivrogne flamboyant",
                "Protection",
                "Amour, à sens unique",
            ],
            10: ["Très, très vieux", "Très poli", "Amour", "Pote de bistro"],
            11: ["Queue bandée", "Honnête sans réserve", "Protéger", "A une dette"],
            12: [
                "Un nœud à la queue",
                "Discours lent, soigné",
                "Nourriture",
                "Longue et tumultueuse",
            ],
            13: [
                "Oreille manquante",
                "Discours rapide, décousu",
                "Amitié",
                "Ennemies jurées",
            ],
            14: [
                "Longues moustaches",
                "Serviteur secret d'un chat",
                "Repos",
                "Sœurs de Guilde",
            ],
            15: [
                "Cligne des yeux",
                "Elevée par des rats",
                "Connaissance",
                "Amies d'enfance",
            ],
            16: [
                "Lourde cape noire",
                "Exilée de chez elle",
                "Sauvagerie",
                "L'une a volé à l'autre",
            ],
            17: [
                "Cicactrices de guerre",
                "Dresse des insectes",
                "Beauté",
                "Ont travaillé ensemble",
            ],
            18: [
                "Très jeune",
                "Déteste être dehors",
                "Vengeance",
                "Ont grandi ensemble",
            ],
            19: [
                "Fourrure rasée",
                "Héros local",
                "Servir",
                "Ont servi le même seigneur",
            ],
            20: ["Fourrure tressée", "Moustaches agitées", "Fun", "Parfaite inconnue"],
        }
        self.appearance = details.get(roll("d20"))[0]
        self.quirk = details.get(roll("d20"))[1]
        self.wants = details.get(roll("d20"))[2]
        self.relationship = details.get(roll("d20"))[3]

    def __repr__(self):
        return f"Nom : {self.first_name} {self.last_name}.\nApparence: {self.appearance}.\nParticularité : {self.quirk}.\nDésir : {self.wants}.\nRang : {self.social_position}. Prix des services : {self.payment}.\nSigne : {self.sign}. Disposition : {self.dispositions}.\nRelation : {self.relationship}."


hireling_stats = (
    ("Porteur de torche", "d6", "1p"),
    (
        "Ouvrier",
        "d6",
        "2p",
    ),
    (
        "Tunnelier",
        "d4",
        "5p",
    ),
    (
        "Forgeron",
        "d2",
        "8p",
    ),
    (
        "Guide local",
        "d4",
        "10p",
    ),
    (
        "Soldat",
        "d6",
        "10p",
    ),
    (
        "Érudit",
        "d2",
        "20p",
    ),
    (
        "Chevalier",
        "d3",
        "25p",
    ),
    (
        "Interprète",
        "d2",
        "30p",
    ),
)


class Hireling(NPC_Mouse):
    def __init__(self):
        super(Hireling, self).__init__()
        self.name = random.choice(first_names)
        self.STR = roll("2d6")
        self.DEX = roll("2d6")
        self.WIL = roll("2d6")
        self.HP = roll("1d6")

    def __repr__(self):
        return f"Recrue appelée {self.name} avec {self.HP} PV, FOR {self.STR}, DEX {self.DEX}, VOL {self.WIL}. {self.quirk}"


if __name__ == "__main__":
    print(NPC_Mouse())
