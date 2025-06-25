from .dice_tools import roll
from random import choice, sample

mishaps = {
    2: (
        "<b>Explosion!</b> You take 1d8 damage",
        "<b>Refraction!</b> You target yourself with the spell",
        "<b>Your hand slipped!</b> You target a random ally with the spell",
        "<b>Mind wound!</b> You can't cast this spell again for a week",
        "<b>Discorporation!</b> One random piece of your gear disappears forever",
        "<b>Spell worm!</b> You lose the ability to cast a random spell on each of your turns until you pass a DC 12 Constitution check. You regain the ability to cast those spells after completing a rest",
        "<b>Harmonic failure!</b> You lose the ability to cast a random spell until you complete a rest",
        "<b>Poof!</b> You suppress all light within a near distance from you, including sunlight and magical light, for 10 rounds",
        "<b>The horror!</b> You scream uncontrollably for 3 rounds in Primordial, drawing lots of attention",
        "<b>Energy surge!</b> You glow bright purple for 10 rounds, granting enemies advantage on attacks against you",
        "<b>Unstable conduit!</b> You have disadvantage on casting spells of the same tier for 10 rounds",
    ),
    4: (
        "<b>Blast radius!</b> You and all near creatures take 2d6 damage",
        "<b>Duplicate refraction!</b> You target yourself and the nearest ally with two identical copies of the spell",
        "<b>You flubbed the incantation!</b> You cast a random spell from your known spells at the same targets, even if it would not normally be possible",
        "<b>Ethereal bandersnatch!</b> Two random pieces of your gear disappear forever",
        "<b>Arcano-mutagenesis!</b> You must pass a DC 12 Constitution check or a random stat drops to 3 (-4) until you successfully complete a rest",
        "<b>Boom!</b> You open a 30-foot deep sinkhole in the ground with you at the center. You and all near creatures must pass a DC 15 Dexterity check or fall in",
        "<b>Petrification!</b> 1d4 of your limbs petrify for the next 24 hours",
        "<b>Stupefaction!</b> You lose the ability to cast all spells of the same tier until you complete a rest",
        "<b>It cannot be unseen!</b> You must pass a DC 12 Wisdom check or descend into mad raving for 1d10 rounds",
        "<b>Radioactive energies!</b> You whirl with repulsive energies, drawing the hostility and attacks of all enemies who can see you for the next 1d4 rounds",
        "<b>Uncontained channeling!</b> You have disadvantage on casting spells of the same tier and lower for 10 rounds",
    ),
    5: (
        "<b>Pyroclastic extrusion!</b> You deal 3d8 damage to yourself and all near creatures",
        "<b>Astral incision!</b> An otherworldly blade cuts into your memory. You permanently forget one random spell",
        "<b>The grimlow!</b> You accidentally summon a hostile grimlow in a space near to you. It persists for 2d4 rounds before disappearing whence it came",
        "<b>Dark plasma aura!</b> Attacks against you pass through a vile aura, dealing double damage for the next 2d6 rounds",
        "<b>Gate!</b> You open a magic portal to another location, whether on this plane or another. Something dreadful will come through in 1d4 rounds unless you close it with a DC 18 Intelligence check on your turn",
        "<b>Runaway arcana loop!</b> Your spell targets a random creature you can see, even if it would not normally be possible. Each subsequent turn, you must pass a spellcasting check for that spell or you cast it on another random creature in the same way (effect ends on success)",
        "<b>Arcane obstruction!</b> You lose the ability to cast all spells of a random tier until you complete a rest ",
        "<b>What lurks beyond the veil!</b> You must pass a DC 15 Wisdom check or fall into mad raving for 1d4 hours",
        "<b>Ord's balance!</b> You must either permanently sacrifice a magic item or the ability to cast a tier 3+ spell you know ",
        "<b>Unmitigated chain reaction!</b> You have disadvantage on casting all spells for the next 10 rounds",
        "<b>Shred!</b> You tear a large hole in the fabric of the universe close to you; the lightless tear grows larger every round",
    ),
}


def roll_mishap(spell_tier):
    r = roll("1d12")
    if spell_tier in (1, 2):
        table = 2
    elif spell_tier in (3, 4):
        table = 4
    else:
        table = 5
    if r == 1:
        return "<br/>".join(sample(mishaps.get(table), 2))
    return choice(mishaps.get(table))


def cast_a_spell(bonus, spell_tier, class_):
    """Take bonus to cast and spell tier and return crit, mishap, natural roll, total value, success, outcome"""
    r = roll("1d20")
    crit = False
    mishap = False
    if r == 20:
        crit = True
    if r == 1:
        mishap = True
    total = r + bonus
    success = total >= 10 + spell_tier or crit
    if mishap:
        success = False
    if crit:
        outcome = "<b>Critical Success!</b> Double one numeric value of the Spell."
    elif mishap and class_ == "wizard":
        outcome = "<b>Mishap!</b>" + "<br/>" + roll_mishap(spell_tier)
    elif mishap and class_ == "priest":
        outcome = """<b>Mishap!</b> Your deity is greatly displeased and revokes its power.
        You can’t cast that spell again until you complete ritualistic
        penance to your deity and successfully complete a rest."""
    elif success:
        outcome = "You cast the spell, good job!"
    else:
        outcome = "You failed to cast the spell! You can't cast it again until you complete a rest."
    return crit, mishap, r, total, success, outcome
