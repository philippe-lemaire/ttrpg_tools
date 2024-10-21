import random
from dataclasses import dataclass


@dataclass
class MagicSword:
    weapon_class_name: str
    weapon_class_description: str
    image_num: int
    material: str
    effect_condition: str
    effect_text: str
    cursed: bool
    curse: str
    curse_lifted_by: str

    def __str__(self):
        if not self.cursed:
            return f"Une épée magique faite en {self.material}, de type {self.weapon_class_name}. Effet spécial : {self.effect_condition} : {self.effect_text}"
        else:
            return f"Une épée maudite faite en {self.material}, de type {self.weapon_class_name}. Malédiction : {self.curse}Levée si {self.curse_lifted_by} Après avoir levé la malédiction : {self.effect_condition} : {self.effect_text}"


def generate_magic_sword_obj():
    medium = ("Moyenne", "(d6, patte directrice, ou d8, 2 pattes)")
    weapon_classes = {}
    for k in range(1, 5):
        weapon_classes[k] = medium

    weapon_classes[5] = ("Légère", "(d6, 1 patte, patte directrice/ patte opposée)")
    weapon_classes[6] = ("Lourde", "(d10, 2 pattes)")
    weapon_material_and_effect = (
        (
            "fer forgé",
            "quand tenue",
            "vous lancez les sauvegardes de coups critiques avec Avantage.",
        ),
        (
            "conception féérique complexe",
            "quand tenue",
            "vous pouvez vous déguiser en n'importe quelle créature de la taille d'une souris.",
        ),
        ("clou rouillé", "dégâts critiques", "vous infligez la condition Effroi."),
        ("croc de serpent", "dégâts critiques", "vous infligez d6 dégâts à la DEX."),
        (
            "sabre de soldat de plomb",
            "quand tenue",
            "si vous menez une troupe de souris, elles ont toutes +1 armure.",
        ),
        (
            "verre poli",
            "quand tenue",
            "vous pouvez retenir votre respiration sous l'eau pendant 1 tour.",
        ),
        (
            "dent de loup",
            "dégâts critiques",
            "votre prochaine attaque est améliorée (d12 dégâts).",
        ),
        (
            "aiguille à coudre en argent",
            "dégâts critiques",
            "retirer toute l’usure d'un de vos objets (hors sorts).",
        ),
        ("tige de rosier", "dégâts critiques", "retirez une condition."),
        (
            "ombre congelée",
            "quand tenue",
            "vous êtes invisible si vous restez parfaitement immobile.",
        ),
    )
    curses = (
        (
            "lancez les sauvegardes contre dégâts critiques avec Désavantage.",
            "faites un sacrifice désintéressé en mettant votre vie en danger.",
        ),
        (
            "quand vous devenez Épuisé, prenez la condition 2 fois.",
            "Prenez la place d’un pauvre fermier pendant une saison.",
        ),
        (
            "quand vous êtes menacé·e, réussissez un jet de VOL, ou bien vous attaquez.",
            "faites la paix avec un ennemi mortel.",
        ),
        (
            "-1 sur les jets de réaction des rencontres.",
            "donnez toutes vos possessions, sans tricher.",
        ),
        (
            "quand vous voyez un allié prendre des dégâts, prenez la condition Effroi.",
            "Exaucez le vœu d’une souris mourante.",
        ),
        (
            "Les sorts lancés en votre présence marquent toujours un usage.",
            "détruisez la source du pouvoir d'un sorcier hibou.",
        ),
    )
    weapon_class_name, weapon_class_description = weapon_classes.get(
        random.randint(1, 6)
    )
    image_num = random.randint(1, 10)
    material, effect_condition, effect_text = weapon_material_and_effect[image_num - 1]
    cursed_roll = random.randint(1, 6)
    cursed = cursed_roll == 6
    if cursed:
        curse, curse_lifted_by = random.choice(curses)
    else:
        curse, curse_lifted_by = "", ""

    return MagicSword(
        weapon_class_name,
        weapon_class_description,
        image_num,
        material,
        effect_condition,
        effect_text,
        cursed,
        curse,
        curse_lifted_by,
    )
