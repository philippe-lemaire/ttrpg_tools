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
from .true_kin import set_character_name_and_details_true_kin
from .cacogen import gen_looks_cacogen, set_character_name_and_details_cacogen
from .synth import get_synth_looks, set_synth_details
from .newbeast import get_newbeast_looks, set_newbeast_name_and_animal
from .neobloom import set_neobloom_name_and_details
from .mycomorph import set_mycomorph_name_and_details
from .faa_nomad import set_character_name_and_details_faa_nomad
from .cacklemaw_exile import set_character_name_and_details_cacklemaw_exile
from .planeyfolk import set_character_name_and_details_planeyfolk
from .lithling import set_character_name_and_details_lithling

from random import randint, choice


class Character:
    def __init__(self, ancestry=None):
        self.inventory = ["3 rations of water", "3 rations of food"]
        self.hp = randint(1, 8)

        if ancestry:
            self.ancestry = ancestry
        else:
            self.ancestry = choice(ANCESTRIES)

        if self.ancestry == ANCESTRIES[0]:  # True Kin
            set_character_name_and_details_true_kin(self)
        elif self.ancestry == ANCESTRIES[1]:  # cacogen
            self.mutations = get_mutations(3)
            self.looks = gen_looks_cacogen()
            set_character_name_and_details_cacogen(self)
        elif self.ancestry == ANCESTRIES[2]:  # Synth
            self.looks = get_synth_looks()
            set_synth_details(self)
            self.inventory.append("3 spare Synth parts")
        elif self.ancestry == ANCESTRIES[3]:  # newbeast
            self.looks = get_newbeast_looks()
            set_newbeast_name_and_animal(self)
        elif self.ancestry == ANCESTRIES[4]:  # neobloom
            set_neobloom_name_and_details(self)
        elif self.ancestry == ANCESTRIES[5]:  # mycomorph
            set_mycomorph_name_and_details(self)
        elif self.ancestry == ANCESTRIES[6]:  # faa nomad
            set_character_name_and_details_faa_nomad(self)
        elif self.ancestry == ANCESTRIES[7]:  # cacklemaw exile
            set_character_name_and_details_cacklemaw_exile(self)
        elif self.ancestry == ANCESTRIES[8]:  # planeyfolk
            set_character_name_and_details_planeyfolk(self)
        elif self.ancestry == ANCESTRIES[9]:  # lithling
            set_character_name_and_details_lithling(self)
        for ability in ABILITIES:
            setattr(self, ability, roll_stat())

        self.item_slots = 10 + self.CON
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
