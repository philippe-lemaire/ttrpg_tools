from .dice_tools import roll, get_closest_key
from .game_facts import (
    classes,
    ancestries,
    backgrounds,
    stats_names,
    talents_dict,
    ancestries_feat_dict,
)
import random


def roll_stats():
    stats_rolled = [roll("3d6") for _ in range(6)]

    stats = {k: v for k, v in zip(stats_names, stats_rolled)}
    return stats, max(stats_rolled)


class PC_Character:
    def __init__(
        self,
        stats_d,
        ancestry,
        background,
        class_,
        hp=0,
        level=1,
        known_talents=[],
        first_creation=True,
    ):
        # stats
        for stat_name, value in stats_d.items():
            setattr(self, stat_name, value)
            setattr(self, f"{stat_name}_MOD", (value - 10) // 2)
        if isinstance(ancestry, int):
            self.ancestry = ancestries[ancestry]
        else:
            self.ancestry = ancestry

        self.ancestry_feat = ancestries_feat_dict.get(self.ancestry)
        if isinstance(background, int):
            self.background, self.background_description = backgrounds[background]
        else:
            self.background = background
            self.background_description = ""

        if isinstance(class_, int):
            self.class_ = classes[class_]
        else:
            self.class_ = class_
        # level
        self.level = level
        # hp
        self.hp = hp
        self.talents = known_talents

        if first_creation:
            self.roll_hp()
            self.roll_talent()

    def save(self):
        stats_d = {attr: getattr(self, attr) for attr in stats_names}
        return {
            "stats_d": stats_d,
            "ancestry": self.ancestry,
            "background": self.background,
            "class_": self.class_,
            "hp": self.hp,
            "level": self.level,
            "known_talents": self.talents,
        }

    def level_up(self):
        self.level += 1
        self.roll_hp()
        self.roll_talent()

    def roll_hp(self):
        if self.level == 0:
            rolled_hp = max(1, self.CON_MOD)
            if self.ancestry == "Dwarf":
                rolled_hp += 2

        else:
            classes_hit_dice = ["d8", "d6", "d4", "d4"]
            classes_d = {cl: hd for cl, hd in zip(classes, classes_hit_dice)}
            hd = classes_d.get(self.class_)

            if self.ancestry == "Dwarf":
                rolled_hp = max(1, roll(hd, advantage=True) + self.CON_MOD) + 2
            else:
                rolled_hp = max(1, roll(hd) + self.CON_MOD)
        self.hp += rolled_hp

    def roll_talent(self):
        """Rolls a talent depending on class_"""
        talents = talents_dict.get(self.class_)
        n_talents = 2 if (self.ancestry == "Human" and self.level == 1) else 1

        rolled_talents = []
        for _ in range(n_talents):
            rolled_value = roll("2d6")
            rolled_talents.append(get_closest_key(rolled_value, talents))

        self.talents.extend(rolled_talents)

    def get_stats(self):
        stats = [getattr(self, attr) for attr in stats_names]
        stats_mod = [getattr(self, f"{attr}_MOD") for attr in stats_names]
        return zip(stats_names, stats, stats_mod)

    def __repr__(self):
        return f"""{self.background} level {self.level} {self.ancestry} {self.class_} character with {self.hp} Hit Points.\n{[f"{attr}: {getattr(self, attr)}" for attr in stats_names]}"""


class NPC_Character(PC_Character):
    def __init__(self, level=0, ancestry=None):
        # Level
        self.level = level
        # Stats generation

        rolled_values = [roll("3d6") for _ in range(6)]
        for stat, rolled_value in zip(stats_names, rolled_values):
            setattr(self, stat, rolled_value)
            setattr(self, f"{stat}_MOD", (rolled_value - 10) // 2)

        # ancestry

        if ancestry is None:
            self.ancestry = random.choice(ancestries)
        # class

        if self.level == 0:
            self.class_ = "Peasant"
        else:
            self.class_ = random.choice(classes)
        # HP
        self.roll_hp()

        # background

        self.background, self.background_description = random.choice(backgrounds)
