import random
from .roll import find_key
from .magic_sword import generate_magic_sword_obj
from .spells import generate_spell_obj


slots = "emplacements d’inventaire"

trinkets = (
    "Lanterne à fantôme (émet une lumière qui chasse les fantômes)",
    "Coquillages parlants (l’un dit ce que l’autre entend)",
    "Paille à air (un tube qui contient toujours de l’air)",
    "Dague de membre du culte des chauves-souris (permet d’entrer dans leur repaire)",
    "Haricots magiques (pousse totalement en 6 Tours)",
    "Appareil humain et état de marche (inventez quelque-chose de marrant)",
)

valuable_treasure = (
    "Meule de fromage affiné (100p)",
    f"Chaîne en argent (2 {slots}, 500p)",
    "Bijou de pendentif (400p)",
    "Bague en or (500p)",
    "Diamand poli (1000p)",
    f"Collier de perles (2 {slots}, 1500p)",
)

unusual_treasure = (
    "Paquet d’herbes âcres (200p chez un apoticaire",
    "Champignons séchés de couleur bizarre (200p chez une sorcière)",
    "Pierre étrangement brillante (300p chez un sorcier)",
    "Bijou de famille ayant une valeur sentimentale pour une souris noble",
    "Acte de propriété pour un terrain",
    "Carte au trésor",
)

large_treasure = (
    f"cuillère en argent géante (2 {slots}, 300p)",
    f"Peigne en ivoire (4 {slots}, 400p)",
    f"Grande bouteille de liqueur (4 {slots}, 500p)",
    f"Statue de Souris Ancienne (4 {slots}, 500p)",
    f"Trone de Souris Ancienne (6 {slots}, 1000p)",
    f"Montre en or (4 {slots}, 1000p)",
)

useful_treasure = (
    f"{random.randint(1,6)} rations, bien conservées",
    f"{random.randint(1,6)} torches",
    f"Arme quelconque",
    f"Armure quelconque",
    f"Objet utilitaire quelconque",
    f"Une souris perdue, prête à aider",
)


def generate_treasure_table():
    treasure_table = {
        1: generate_magic_sword_obj(),
        2: generate_spell_obj(),
        3: random.choice(trinkets),
        4: random.choice(valuable_treasure),
        5: random.choice(unusual_treasure),
        6: random.choice(large_treasure),
        9: random.choice(useful_treasure),
        11: f"Boîte contenant {random.randint(1, 6)*100} pépins",
        12: f"Sac contenant {random.randint(1, 6)*50} pépins",
        15: f"Bourse contenant {random.randint(1, 6)*10} pépins",
        18: f"Un petit tas de {random.randint(1, 6)*5} pépins",
    }
    return treasure_table


def generate_treasure_list(extra_dice=0):
    dice = 2 + extra_dice
    treasures = []
    for die in range(dice):
        table = generate_treasure_table()
        roll = random.randint(1, 20)
        k = find_key(roll, table)
        treasure = table[k]
        treasures.append(treasure)

    return treasures
