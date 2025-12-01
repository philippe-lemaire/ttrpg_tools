from random import choice
from dataclasses import dataclass

grave_data = (
    (
        "Ruined Village",
        "Autarchy Soldiers",
        "Upside Down",
        "Has Been Desecrated",
    ),
    (
        "Large Cave",
        "Titan-era Programmers",
        "In Salted Earth",
        "Believed Cursed",
    ),
    (
        "Secret Cave",
        "Autarchy Nobles",
        "In Decorated Urn",
        "Has Been Robbed",
    ),
    (
        "Below Floating Crystal",
        "Autarch’s Consort",
        "Mummified",
        "Visited by Ghouls",
    ),
    (
        "Lonely Hilltop",
        "Newbeasts",
        "Laminated",
        "Home to Rare Animal",
    ),
    (
        "Dry River-bed",
        "Synthetic Warrior",
        "Held in Preservation Tank",
        "Believed Haunted",
    ),
    (
        "Dry Lake-bed",
        "Synthetic Poet",
        "Held in Anti-Entropy Sphere",
        "Coins Left In Tribute",
    ),
    (
        "Imposing Crypt",
        "Synthetic Oracle",
        "Cryogenic Pod",
        "Food Left In Tribute",
    ),
    (
        "Cactus Grove",
        "Notorious Heretic",
        "Surrounded by Grave Goods",
        "Swords Left In Tribute",
    ),
    (
        "Ring of Standing Stones",
        "Cacogen Mystic",
        "Crystal Coffin",
        "Candles Burning",
    ),
    (
        "Under Petrified Tree",
        "Faa Nomad Ancestors",
        "Biotech Sarcophagus",
        "Memorial Tree",
    ),
    (
        "Below Huge Statue",
        "Faa Nomad Prophet",
        "Wearing Lifelike Death Mask",
        "Engraved Mantra",
    ),
    (
        "Elegant Pagoda",
        "Powerful Psychic",
        "Sky Burial",
        "Memorial Fountain (Dry)",
    ),
    (
        "Looming Edifice",
        "Famed Swordsman",
        "Consumed by Fungus",
        "Ritual Artwork (Ugly)",
    ),
    (
        "Plain of Stones",
        "Bandit King",
        "Food for Sacred Flower",
        "Ritual Artwork (Good)",
    ),
    (
        "Near Wreck",
        "Hegemony Rangers",
        "Below Cairn",
        "Site of Pilgrimage",
    ),
    (
        "Near Oasis",
        "Massacred Faa Nomads",
        "Inside Stone Cube",
        "Synthetic Grave Keeper",
    ),
    (
        "Near Ruin",
        "Hegemony Exultant",
        "Inside Hypergeometric Artefact",
        "Hideout for Bandits",
    ),
    (
        "Near Holy Place",
        "Autarch",
        "Frozen Outside Time-stream",
        "Entrance to Vault",
    ),
    (
        "Near Settlement",
        "Extra-Solar Explorers",
        "Not Really Dead",
        "Monster Lair",
    ),
)


@dataclass
class Grave:
    location: str
    grave_for: str
    burial_method: str
    grave_quirk: str

    def __repr__(self):
        return f"""Grave for {self.grave_for}, located in {self.location.lower()}.
    <br>Burial method: {self.burial_method.lower()}.
    <br>Quirk: {self.grave_quirk.lower()}.
    """


def gen_grave():
    data = [choice(grave_data)[k] for k in range(4)]
    return Grave(*data)
