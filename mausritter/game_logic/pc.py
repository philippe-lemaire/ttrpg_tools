import random
from .roll import roll
from .weapons import weapons
from .npc import first_names, last_names, signs, dispositions

past = {
    1: {
        1: (
            "Sujet d'expériences",
            "Sort: Projectile magique",
            "Plaque de plomb (Arm. lourde)",
        ),
        2: ("Commise de cuisine", "Blouson & Bouclier (Arm. légère) ", "Casseroles"),
        3: ("Souris domestiquée", "Sort: Se faire comprendre", "Bouteille de lait"),
        4: ("Sorcière des buissons", "Sort: Soins", "Ciseaux"),
        5: ("Maroquinière", "Blouson & Bouclier (Arm. légère) ", "Ciseaux"),
        6: ("Dure à cuire", "Dague (Légère, d6)", "Flasque de café"),
    },
    2: {
        1: ("Prêtresse mendiante", "Sort: Restauration", "Symbole sacré"),
        2: ("Joueuse", "Dés pipés", "Dague (Légère, d6)"),
        3: ("Scarabergère", "Employé: Scarabée loyal", "Perche, 15cm"),
        4: ("Pêcheuse", "Filet", "Aiguille (Légère, d6)"),
        5: ("Forgeronne", "Marteau (Moyenne, d6/d8)", "Lime métallique"),
        6: ("Câbleuse", "Câble, bobine", "Lanterne électrique"),
    },
    3: {
        1: ("Bûcheronne", "Hache (Moyenne, d6/d8)", "Ficelle, pelote"),
        2: (
            "Sectatrice de la Chauve-Souris ",
            "Sort: Ténèbres ",
            "Sac de dents de chauve-souris",
        ),
        3: ("Mineuse d'étain", "Pioche (Moyenne, d6/d8)", "Lanterne"),
        4: ("Ramasseuse d'ordures", "Crochet à ordures (Lourd, d10)", "Miroir"),
        5: ("Rôdeuse des murs", "Hameçon", "Fil, bobine"),
        6: ("Marchande", "Employé: Porteur rat", "Dette de 20p venant d'un noble"),
    },
    4: {
        1: ("Sapeuse", "Marteau (Moyenne, d6/d8)", "Pieux en bois"),
        2: ("Dresseuse de ver", "Perche, 15cm", "Savon"),
        3: ("Chevaucheuse de moineau", "Hameçon", "Lunettes"),
        4: ("Guide des égouts", "Lime métallique", "Fil, bobine"),
        5: ("Gardienne de prison", "Chaînes, 15cm", "Lance (Lourd, d10)"),
        6: (
            "Cultivatrice de champignons ",
            "Cèpes séchés (comme rations) ",
            "Masque à spores",
        ),
    },
    5: {
        1: ("Constructrice de barrages", "Pelle", "Pieux en bois"),
        2: ("Cartographe", "Encre & plume", "Compas"),
        3: ("Voleuse de pièges", "Morceau de fromage", "Colle"),
        4: ("Vagabonde", "Tente", "Carte au trésor, douteuse"),
        5: ("Céréalicultrice", "Lance (Lourde, d10)", "Sifflet"),
        6: ("Messagère", "Sac de couchage", "Documents, scellés"),
    },
    6: {
        1: ("Troubadour", "Instrument de musique", "Miroir"),
        2: ("Brasseuse", "Petit baril de bière", "Jeu de dés pipés"),
        3: ("Tireuse de sève", "Seau", "Pieux en bois"),
        4: ("Apicultrice", "Pot de miel", "Filet"),
        5: ("Bibliothécaire", "Extrait d'un livre obscur", "Encre & Plume"),
        6: ("Noble sans-le-sou", "Chapeau en feutrine", "Parfum"),
    },
}

colors = (
    "Chocolat",
    "Noir",
    "Blanc",
    "Brun",
    "Gris",
    "Bleu",
)


patterns = (
    "uni",
    "à rayures",
    "irrégulier",
    "en bandes",
    "marbré",
    "moucheté",
)

physical_traits = (
    "Cicatrices",
    "Fourrure entretenue",
    "Corpulente",
    "Dreadlocks",
    "Squelettique",
    "Fourrure teinte",
    "Filiforme",
    "Fourrure rasée",
    "Petite",
    "Fourrure frisée",
    "Massive",
    "Fourrure soyeuse",
    "Peintures de guerre",
    "Yeux d’ébène",
    "Habits étrangers",
    "Cache-Œil",
    "Habits élégants",
    "Yeux rouges",
    "Habits rapiécés",
    "Regard sage",
    "Habits de mode",
    "Regard vif",
    "Habits sales",
    "Regard lumineux",
    "Oreille manquante",
    "Queue coupée",
    "Visage grumeleux",
    "Queue-fouet",
    "Joli visage",
    "Queue touffue",
    "Visage rond",
    "Queue épaisse",
    "Visage délicat",
    "Queue préhensile",
    "Visage allongé",
    "Queue tordue",
)


def roll_stat():
    rolls = [random.randint(1, 6) for die in range(3)]
    rolls.remove(min(rolls))
    return sum(rolls)


class Mouse_PC:
    def __init__(self, name):
        self.name = name
        self.STR = roll_stat()
        self.DEX = roll_stat()
        self.WIL = roll_stat()
        self.pips = roll("d6")
        self.HP = roll("d6")
        sign_roll = random.randint(0, 5)
        self.sign = signs[sign_roll]
        self.disposition = dispositions[sign_roll]

        past_items = past.get(self.HP).get(self.pips)[1:]
        self.inventory = list(past_items)
        self.inventory.extend(("Torche", "Rations"))
        self.background = past.get(self.HP).get(self.pips)[0]

        alternative_past_items = past.get(random.randint(1, 6)).get(
            random.randint(1, 6)
        )[1:]
        best_stat = max(self.STR, self.DEX, self.WIL)
        if best_stat <= 7:
            self.inventory.extend(alternative_past_items)

        elif best_stat <= 9:
            chosen_item = random.choice(alternative_past_items)
            self.inventory.append(chosen_item)

        self.fur = f"{random.choice(colors)} {random.choice(patterns)}"
        self.physical_trait = random.choice(physical_traits)

    def __repr__(self):
        return f"{self.name}. {self.STR=} {self.DEX=} {self.WIL=} {self.HP=} {self.pips=} {self.background} {self.inventory=}"


def generate_mouse_pc_obj():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return Mouse_PC(name)
