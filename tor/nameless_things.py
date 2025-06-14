from random import choice, sample
from .tor_dice_roller import eye, gandalf, FeatDie

referred_to_as = (
    "The Bane",
    "The Scourge",
    "The Horror",
    "The Terror",
    "The Defiler",
    "The Devourer",
    "The Stalker",
    "The Hunter",
    "The Watcher",
    "The Crawler",
    "The Lurker",
    "The Flame",
)

refered_to_part_2 = (
    "in the Dark",
    "of the Abyss",
    "in the Deep",
    "of the Pit",
    "of Udûn",
    "in the Water",
)

refered_by = (
    "by <b>Men</b>",
    "by <b>Elves</b>",
    "by <b>Dwarves</b>",
    "by <b>Orcs</b>",
    "by <b>the Wise</b>",
    "in <b>ancient lore</b>",
)

described_as = (
    "Bat-­like",
    "Spider-­like",
    "Fish-­like",
    "Slug-­like",
    "Worm-­like",
    "Centipede-­like",
    "Insect-­like",
    "Crustacean-­like",
    "Octopus-­like",
    "Man-­like",
    "Toad-­like",
    "Troll-­like",
)

described_as_part_2 = (
    "with remorseless eyes",
    "with great horns",
    "with luminous skin",
    "with a huge head",
    "with a swollen body",
    "yet greater",
)

before_you_see_it = (
    "notice a deadly silence",
    "hear a sinister hissing",
    "hear a low growl",
    "see the bones of its victims",
    "feel your skin crawl",
    "hear a deafening sound or scream",
    "notice its tracks",
    "hear a terrifying scream",
    "smell a hideous stench",
    "feel a violent gust of air",
    "hear a piping sound",
    "feel a terrible cold",
)

what_you_see_first = (
    "is a great shadow, in the middle of which is a dark form",
    "are its great claws",
    "are its eyes, glowing in the dark",
    "is that its body is flaccid and translucent, as if composed of gelatinous material",
    "is its gaping mouth, opening and closing as if gasping for air",
    "is a large maw, with fangs eerily similar to human teeth",
    "is that swarms of insects or other vermin are crawling before it",
    "is a long, sinuous tentacle, slithering towards you",
    "are its huge fangs, so big and long that it cannot close its mouth",
    "are its wide, blind eyes",
    "are many twisted horns of stained ivory",
    "is a vision of a beautiful creature, a phantom of the mind",
)
rumour = (
    "When Sauron reoccupied Dol Guldur, he sought the allegiance of the many dark things living in Mirkwood. Some refused, and were imprisoned in the vast dungeons of the fortress. When the White Council attacked, one such creature was still kept there in chains, dying. Later, it managed to break free and vanish into the darkness, a sworn enemy of any living being.",
    "When Annúminas was young, the Men of Arnor disturbed something monstrous that had been sleeping on the bottom of Lake Evendim for millennia. One summer night, the thing lashed out in fury at several ships anchored near the harbour, dragging them into the depths, along with their crews. Then, it disappeared again. For a while.",
    "Forced long ago to serve Sauron, the thing fought at the battle of Dagorlad, spreading terror among the ranks of the Elves. Since no one had the courage to face it, Gilgalad himself had to intervene. Surprised by the steadfastness of the High King and the splendour of Aiglos, his great spear, the thing chose to retreat. With the defeat of its master, the thing regained its free will and fled across Middle-earth.",
    "After the Great Plague, the once wealthy Tharbad fell into decay, and its population diminished. One night, some among those who still lived in the city saw a large black shadow slowly approach the bridge, encompassing it. After a few moments, with a great roar, the bridge crumbled into a thousand pieces.",
    "Ohtar, Isildur's squire who was among the few to save himself from the ambush of the Orcs, escaped the disaster of the Gladden Fields, taking with him the sword of Elendil. Some say he was chased for a long time by a monstrous creature, which moved only at night. The thing seemed able to 'smell' his movements.",
    "Fornost didn’t fall by normal means. The Witch-­king of Angmar unleashed against the city a terrifying creature that owed the Wraith-king a debt of gratitude. It was this enemy of all light and life that disrupted the defenses and brought them down. The debt paid, it returned to the darkness from which it had been called.",
    "The Dwarves spoke of many horrors haunting the Grey Mountains. Emerging from who knows where, they crawled into the mines, killing and destroying. Eventually the Dwarves managed to drive them out, but one of them just wouldn't go away. It is said that it was Thorin I who defeated and drove it away, in a long duel that took place in the dark depths of the mine.",
    "For a long time, the thing dwelt in a deep cave in the northernmost foothills of the Misty Mountains. The Hillmen worshipped it as a god, feeding and caring for it. Then war came to those territories. Armies of Elves and Men drove out the Hillmen, and the thing was deprived of its followers, developing an irrepressible hatred against the invaders.",
    "Centuries ago, the thing dwelt in the darkest recesses of a valley on the east side of the Misty Mountains. One day, it came to a village of the Woodmen, when the hunters were away. When they returned, they were met by a gruesome scene: dismembered bodies, destroyed houses, a terrible smell that filled the air. No survivors.",
    "Once every certain number of years, the thing returns to the Mountains of Mirkwood. When it does, hundreds of Spiders, large and small, swarm as if crazed to the south or west, overwhelming whatever they encounter in their path.",
    "The thing is greedy. Not for treasure, but for bones. Animal ones are easy to get, and so are those of Orcs, Men, or Dwarves — this has made the thing hungry for the bones of Elves.",
    "When Beleriand was broken, many creatures fled its ruin. Among them is a thing that is particularly large and cruel.  Since that time, it has been moving east.",
)

remembered = (
    "Orcs hate the evil things that crawl in the dark perhaps even more than Men, Elves, and Dwarves. For they are more often the ones who end up as food to feed them. Being able to talk to an Orc could prove very useful, if the thing is nearby.",
    "The Great Eagles see many things from above, but they don't speak of them unless they have a good reason. They do not tell, for example, of the monstrosity that after darkness haunted the banks of the Great River long ago, devouring lonely travellers. They spied it incessantly. One day, it was gone. The Eagles searched the surroundings for a long time, but to no avail.",
    "There is only one Elven song that tells of the mournings caused by the thing, but being immensely sad, it is seldom sung in the Hall of Fire of Rivendell. Some say that if it's nighttime and you fear the thing is nearby, singing the whole song will keep it from getting closer.",
    "A sentence carved onto the wall of a dark cave in the north near the Grey Waste, reads: “Here Belegorn son of Bergil of Dol Amroth banished the thing from the Abyss but died of its foul wounds. Glorfindel of the Elves retrieved his body to return to his family”",
    "Among the ancient scrolls and books preserved in Minas Tirith, there is a brief chronicle of the times when the city itself was built. Despite numerous missing pieces of text, it is clear that it concerns the presence of an evil thing under Mount Mindolluin, horrible to look upon and very aggressive.",
    "Few traces remain of the countless generations of Northmen who inhabited the southeastern edge of Mirkwood.  Among them is a burial monument covered in soft moss. An inscription speaks of the death of Crinna, a village chief probably, caused by a terrible thing that came out of the woods at night and could only be kept at bay by lighting large fires.",
    "Since many Hobbits are afraid of the water, there is a common test of courage among the youth of the Eastfarthing that involves reciting a nursery rhyme while sitting on the shore of the Brandywine, at night. The rhyme, handed down since the dawn of time, speaks of a thing made of darkness, which comes out of the water and devours those who look at their reflection in the moonlight.",
    "The Rangers tell many tales of the horrible and mysterious things that prowl in Eriador. Most are made up, the Elves laughingly say, but one is definitely not. A creature that can suddenly appear at your side while you're sleeping. The Elves speak of it as well, but they are less concerned, since they never sleep…",
    "Saruman loves secrets. And he is adept at keeping quiet about his well-­stocked collection of texts concerning the presence of dark creatures roaming Middle-­earth. He tried to classify them once, but soon desisted: too many, and too different from each other.",
    "The Seeing Stone on the tower of Elostirion, in the Emyn Beraid, constantly looks westwards, beyond the sea. Only on very few occasions does it turn its gaze elsewhere, when a creature as ancient and evil approaches the Grey Havens.  It follows this hideous thing in all its movements, and only when it passes out of sight does the Stone return to look towards the immortal lands.",
    "In the private library of Elrond, in Rivendell, there is a parchment entirely dedicated to the creature, with many indications about its habits and the places where it might lurk.",
    "Only the wisest of Middle-earth know anything about this dark creature as old as the earth. And they fear it. But by asking them directly, some good advice might be acquired. If you want to avoid it or flee from it of course, not on how to fight it, for no one would be so foolish…",
)


def get_hate(die):
    if die.value == gandalf:
        return 6
    if die.value == eye:
        return 12
    v = die.value + die.value % 2
    return 12 - v // 2


def get_armour(die):
    if die.value == gandalf:
        return 2
    if die.value == eye:
        return 5
    if die.value <= 4:
        return 4
    return 3


def get_endurance(die):
    if die.value == gandalf:
        return 60
    if die.value == eye:
        return 120
    v = die.value + die.value % 2
    return 120 - 5 * v


def get_might(die):
    if die.value == eye:
        return 3
    if die.value == gandalf:
        return 2
    return 3 if die.value <= 4 else 2


def get_combat_proficiency(die):
    if die.value == gandalf:
        return 2
    if die.value == eye:
        return 4
    return 3


def get_number_of_fell_abilities(die):
    if die.value == gandalf:
        return 2
    if die.value == eye:
        return 5
    v = die.value
    if v in range(1, 5):
        return 4
    if v in range(5, 9):
        return 3
    return 2


def get_parry(die):
    if die.value == eye:
        return "+4"
    if die.value == gandalf or die.value >= 8:
        return "—"
    v = die.value + die.value % 2
    return f"+{4 - v//2}"


attack_forms = [
    [
        "Crush (hooves, paws)",
        "Attribute Level",
        "12",
        "Break Shield",
    ],
    [
        "Bite (bite, beak)",
        "Attribute Level -2",
        "14",
        "Pierce",
    ],
    [
        "Rend (fangs, claws)",
        "Attribute Level -2",
        "16",
        "Seize",
    ],
]

fell_abilities = [
    (
        "Thing of Terror",
        "At the start of the first round of the battle all Player-heroes in sight of one or more creatures with this ability gain 3 Shadow points (Dread). Those who fail their Shadow test are daunted and cannot spend Hope for the rest of the fight.",
    ),
    (
        "Deadly Wound",
        "Wounded targets make an Ill-favoured Feat die roll to determine the severity of the injury.",
    ),
    (
        "Denizen of the Dark",
        "All rolls are Favoured while in darkness.",
    ),
    (
        "Great Leap",
        "Spend 1 Hate to attack any Player-hero, in any combat stance, including Rearward.",
    ),
    (
        "Horrible Strength",
        "If the creature hits and causes a Piercing Blow, spend 1 Hate to make the target’s Protection roll Ill-favoured.",
    ),
    (
        "Poison",
        "If an attack results in a Wound, the target is also poisoned (see page 134).",
    ),
    (
        "Heartless",
        "The creature is not affected by the Intimidate Foe combat task, unless a Magical success is obtained.",
    ),
    (
        "Thick Hide",
        "Spend 1 Hate point to gain (2d) on a Protection roll.",
    ),
    (
        "Strike Fear",
        "Spend 1 Hate to make all Player-­heroes in sight gain a number of Shadow points (Dread) equal to the Might rating of the creature. Those who fail their Shadow test are daunted and cannot spend Hope for the rest of the fight.",
    ),
    (
        "Snake-like Speed",
        "When targeted by an attack, spend 1 Hate to make the attack roll Ill-favoured.",
    ),
    (
        "Foul Reek",
        "Spend 1 Hate point to cause all combatants engaged with the thing to lose (1d) on all rolls for the round.",
    ),
    (
        "Fear of Fire",
        "The thing loses 1 Hate at the start of each round it is engaged in close combat with an adversary wielding a torch or other sort of burning item.",
    ),
]


class NamelessThing:
    def __init__(self):
        self.referred_to_as = choice(referred_to_as)
        self.referred_by = choice(refered_by)
        self.description = f"{choice(described_as)} {choice(described_as_part_2)}"
        self.before_you_see_it = choice(before_you_see_it)
        self.what_you_see_first = choice(what_you_see_first)
        self.rumour = choice(rumour)
        self.remembered = choice(remembered)
        self.hate = get_hate(FeatDie())
        self.parry = get_parry(FeatDie())
        self.armour = get_armour(FeatDie())
        self.endurance = get_endurance(FeatDie())
        self.might = get_might(FeatDie())
        self.combat_proficiency = get_combat_proficiency(FeatDie())
        self.number_of_fell_abilities = get_number_of_fell_abilities(FeatDie())
        self.attack_forms = sample(attack_forms, 2)

        # replace Attribute Level in attacks by computed value
        for att in self.attack_forms:
            att[1] = str(eval(att[1].replace("Attribute Level", str(self.hate))))

        self.fell_abilities = sample(fell_abilities, self.number_of_fell_abilities)

    def __repr__(self):
        return self.referred_to_as + self.description


if __name__ == "__main__":
    print(NamelessThing())
