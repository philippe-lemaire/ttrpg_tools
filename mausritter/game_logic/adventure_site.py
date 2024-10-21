import random
from dataclasses import dataclass

pasts = [
    "un ancien temple du culte chauve-souris",
    "une tour de guet abandonnée de longue date",
    "un manoir champêtre d'une souris noble",
    "un entrepôt hivernal caché",
    "une sépulture de souris de l'ancien temps",
    "un terrier creusé par des lapins ou des renards",
    "un bâtiment ou maison humaine",
    "un égout ou une canalisation",
    "des tunnels de fourmilière, terriblement étroits",
    "un arbre massif, sculpté par des souris",
    "une tour de sorcier",
    "un moulin à grains d'une colonie",
    "le nid du roi des rats",
    "un squelette d'une grande bête",
    "une académie de socières",
    "un portail vers le royaume des fées",
    "une mine profonde",
    "un repaire de bandits",
    "un grotte naturelle",
    "une colonie souris",
]

falls = [
    "une inondation",
    "un incident magique",
    "les ravages du temps",
    "un acte de destruction humaine",
    "un envahissement de mousse",
    "le tiraillement entre deux royaumes",
    "une attaque de grande bête",
    "une tempête",
    "l'arrivée d’esprits qui hantent encore ces lieux.",
    "un abandon soudain et mystérieux",
    "un conflit interne",
    "une maladie",
]

finds = [
    "Des souris, rendues folles ou désespérées",
    "Des souris, altérées magiquement",
    "Des bandits rats",
    "L'armée du Roi des Rats",
    "Les résidents d'origine, étrangement déformés",
    "Des esprits fantômatiques",
    "Avant-garde de l'armée fée",
    "Un serpent de mauvaise humeur",
    "Une nuée d'insectes",
    "Un Seigneur chat et ses serviteurs",
]

doings = [
    "un endroit sûr où vivre ou se cacher",
    "une réserve de nourriture",
    "un parent ou un ami ayant disparu",
    "des œuvres d'art anciennes, de valeur",
    "les derniers débris d'une ruine saccagée",
    "des champignons rares, pour alchimistes",
    "un sort étrange et puissant",
    "un gros tas de pépins",
]

secrets = [
    "un monolithe bruissant d’une obscure énergie",
    "une bête des origines, encore vivante",
    "des signes d’expérimentations humaines",
    "une tombe oubliée d’une ancienne reine",
    "un chemin vers les veines de la terre",
    "un portail vers le royaume des fées",
]


@dataclass
class AdventureSite:
    past: str
    fall: str
    find: str
    doing: str
    secret: str


def generate_adventure_site_obj():
    past = random.choice(pasts)
    fall = random.choice(falls)
    find = random.choice(finds)
    doing = random.choice(doings)
    secret = random.choice(secrets)
    return AdventureSite(past, fall, find, doing, secret)


if __name__ == "__main__":
    print(generate_adventure_site_obj())
