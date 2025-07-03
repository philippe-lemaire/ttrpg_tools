from .hoard_treasure import roll_potion, roll
import random
from collections import namedtuple


class AlchemistBeaker:
    def roll_potions(self):
        return [roll_potion() for _ in range(self.nlayers)]

    def __init__(self):
        self.nlayers = roll("1d4") + 1
        self.layers = self.roll_potions()

    def __repr__(self):
        return f"Alchemist's Beaker with {self.nlayers} layers."

    def pour(self):
        return self.layers.pop()

    def replenish(self):
        if self.layers:
            print(f"The Beaker is not empty, it still contains {self.layers}.")
            return None
        if not self.layers:
            self.layers = self.roll_potions()
            print(f"Replenished the beaker with {self.layers}")


Card = namedtuple("Card", ["name", "effect"])


class DeckofManyThings:
    def __init__(self):
        self.cards = [
            Card(
                "Sun",
                "Gain 50,000 XP and one beneficial miscellaneous magic item. (Roll for the magic item until something beneficial to the character comes up.",
            ),
            Card(
                "Moon",
                "1d4 wishes, which must be used within 1 turn per wish received.",
            ),
            Card(
                "Star",
                "Prime requisite increases by 2 points. If this would raise the score above 18, the points are instead allocated to random ability scores.",
            ),
            Card(
                "Vizier",
                "Grants the true and thorough answer to one question or problem. The question may be posed immediately or at any time in the future.",
            ),
            Card(
                "Comet",
                "Single-handedly defeat the next hostile monster(s) encountered to gain a level.",
            ),
            Card(
                "Throne",
                "CHA increases to 18 and the character gains possession of a small keep.",
            ),
            Card(
                "Key",
                "Gain a random treasure map plus a random magic weapon, staff, or wand (as appropriate to the character).",
            ),
            Card("Knight", "Gain the loyal service of a 4th level fighter."),
            Card(
                "Fates",
                "Allows the character to avoid one situation or the effects of one event, usable at any point in the future. The character’s companions do not gain the same benefit.",
            ),
            Card("Gem", "Gain 20 random gems or 20 random pieces of jewellery."),
            Card(
                "The Void",
                "The character becomes a mindless automaton, their soul trapped in a prison on another world or plane of existence. The soul can only be retrieved by questing (even a wish cannot retrieve it). When this card is drawn, the deck of many things disappears —no further cards can be drawn.",
            ),
            Card(
                "Flames",
                "A powerful chaotic monster from another plane of existence becomes aware of the character and schemes to destroy them.",
            ),
            Card(
                "Skull",
                """A lesser grim reaper appears and attacks
the character, who must defeat it alone. If the character is slain, they can never be returned to life. If other characters help
in the battle, lesser grim reapers appear to fight them as well.
<br>
<b>Lesser Grim Reaper: AC</b –3> [22],<br>
<b>HD</b> 10** (45hp), <b>Att</b> 1 × scythe (2d8),<br>
<b>THAC0</b> 11 [+8], <b>MV</b> 120’ (40’), <br>
<b>SV</b> D6W7 P8 B8 S10 (10), ML 12, AL Neutral,<br>
<b>XP</b> 2,300, <b>NA</b> 1 (1), <b>TT</b> None<br>
<ul>
<li>Undead: Immune to effects that affect living creatures (e.g. poison). Immune to mind-affecting or mind-reading spells (e.g. charm, hold, sleep).</li>
<li>Initiative: Always wins.</li>
<li>Attacks: Always hits.</li>
<li>Energy immunity: Unharmed by cold, fire, and electricity.</li>
</ul>""",
            ),
            Card(
                "Idiot",
                "Lose 1d4 points of INT. The character may choose to draw another card.",
            ),
            Card(
                "Talons",
                "All magic items owned by the character vanish instantly and permanently.",
            ),
            Card(
                "Ruin",
                "All money, valuables, and property owned by the character vanish instantly and permanently.",
            ),
            Card("Medusa", "Suffer a permanent –3 penalty to saves vs petrification."),
            Card(
                "Rogue",
                "A friendly NPC (a retainer, if the character has any) becomes utterly and permanently hostile toward the character. The hatred is initially secret and will only be revealed at a devastating moment.",
            ),
            Card(
                "Donjon",
                "The character is stripped of all equipment and spells and is imprisoned, either magically or physically. When this card is drawn, the deck of many things disappears—no further cards can be drawn.",
            ),
            Card(
                "Balance",
                "Change alignment (lawful becomes chaotic, chaotic becomes lawful, neutral becomes lawful or chaotic). If the character fails to behave according to their new alignment, they will be judged by higher powers and risk annihilation.",
            ),
            Card(
                "Jester",
                "Gain 10,000 XP or draw two more cards. After being drawn, the Jester card disappears forever.",
            ),
            Card(
                "Fool",
                "Lose 10,000 XP (to a minimum of 0 XP) and draw another card. After being drawn, the Fool card disappears forever.",
            ),
        ]

        random.shuffle(self.cards)

    def __getitem__(self, position):
        return self.cards[0]

    def __len__(self):
        return len(self.cards)

    def draw(self, n):
        cards_drawn = []
        for _ in range(n):
            c = self.cards.pop()
            cards_drawn.append(c)
            if c.name == "Fool":
                c = self.cards.pop()
                cards_drawn.append(c)
            if c.name in ("Donjon", "The Void"):
                print("The deck disappears.")
                break
        return cards_drawn
