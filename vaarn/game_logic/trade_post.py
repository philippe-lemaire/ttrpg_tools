from random import choice, sample
from dataclasses import dataclass

trade_post_data_location_who_what = (
    (
        "Large Tent",
        "Hegemony Soldiers",
        "Water",
    ),
    (
        "Crossroads",
        "Faa Nomad Raiders",
        "Information",
    ),
    (
        "Beneath Great Cactus",
        "Faa Nomad Herdsmen",
        "Memories",
    ),
    (
        "Echoing Cave",
        "Cacogen Drifters",
        "Music",
    ),
    (
        "Beneath Glowering Idol",
        "Furtive Monks",
        "Olives",
    ),
    (
        "Sheltered Valley",
        "Cacklemaw Exiles",
        "Weapons",
    ),
    (
        "Atop Great Rock",
        "Oracle’s Caretakers",
        "Armour",
    ),
    (
        "Within Huge Skull",
        "Servants of a Petty God",
        "Pottery",
    ),
    (
        "Within Huge Empty Shell",
        "Vault Raiders",
        "Jewellery",
    ),
    (
        "Ancient Tollbooth",
        "A Science-Mystic",
        "Dried Fish",
    ),
    (
        "Stone Fort",
        "Lithling Scholars",
        "Livestock",
    ),
    (
        "Grove of Martyr Trees",
        "Gnomonian Merchants",
        "Prisoners",
    ),
    (
        "Dried Up Oasis",
        "Mercenary Band",
        "Psychedelics",
    ),
    (
        "Polluted Lakeshore",
        "Roaming Scavengers",
        "Flowers",
    ),
    (
        "Near Faa Nomad Camp",
        "Secretive Hermit",
        "Synth Parts",
    ),
    (
        "Near Hegemony Camp",
        "Lowly Goatherds",
        "Camels",
    ),
    (
        "Near Wreck",
        "Pious Synths",
        "Books",
    ),
    (
        "Near Holy Place",
        "Deranged Synths",
        "Carpets",
    ),
    (
        "By Oasis",
        "Pack of Newbeasts",
        "Medicine",
    ),
    (
        "Inside Ruin",
        "Titan Cultists",
        "Exotica",
    ),
)


npcs_a = (
    "Owner of the Trade Post",
    "Owner’s Spouse",
    "Owner’s Sibling",
    "Owner’s Heir",
    "Peacekeeper at the Trade Post",
    "Peacekeeper’s Sinister Deputy",
    "Studious Clerk",
    "Dishonest Clerk",
    "Lowly Servant",
    "Orphan, Found in the Deser",
)

npcs_b = (
    "Successful, Pompous Trader",
    "Sly, Scheming Trader",
    "Elderly, Naïve Trader",
    "Young, Cruel Trader",
    "Reckless, Hotheaded Trader",
    "Whining, Annoying Trader",
    "Brawny Youth, who Assists a Trader",
    "Performer, Who Entertains Traders",
    "Fortune-Teller, Just Passing Through",
    "Wandering, Scheming Stranger",
)


sources_of_drama = (
    "Envy (Property)",
    "Envy (Success)",
    "Love (Forbidden)",
    "Love (Unrequited)",
    "Love (Triangle)",
    "Unpaid Debts",
    "Boredom",
    "Petty Rivalry",
    "Robbery",
    "Gossip",
    "Adultery",
    "Conspiracy",
    "Gluttony",
    "Mistaken Identity",
    "Wild, Baseless Accusations",
    "Addiction (Drink)",
    "Addiction (Narcotics)",
    "Shoddy Goods",
    "Blackmail",
    "Murder",
)


@dataclass
class TradePost:
    location: str
    who_trades_here: str
    what_is_traded: str
    npc_a: str
    source_of_drama: str
    npc_b: str

    def __repr__(self):
        return f"""Located in a {self.location.lower()}.
        <br>
        {self.who_trades_here.capitalize()} are trading {self.what_is_traded.lower()}.
        <br>
        {self.npc_a.capitalize()} is in conflict with a {self.npc_b.lower()} over {self.source_of_drama.lower()}.
        """


def gen_trade_post():
    location = choice([line[0] for line in trade_post_data_location_who_what])
    who_trades_here = sample([line[1] for line in trade_post_data_location_who_what], 2)
    what_is_traded = sample([line[2] for line in trade_post_data_location_who_what], 2)
    who_trades_here = " and ".join(who_trades_here)
    what_is_traded = " and ".join(what_is_traded)
    npc_a = choice(npcs_a)
    source_of_drama = choice(sources_of_drama)
    npc_b = choice(npcs_b)

    return TradePost(
        location, who_trades_here, what_is_traded, npc_a, source_of_drama, npc_b
    )
