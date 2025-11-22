from dataclasses import dataclass
from random import randint, choice

base_types = ("melee", "ranged")
rarities = ["basic", "advanced", "exotic"]


base_weapons = {
    "melee": (
        "Dagger (d6, 1 slot)",
        "Flail (d6, 1 slot)",
        "Whip (d6, 1 slot)",
        "Axe (d6, 1 slot)",
        "Club (d6, 1 slot)",
        "Fleshripper (d6, 1 slot)",
        "Shock Baton (d6, Electrical, 1 slot)",
        "Razordisk (d6, 1 slot)",
        "War Fan (d6, 1 slot)",
        "Scythe (d6, 1 slot)",
        "Sword (d8, 2 slots)",
        "Mace (d8, 2 slots)",
        "Rapier (d8, 2 slots)",
        "Spear (d8, 2 slots)",
        "Quarterstaff (d8, 2 slots)",
        "War Hammer (d8, 2 slots)",
        "Great Mace (d10, 3 slots)",
        "Great Axe (d10, 3 slots)",
        "Halberd (d10, 3 slots)",
    ),
    "ranged": (
        "Great Sword (d10, 3 slots)",
        "Sling (d4, 1 slot, Ud20)",
        "Revolver (d6, 1 slot, Ud10)",
        "Pistol (d6, 1 slot, Ud10)",
        "Musket (d8, 2 slots, Ud8)",
        "Shotgun (d8, 2 slots, Ud8)",
        "Crossbow (d8, 2 slots, Ud8)",
        "Longbow (d8, 2 slots, Ud10)",
        "Rifle (d8, 2 slots, Ud10)",
        "Laser Pistol (d6, Beam, 1 slot, Ud12)",
        "Hand Cannon (d8, 2 slots, Ud8)",
        "Shock Bow (d8, Electrical, 2 slots, Ud8)",
        "Auto-Rifle (d8, 2 slots, Ud8)",
        "Scattergun (d8, 2 slots, Ud10)",
        "Laser Rifle (d8, Beam, 2 slots, Ud12)",
        "Concussion Rifle (d10, Concussive, 3 slots, Ud8)",
        "Spore Thrower (d10, Blast, Fungal, 3 slots, Ud8)",
        "Grenade Launcher (d10, Blast, 3 slots, Ud6)",
        "Laser Cannon (d10, Beam, 3 slots, Ud8)",
        "Port-A-Cannon (d12, Blast, 5 slots, Ud6)",
        "Railgun (d12, Piercing, 5 slots, Ud6)",
    ),
}

tags_dict = {
    rarities[0]: (
        (
            "Accurate",
            "Roll to hit with ADV if used at long range.",
        ),
        (
            "Ancient",
            "Half base trade value.",
        ),
        (
            "Bejewelled",
            "Triple base trade value.",
        ),
        (
            "Blasphemous",
            "Cursed by a religious leader. DIS on reaction rolls when encountering followers of said religion.",
        ),
        (
            "Bone",
            "Double trade value with Cacklemaw and Ghouls.",
        ),
        (
            "Corroded",
            "Half base trade value.",
        ),
        (
            "Crystalline",
            "If natural 1 is rolled, the weapon shatters beyond repair. Double base trade value.",
        ),
        (
            "Delicate",
            "Half base slot weight, minimum one slot, breaks on a to-hit roll of 1-2.",
        ),
        (
            "Elegant",
            "Half base slot weight, minimum one slot.",
        ),
        (
            "Fungal",
            "Deals no damage to Fungal creatures. Regains an Ammo die step when fed decaying animal or vegetable matter.",
        ),
        (
            "Gilded",
            "Double base trade value.",
        ),
        (
            "Laquered",
            "Double base trade value. Cannot rust or be corroded.",
        ),
        (
            "Luminous",
            "Can be used as light source, double base trade value.",
        ),
        (
            "Nomad’s",
            "Made by Faa Nomads, double trade value with Faa nomads.",
        ),
        (
            "Ornate",
            "Double base trade value.",
        ),
        (
            "Polychrome",
            "Double base trade value.",
        ),
        (
            "Quicksilver",
            "Half base slot weight, minimum one slot.",
        ),
        (
            "Ritual",
            "Used in an occult ritual. Double trade value with Mystics.",
        ),
        (
            "Sacred",
            "Blessed by a religious leader. ADV on reaction rolls when encountering followers of said religion.",
        ),
        (
            "Translucent",
            "Double base trade value.",
        ),
    ),
    rarities[1]: (
        (
            "Agonising",
            "Biological targets Morale save or flee the wielder. PCs damaged must EGO save or move away from the user.",
        ),
        (
            "Anti-Paradoxical",
            "Weapon is designed to combat extra dimensional beings. Double damage to Outsider-type creatures",
        ),
        (
            "Blasting",
            "The weapon can hit multiple targets in the same area. Roll to-hit once and compare to the AV score of all targets.",
        ),
        (
            "Blinding",
            "Targets must DEX Save vs 1 round of Blindness.",
        ),
        (
            "Concussive",
            "Targets STR save or are moved away from their location",
        ),
        (
            "Corrosive",
            "The weapon degrades AV. On a hit, the weapon either deals damage or reduces the target's AV score by one (attacker's choice)",
        ),
        (
            "Electrical",
            "Double damage to Synthetic creatures, targets wearing metal armour, targets in water.",
        ),
        (
            "Entangling",
            "Targets DEX save or become Entangled. Entangled creatures have AV 09, and attack with DIS. Must DEX Save to break free.",
        ),
        (
            "Eroding",
            "Double damage to Mineral-type creatures, vehicles, and static structures",
        ),
        (
            "Flaming",
            "Ignites flammable objects. Cannot be used underwater or against submerged opponents.",
        ),
        (
            "Freezing",
            "Targets CON save vs d4 DEX damage. At 0 DEX they are frozen solid and cannot move.",
        ),
        (
            "Heavy",
            "Double damage, double slot weight, minimum STR +3 to use",
        ),
        (
            "Hypergeometric",
            "The weapon exists partially outside of Euclidean space and deals doubled damage to Hypergeometric creatures.",
        ),
        (
            "Mauling",
            "Extra dice of damage against targets with AV 13 or lower, deals halved damage to opponents with AV 16 or higher",
        ),
        (
            "Parasitic",
            "The weapon is alive, and cannot be unequipped without surgery. The user must consume double rations each day. It does not need to reload.",
        ),
        (
            "Piercing",
            "Extra dice of damage against targets with AV 16 or higher, deals halved damage to opponents of AV 13 or lower.",
        ),
        (
            "Psyche-Suppressant",
            "Double damage to Psychic creatures. Cannot use Mystic Gifts while holding.",
        ),
        (
            "Strong",
            "The weapon deals double base damage. If the weapon would break, it does not.",
        ),
        (
            "Unstable",
            "If the wielder of this weapon rolls a 1 while using it, the weapon explodes, dealing 2d6 damage to the wielder.",
        ),
        (
            "Vampiric",
            "When this weapon damages biological creatures, the wielder regains HP equal to half the damage inflicted.",
        ),
    ),
    rarities[2]: (
        (
            "Aegis-Bearing",
            "Projects a personal warding field. Grants +5 AV while held.",
        ),
        (
            "Annihilating",
            "Target must CON save or crumble to dust. Wielder loses 1 max HP each time this weapon is drawn.",
        ),
        (
            "Autarch’s",
            "Weapon once belonged to ancient Autarch. Of highest quality, deals triple base damage and has five times its base trade value.",
        ),
        (
            "Blood-Rapturous",
            "When target is killed this weapon, the user heals for the target’s maximum HP.",
        ),
        (
            "Colossal",
            "The weapons deals triple base damage, has triple base slot weight. Minimum STR +6 to use.",
        ),
        (
            "Extra-Dimensional",
            "The weapon was forged in another dimension. It has the Hpergeometric and Anti-Paradoxical tags, and five times its base trade value.",
        ),
        (
            "Hard Light",
            "The weapon is made from hard light, projected from a wrist-mounted prism. It has a weight of 0.",
        ),
        (
            "Heat-Seeking",
            "Always hits warm-blooded creatures.",
        ),
        (
            "Indestructible",
            "Weapon cannot be broken or destroyed by any means, natural or supernatural.",
        ),
        (
            "Lithifying",
            "Targets take d8 DEX damage and gain +1 AV. At 0 DEX they turn to stone.",
        ),
        (
            "Nano-edged",
            "Weapon deals three times base damage",
        ),
        (
            "Necrotic",
            "Biological targets suffer d6 STR damage alongside base damage.",
        ),
        (
            "Neurotoxic",
            "Biological targets CON save vs death.",
        ),
        (
            "Polymorphic",
            "Weapon can swap between two forms at will. Choose an alternate base melee type or base ranged type.",
        ),
        (
            "Reflecting",
            "Missed attacks against the wielder damage the attacker instead.",
        ),
        (
            "Psionic",
            "Operated used psychic power. To-hit rolls made with PSY bonus, EGO bonus added to damage.",
        ),
        (
            "Rocket Boosted",
            "Weapon contains a small rocket-pack. +d10 damage when charging into melee range. Can be used to gain altitude.",
        ),
        (
            "Stim-Boosting",
            "Weapon boosts wielder’s reaction times. Make one extra combat action per round",
        ),
        (
            "Ultra-Corrosive",
            "Reduces AV by -2 on a hit. Targets take d8 CON damage alongside base damage.",
        ),
        (
            "Vibroactive",
            "The weapon or its projectiles vibrate at an atomic frequency inimical to solid-state armour. The weapon hits as though the target was unarmoured.",
        ),
    ),
}


@dataclass
class Weapon:
    rarity: str
    base_type: str  # melee or ranged
    weapon_base: str  # dagger or sling
    tags: list

    def __repr__(self):
        return f"{self.rarity.capitalize()} Weapon. {self.weapon_base.capitalize()}. <br>Tags:"


@dataclass
class Tag:
    name: str
    effect: str

    def __repr__(self):
        return f"<b>{self.name}</b>: {self.effect}"


def weapon_generator(rarity):
    base_type = choice(base_types)
    if rarity == rarities[0]:
        r = randint(0, 11)
        tags = [Tag(*choice(tags_dict[rarity]))]
    elif rarity == rarities[1]:
        r = randint(0, 19)
        tags = [Tag(*choice(tags_dict[tier])) for tier in rarities[:2]] + [
            Tag(
                "Fragile",
                f"If the wielder rolls a 1 while making an attack roll, the {rarity.capitalize()} Weapon breaks and must be repaired.",
            )
        ]
    elif rarity == rarities[2]:
        r = max(randint(0, 19) for _ in range(2))
        tags = [Tag(*choice(tags_dict[tier])) for tier in rarities] + [
            Tag(
                "Fragile",
                f"If the wielder rolls a 1 while making an attack roll, the {rarity.capitalize()} Weapon breaks.",
            )
        ]
    weapon_base = base_weapons[base_type][r]
    return Weapon(rarity, base_type, weapon_base, tags)
