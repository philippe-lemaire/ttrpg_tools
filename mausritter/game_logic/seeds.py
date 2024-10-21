import random

from dataclasses import dataclass


@dataclass
class Seed:
    creature: str
    problem: str
    complication: str


def generate_seed_obj(mix=False):
    seeds = {
        11: [
            "Une souris pêcheuse",
            "Il ou elle a été accusé d’un crime",
            "L'employé d'un PJ est responsable",
        ],
        12: [
            "Une famille dissidente",
            "Il ou elle Cherche une nouvelle maison",
            "Il faut traverser rivière",
        ],
        13: [
            "Un sorcier",
            "il ou elle est suivi·e",
            "L'antagoniste est sa propre ombre",
        ],
        14: [
            "Un Gardien de cafards",
            "il ou elle A découvert un étrange artefact",
            "Il est amnésique",
        ],
        15: [
            "Un fermier",
            "il ou elle a été Témoin d’un présage inquiétant",
            "L'antagoniste est déguisé",
        ],
        16: [
            "Une souris des Bourgs",
            "il ou elle doit assassiner un rival",
            "La maison d'un PJ est impliquée",
        ],
        21: [
            "Un fourrageur",
            "il ou elle doit retrouver un trésor perdu",
            "C'est protégé par d'étranges bêtes",
        ],
        22: [
            "Un·e commerçant·e",
            "il ou elle A vu sa maison se faire détruire",
            "L'antagoniste est un ami très proche",
        ],
        23: [
            "Un·e marchand·e itinérant·e",
            "il ou ellle a été Dépouillé·e d'un bien précieux",
            "C'est le véritable antagoniste",
        ],
        24: [
            "Un·e chevaucheur·se de pigeon",
            "il ou elle A été kidnappé·e",
            "L'ami·e d'un PJ est impliqué·e",
        ],
        25: [
            "Un·e brasseur·se",
            "il ou elle A été exilé·e de son village",
            "Il ou elle a été piégé·e",
        ],
        26: [
            "Un·e herboriste",
            "il ou elle Cherche un remède rare",
            "C'est très urgent",
        ],
        31: [
            "Un· Messager·e",
            "il ou elle A perdu son chemin",
            "Il ou elle dispose d'une information vitale",
        ],
        32: [
            "Un·e Vagabond·e",
            "il ou elle S'est fait voler toute sa nourriture",
            "L'antagoniste a une bonne raison",
        ],
        33: [
            "Un sujet d'expériences",
            "il ou elle Est pourchassé·e par des humains",
            "Il ou elle est suivi par une puce",
        ],
        34: [
            "Un·e mineur·se d'étain",
            "Il ou elle A été détroussé·e par des bandits",
            "L'antagoniste est complètement saoûl",
        ],
        35: [
            "Un·e boulanger·e",
            "il ou elle A mangé une baie empoisonnée",
            "L'antagoniste est un membre de la famille",
        ],
        36: [
            "Un Chevalier des Haies",
            "Un membre de sa famille a disparu",
            "Il ou elle est mourant",
        ],
        41: [
            "Un Collecteur d'impôts",
            "il ou elle A perdu un grand nombre de pépins",
            "Il ou elle est complètement bourré·e",
        ],
        42: [
            "Une Matriarche",
            "il ou elle A été accusé·e de meurtre",
            "L'antagoniste est un change-forme",
        ],
        43: [
            "Un·e prospecteur·rice",
            "Sa tortue de trait est coincée",
            "Il ou elle est bien plus riche que ce que les apparences suggèrent",
        ],
        44: [
            "Un·e Chef·fe de la Guilde des Tunnels ",
            "il ou elle A été assassiné",
            "Le rival d'un PJ est impliqué",
        ],
        45: [
            "Une souris noble",
            "Sa maison est attaquée",
            "L'antagoniste cherche à se venger",
        ],
        46: [
            "Un·e bandit·e rat·te",
            "il ou elle Veut voler un rival",
            "Un fantôme hante les lieux",
        ],
        51: [
            "Une abeille reine",
            "il ou elle doit Voyager vers un nouveau domicile",
            "Ses suivants ne sont pas d'accord",
        ],
        52: [
            "Une officière de l'armée fourmi",
            "il ou elle Est chassé·e par des ennemis",
            "Il ou elle est sérieusement blessé",
        ],
        53: [
            "Un mage Hibou",
            "il ou elle Veut retrouver un sort rare",
            "C'est au fond d'une grotte",
        ],
        54: [
            "Un Seigneur Chat",
            "il ou elle Veut être diverti",
            "Il ou elle a piégé les PJ",
        ],
        55: [
            "Un caneton",
            "il ou elle A perdu sa mère",
            "Il ou elle doit rejoindre une île",
        ],
        56: [
            "Un mille-pattes géant",
            "il ou elle Veut un endroit chaud où dormir",
            "il ou elle A besoin d'un objet porté par un PJ",
        ],
        61: [
            "Un ambassadeur lilliputien",
            "il ou elle Veut atteindre la reine souris",
            "il ou elle Ne comprend pas les coutumes locales",
        ],
        62: [
            "Un fantôme piégé",
            "il ou elle Veut trouver le grand amour",
            "il ou elle Ne peut pas quitter ce lieu",
        ],
        63: [
            "Un émissaire fée",
            "il ou elle Veut enlever une souris",
            "Sa cible est un PJ",
        ],
        64: [
            "Une nuée de moucherons",
            "il ou elle Veut voler une des souris-joueuses",
            "L'antagoniste est exceptionnellement doué",
        ],
        65: [
            "Une Mémé araignée",
            "il ou elle A perdu un trésor ancien",
            "il ou Elle l'a avalé",
        ],
        66: [
            "Un oisillon",
            "il ou elle Ne peut pas rentrer à la maison",
            "il ou elle Doit grimper à un arbre",
        ],
    }
    if not mix:
        creature, problem, complication = seeds.get(random.choice(list(seeds.keys())))
    else:
        creature, problem, complication = [
            seeds.get(random.choice(list(seeds.keys())))[k] for k in range(3)
        ]
    return Seed(creature.capitalize(), problem.lower(), complication.lower())


if __name__ == "__main__":
    print(generate_seed_obj(mix=True))
