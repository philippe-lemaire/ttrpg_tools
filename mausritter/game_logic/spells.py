from dataclasses import dataclass
from .roll import roll


spells = {
    2: (
        "Boule de feu",
        "Lance une boule de feu jusqu’à 60cm. Inflige [SOMME]+[DÉS] dommages aux créatures à 15cm.",
        "Au cœur d’un brasier intense pendant trois jours et trois nuits.",
    ),
    3: (
        "Soins",
        "Soigne [SOMME] dommages en FOR et retire la condition Blessée à une créature.",
        "Se couper pour d6 dommages en FOR, et recouvrir de ce sang.",
    ),
    4: (
        "Projectile magique",
        "Inflige [SOMME]+[DÉS] dommages à une créature visible.",
        "Faire une chute d’au moins 10m. Toucher le sort pendant un tour.",
    ),
    5: (
        "Effroi",
        "Donne la condition Effroi à [DÉS] créatures.",
        "Recevoir la condition Effroi par une créature hostile alors que l’on porte le sort.",
    ),
    6: (
        "Ténèbres",
        "Crée une sphère de pures ténèbres d’un diamètre de [SOMME]x5cm pour [DÉS] tours.",
        "Rester à découvert dans un endroit sans lumière pendant trois jours.",
    ),
    7: (
        "Restauration",
        "Retire la condition Fatiguée ou Effrayée à [DÉS]+1 créatures.",
        "Enterrer dans un champ tranquille ou un lit de rivière pendant trois jours.",
    ),
    8: (
        "Compréhension",
        "Deviens compréhensible pour [DÉS] créatures d’une autre espèce pendant [DÉS] tours.",
        "Donner sans contrainte le sort à une créature d’une autre espèce.",
    ),
    9: (
        "Scarabée fantôme",
        "Crée une illusion de scarabée qui peut porter 6 cases d’inventaires pour [DÉS]x6 tours.",
        "Enterrer dans un cimetière de scarabées pendant trois nuits.",
    ),
    10: (
        "Lumière",
        "Force [DÉS] créatures à faire une sauvegarde de VOL pour ne pas être sonnées. Sinon, peut aussi créer l’équivalent d’une torche pour [SOMME] tours.",
        "L’exposer à la première lumière du jour, et aux dernier rayon de soleil de trois jours consécutifs.",
    ),
    11: (
        "Cercle invisible",
        "Crée un cercle de force de [DÉS]x15cm.  Invisible et inamovible.",
        "Former un cercle de fer aussi large que le dernier lancement du sort. Passer le sort à travers. Dissoudre le cercle.",
    ),
    12: (
        "Toc Toc",
        "Ouvre une porte ou un contenant, comme si une sauvegarde de FOR de 10+([DÉS]x4) avait été réussie.",
        "Enfermer dans une boîte verrouillée, elle-même dans une boîte verrouillée, elle aussi dans une boîte verrouillée. Laisser pendant trois jours.",
    ),
    13: (
        "Graisse",
        "Couvre une zone de [DÉS]x15cm d’une graisse glissante et inflammable. Une sauvegarde de DEX est requise pour ne pas tomber.",
        "Recouvrir de graisse animale. Attendre la putréfaction.",
    ),
    14: (
        "Croissance",
        "Augmente la taille d’une créature [DÉS]+1 fois pour un tour.",
        "Laisser dans les plus hautes branches d’un grand arbre pour trois jours.",
    ),
    15: (
        "Invisibilité",
        "Rend une créature invisible pour [DÉS] tours.  Tout mouvement diminue la durée d’un tour.",
        "Tenir le sort pendant une journée, sans jamais ouvrir les yeux.",
    ),
    16: (
        "Herbe à chat",
        "Rend un objet totalement irrésistible pour les chats. Dure [DÉS] tours.",
        "Donner à un chat un présent qu’il désire vraiment.",
    ),
}


@dataclass
class Spell:
    name: str
    effect: str
    recharge: str

    def __str__(self):
        return f"Le sort {self.name}. Effet : {self.effect} Recharge : {self.recharge}"


def generate_spell_obj():
    name, effect, recharge = spells.get(roll("2d8"))
    return Spell(name, effect, recharge)


def get_spell_list():
    return [Spell(*data) for data in spells.values()]
