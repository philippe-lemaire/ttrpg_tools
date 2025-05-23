from random import randint, choice
from .game_data import LIMINAL_HORROR_MODULES

bloom_fallouts = (
    "<b>Sporocarp</b>: Your nails yellow and your skin begins to crack and harden in places, mottling in color. +1 armor.",
    "<b>Bioluminescence</b>: There’s a chemical reaction going on inside of you. In darkness, the skin of your hands produces a weak light.",
    "<b>Mycelia Hair</b>: Your hair begins to fall out, quickly replaced by wispy white strands. You are much more sensitive to environmental changes (temperature, wind direction, pressure, etc). Roll d4 and add it to your CTRL (max 18).",
    "<b>Coagulation</b>: You don’t bleed. Mycelic fibers stitch together your wounds. Heal d2 STR damage per day, up to max.",
    "<b>Psilocybin</b>: Your vision waivers. Hallucinations manifest. Ghosts wander at the periphery. +1 Stability.",
    "<b>Become One</b>: Something is calling to you, a compulsion to join with the mass. It feels the pull to you as well. Facilitator</b>: PC has +1 Stability whenever in the presence of the Flesh Hydra (p.15).",
    "<b>Impulse</b>: You can feel them communicating. A tingle on the skin, a spike of anxiety. Every dawn there are more voices.",
    "<b>Twisted Strands</b>: Strands of mycelia twist under your skin, bulging like varicose veins. Digging into muscle, they act as extra ligaments. Roll d4 and add it to your STR (max 18).",
    "<b>Deadened Nerves</b>: Something inside is allowing you to push past your physical limits, but everything comes at a cost. You are no longer affected by Fatigue or Deprivation.",
)

legacy_fallouts = (
    """<b>Have you been replaced?</b> You’ve seen what they can do -their magics and their deceptions. What would stop them from taking you? Maybe you aren’t who you think you are? How would you even know?<br>
During your next moment of quiet reflection, roll 1d6. If the total is higher than your max HP, take the new result.""",
    """<b>Memories of an Unknown Traveler</b>: These memories are not your own. They are of a different time, a different place, from a perspective so unlike your own. The realities they walk through are so alien and different, their feelings so foriegn. If only you could understand what they experienced.<br>
During your next rest, roll 1d6. If the total is higher than your max HP, take the new result.""",
    """<b>Paranoia</b>: Is it paranoia if the worries are completely reasonable? You’ve seen what happens in the dark, you know what goes bump in the night.<br>
After a week, roll 1d6. If the total is higher than your max HP, take the new result.""",
    """<b>Plagued by Nightmares</b>: It comes for you every night, without fail. You do not know if they are from the beginning, or the end. All you know is that they won’t stop, and that they must mean something. After a week of nightmares, tell your Facilitator two distinct images that linger at the edge of your remembering.<br>
""",
    """<b>Mirror World</b>: Everything seemed okay at first, but now you are sure of it - the world inside the mirror is different. The side glances, the shifting of places, it is undeniable.<br>
When you first start to notice, roll 2d6. If the total is higher than your max HP, take the new result.
""",
    """<b>Odd</b>: You adopt an odd behavior that makes others uncomfortable. If you resist indulging in your “Oddity” for 24 hours, take the Deprived tag. If others see you engage in this creepy behavior, they must make a CTRL save or take 1d4 Stress.<br>
After the first instance, roll 3d6. If the total is higher than your current CTRL, take the new result.
""",
    """<b>Hunger</b>: You develop an unnatural hunger for the unusual. If you do not satiate your appetite for 24 hours, take the Deprived tag. When you eat, restore HP and give 1d4 stress to any that can see.<br>
After the first instance, roll 3d6. If the total is higher than your current STR, take the new result.
""",
    """<b>Scarred</b>: Every wound you inflict leaves its ragged mark upon your body.<br>
After the first instance, make a CTRL save. If you pass, increase your max STR by 1d4.
""",
    """<b>Liminal Communion</b>: It wasn’t noticeable at first, but something is trying to communicate, but it does not have a mouth by which to scream. Its words manifest throughout physical space.<br>
Increase your max CTRL by 1d4.
""",
    """<b>Magical Corruption (this can be taken multiple times per character)</b>: Flesh is weak. A part of your body becomes visibly changed through your proximity to the weird. The Facilitator and Player should decide on how that change manifests and if it has any mechanical impacts.<br>
  	  	 """,
    """<b>Threshold</b>: There is a pale door with a black handle. It is unremarkable other than the fact that this door can seemingly appear anywhere. Sometimes the door is in places it should not be. Sometimes it stands alone, attached to nothing at all. The one thing you are sure of is that it is the same door each time- one you have not yet been able to open.
""",
    """<b>Neural Superposition</b>: You see images of unknown places superposed onto this one, sometimes making it difficult to tell what is real. In another time you may have been called an oracle.<br>
When you roll DEX saves, roll 2d20 and take the lowest result. Once per day you see something significant (ask your Facilitator what it is).
""",
    """<b>Seventh Son of a Seventh Son</b>: Enough exposure has shifted and changed you. You are more connected to the otherworldly. Add Magic to your character sheet and follow the rules. This new power is great, and terrible.<br>
The first time you use a spell it causes 1d6 stress.<br>
Your second spell causes 1d4 stress<br>
Finally the third spell you cast causes 1 stress.
""",
    """<b>Marked by fear</b>: The core of your being has been twisted and changed. When you act in a way that manifests your marked fear and have to make a save, roll 2d20 and take the lowest result. When you resist an opportunity to indulge the fear, take 1d4 stress.<br>
Create a fundamental fear with your Facilitator.
""",
    """<b>Heavy is the head</b>: An ethereal crown hangs above your head. It is not visible to all, only a special few. Tales have been told of your coming.<br>
Make a CTRL save. If you pass, increase your max CTRL by 1d6.
""",
    """<b>Full to Bursting</b>: You have a feeling of fullness and contentment.<br>
Next time you would fail a critical damage STR save</b>:<br>
you succeed instead. Immediately and violently begin to vomit vermin (player’s choice).<br>
Any being that can see they must make a CTRL save or take 1d6 stress.<br>
Roll 3d6. If the total is higher than your max CTRL, take the new result.
""",
    """<b>Progeny</b>: Something is growing inside of you. Hope has long since abandoned it, and it has no more room for dreams.<br>
Roll 2d6. Take the new result as your max HP
""",
    """<b>Fate’s Web (this can only be taken once per character but multiple times per table)</b>: At least a puppet can see the strings that bind it, if only you were so lucky.<br>
Roll on the Magical Fallout Table - Omens and Magical Catastrophes.
""",
    """<b>The Hunt</b>: Patronage is a dangerous thing. It becomes harder to ignore the primal impulses that burn deep inside you. Your attacks are Enhanced Critical Damage mutilates your body but you can continue to act.<br>
You become the primary target of otherworldly and attacks made against you are Enhanced.
""",
    """<b>Doomed (this can be taken multiple times per character)</b>:<br>
You have been branded for sacrifice, anointed for doom. If your next critical save against damage is a failure, you die horribly. If it is a success, you roll 3d6 + the number of times you’ve taken Doomed. If the total is higher than your max HP, take the new result.""",
)

hungry_hollow_fallouts = (
    "<b>Fleshy Wax</b>: Your blood begins to thicken with a waxy substance. This fortifies your body against harm while making you less nimble. Reduce your DEX by d4 and increase your STR by d4.",
    "<b>Carrion Eater</b>: You hunger for raw meat. Consuming raw flesh instantly replenishes your HP, even when in a risky situation.",
    "<b>Failed Implantation</b> <em>(this Fallout requires proximity to a Parasite Bee that is trying to implant itself)</em>: The Bee’s implantation was unsuccessful, but its steady drip of neurotoxin continues, fortifying your body against foreign influence. Increase your CTRL by d4.",
    "<b>Hivemind</b>: A mass begins to grow at the base of your skull.  This growth acts as a conduit to the Hive Mind. You can hear their whispers and Apiarist Workers assume you are one of them at first.",
    "<b>Become One</b>: Something calls to you, and you feel a compulsion to join with the Hive. It is drawn to you as well.  Facilitator: PC has +1 Stability whenever in the presence of Brea or the God-Queen (p. 14).",
    "<b>Deadened Nerves</b>: Something inside you lets you push past your physical limits, but everything comes at a cost. You are no longer affected by Fatigue or Deprivation.",
    "<b>Scarred</b>: Every Wound you inflict on another mirrors itself upon your body, leaving a scar. The first time it happens, make a CTRL Save. If you pass, increase your max STR by d4.  table (this can be taken multiple times per character).",
)

fallouts = (legacy_fallouts, bloom_fallouts, hungry_hollow_fallouts)

fallouts_data = dict(zip(LIMINAL_HORROR_MODULES, fallouts))

fallouts_paragraphs = (
    """Some moments change an investigator forever. Players roll or choose from the
the Fallout table when the Investigator suffers Critical Stress.<br><b>Unless marked, the
Fallout can only be chosen once per table</b>.<br>Each Fallout takes up an Inventory
Slot. It cannot be removed.""",
    """Fallout represents the spreading fungal infection, the process by which a victim becomes a Host (p.14).
<br>Unless marked, Fallout entries can only be taken once per character.<br>
Fallout takes up an inventory slot and can only be removed under extenuating circumstances or death.""",
    """Fallout represents the spreading influence of <b>Trigona, God-Queen of the Flesh
Hive</b>.<br>Fallout entries can only be taken once per Investigator.<br>Each time a <em>Fallout</em>
is taken, it takes up an inventory slot and can only be removed under
extenuating circumstances or death.""",
)

FALLOUT_PARAGRAPH_DATA = dict(zip(LIMINAL_HORROR_MODULES, fallouts_paragraphs))


class Fallout:
    def __init__(self, module):
        self.description = choice(fallouts_data[module])
        # check if chance of getting base game fallout is rolled

        if module == LIMINAL_HORROR_MODULES[1]:
            r = randint(1, 10)
            if r == 10:
                self.description = choice(legacy_fallouts)

        elif module == LIMINAL_HORROR_MODULES[2]:
            r = randint(1, 8)
            if r == 8:
                self.description = choice(legacy_fallouts)

    def __repr__(self) -> str:
        return self.description
