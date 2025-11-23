from .ancestries import ANCESTRIES
from .abilities import ABILITIES
from .dice import roll_stat
from .weapons import weapon_generator, rarities
from .boons import BOONS
from .armor import gen_armor, gen_helmet_and_shield
from .explorer_gear import gen_gear
from .cybernetics import gen_cybernetic_implant
from .exotica import gen_exotica
from .hypergeometry import gen_codex
from .mystic_gift import gen_mystery_gift, gen_random_gift
from .alchemy import gen_crucible
from .mutations import get_mutations
from .true_kin import gen_looks_true_kin, set_character_name_and_details_true_kin
from .cacogen import gen_looks_cacogen, set_character_name_and_details_cacogen
from random import randint, choice


class Character:
    def __init__(self):
        self.ancestry = choice(ANCESTRIES)
        # force true kin for template testing
        # self.ancestry = ANCESTRIES[0]
        # force cacogen for template testing
        self.ancestry = ANCESTRIES[1]
        if self.ancestry == ANCESTRIES[0]:  # True Kin
            self.looks = gen_looks_true_kin()
            set_character_name_and_details_true_kin(self)
        elif self.ancestry == ANCESTRIES[1]:  # cacogen
            self.mutations = get_mutations(3)
            self.looks = gen_looks_cacogen()
            set_character_name_and_details_cacogen(self)
        for ability in ABILITIES:
            setattr(self, ability, roll_stat())
        self.healing_rate = randint(1, 8) + self.CON
        self.hp = randint(1, 8)
        self.item_slots = 10 + self.CON
        self.inventory = ["3 rations of water", "3 rations of food"]
        self.boon = choice(BOONS)
        r = 1 if self.boon == BOONS[0] else 0
        self.inventory.append(weapon_generator(rarities[r]))
        self.inventory.append(gen_armor())
        self.inventory.extend(gen_helmet_and_shield())
        self.inventory.extend(gen_gear())
        if self.boon == BOONS[1]:
            self.inventory.append(gen_crucible())
            self.inventory.append("1 Elixir")
        elif self.boon == BOONS[2]:
            self.cybernetics_implant = gen_cybernetic_implant()
        elif self.boon == BOONS[3]:
            self.inventory.append(gen_exotica())
        elif self.boon == BOONS[4]:
            self.inventory.append(gen_codex())
        elif self.boon == BOONS[5]:  # last boon Mystic Gift
            self.mystic_gift = gen_mystery_gift()
            self.random_gift = gen_random_gift()

        # TODO add additional rolls for the other boons
        # TODO add all the traits for each 10 ancestries gasp

    def __repr__(self):
        return f"{self.ancestry} character with {self.CON} CON and {self.hp} Hit Points, equipped with {self.inventory}"
