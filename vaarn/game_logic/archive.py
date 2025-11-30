from random import choice
from dataclasses import dataclass

archive_data = (
    (
        "Books (Holy)",
        "Dusty",
        "Glum Nuns",
        "Rare Object Retrieved From Elsewhere in Vaarn",
    ),
    (
        "Books (Fiction)",
        "Collapsing",
        "Pedantic and Rude",
        "Rare Object Retrieved From Elsewhere in Vaarn",
    ),
    (
        "Books (Obscene)",
        "Cluttered",
        "Salacious Bigots",
        "A Stolen Item From the Collection Retrieved",
    ),
    (
        "Memory Crystals",
        "Labyrinthine",
        "Senile Synths",
        "A Stolen Item From the Collection Retrieved",
    ),
    (
        "Seeds",
        "Dark",
        "Bored Hedonists",
        "Players to Intervene in Internal Power Struggle",
    ),
    (
        "Fungal Spores",
        "Dazzling",
        "Lazy Mycomorphs",
        "Players to Intervene in Internal Power Struggle",
    ),
    (
        "Embryos",
        "Grimy",
        "Tiny Lithling",
        "A Sealed Wing Of the Archive Explored",
    ),
    (
        "Eggs",
        "Chaotic",
        "Maternal New-Parrots",
        "A Sealed Wing Of the Archive Explored",
    ),
    (
        "Maps",
        "Malfunctioning",
        "Ascetic Mutes",
        "An Archivist Escorted To Distant Settlement",
    ),
    (
        "Poems",
        "Elegant",
        "Cultists Who Worship Decay",
        "An Archivist Escorted To Distant Settlement",
    ),
    (
        "Video Recordings",
        "Serene",
        "Ignorant of What They Collect",
        "A Rival Archive Raided",
    ),
    (
        "Music",
        "Squalid",
        "Worship Their Collection",
        "A Rival Archive Raided",
    ),
    (
        "Playscripts",
        "Sterile",
        "Chattering Imbeciles",
        "To Send A Message to a Science-Mystic",
    ),
    (
        "Art (Paintings)",
        "Ordered",
        "Attack Outsiders",
        "To Send A Message to a Science-Mystic",
    ),
    (
        "Art (Statues)",
        "Polluted",
        "Desperately Seeking Recruits",
        "To Locate an Archivist Who Vanished in the Stacks",
    ),
    (
        "Art (Conceptual)",
        "Occult",
        "Afflicted by Strange Illness",
        "To Locate an Archivist Who Vanished in the Stacks",
    ),
    (
        "Taxidermy",
        "Foreboding",
        "Whispering New-Spiders",
        "Monster Lair Removed From Archive",
    ),
    (
        "Preserved Brains",
        "Cheerful",
        "Masked Philosophers",
        "Monster Lair Removed From Archive",
    ),
    (
        "Titancreed Syntax",
        "Burned",
        "Cruel and Calculating",
        "Vault Beneath Archive Explored",
    ),
    (
        "Insects",
        "Infested",
        "Paranoid and Isolated",
        "Vault Beneath Archive Explored",
    ),
)


@dataclass
class Archive:
    archive_of: str
    condition: str
    the_archivists: str
    they_want: str

    def __repr__(self):
        return f"Archive of {self.archive_of}, in {self.condition.lower()} condition.<br>The Archivists are {self.the_archivists.lower()}. They want {self.they_want.lower()}."


def gen_archive():
    data = (choice(archive_data)[k] for k in range(4))
    return Archive(*data)
