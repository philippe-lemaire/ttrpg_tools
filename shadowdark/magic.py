from .dice_tools import roll
from random import choice, sample

wizard_mishaps = {
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

witch_mishaps = {
    1: (
        "<b>Wither!</b> You take 1d6 damage per spell tier",
        "<b>Newt!</b> You turn into a tiny, 1 hit point newt for 3 rounds. You can't cast spells in this form",
        "<b>Shune's baleful gaze!</b> You can't cast this spell and another random spell again for a week",
        "<b>Thieving fairies!</b> You lose a random piece of gear",
        "<b>Cobwebs!</b> Mental cobwebs cloud your mind; you can't cast this spell again for a week",
        "<b>Cackles!</b> You fall to the ground in a fit of cackling, unable to do anything but laugh for the next 3 rounds",
        "<b>Double trouble!</b> You lose the ability to cast a random spell until you complete a rest",
        "<b>Swamp gas!</b> The air fills with sulfurous gas in a near-sized cube around you. All creatures who end their turn in it are blinded and take 1d6 damage. It lasts 3 rounds",
        "<b>Bat!</b> An angry bat appears on your head, flapping and clinging to your face. You are blinded for 3 rounds or until you can toss the beastie away from you",
        "<b>Salt!</b> You're surrounded by a ring of salt and can't touch it or pass through it until something breaks the ring",
        "<b>Siphon!</b> You have disadvantage on casting spells of the same tier or lower for the next 10 rounds",
    ),
    2: (
        "<b>Ruin!</b> You take 1d8 damage per spell tier",
        "<b>Mind rot!</b> You permanently forget one random spell",
        "<b>4The Willowman!</b> You summon The Willowman (who is angry with you) in a space near to you. He stays for 1d6 rounds before disappearing from whence he came",
        "<b>Accursed imps!</b> Cackling imps from hell swarm you, stealing three pieces of random gear and flapping away",
        "<b>Lightning blast!</b> You deal 3d6 damage to yourself and all creatures within near",
        "<b>Cold iron!</b> Spikes of cold iron lance from the ethereal realm, piercing you. You take 2d6 damage and are paralyzed for 2 rounds",
        "<b>Mother of Night!</b> You displease the Dark Mother and lose the ability to cast this spell until atoning to her",
        "<b>Catatonia!</b> You stare blankly and can't take any actions for the next hour",
        "<b>Tongue of dog!</b> Your tongue lolls every time you try to cast a spell of a random tier, ruining the magic. This persists until you complete a rest",
        "<b>Fiddlesticks!</b> You have disadvantage on casting all spells for the next 10 rounds",
        "<b>Nemesis!</b> Somewhere, a child is born who will grow up to become a mighty, sworn enemy to you",
    ),
}


def roll_mishap(spell_tier, class_):
    r = roll("1d12")
    if class_ == "wizard":
        if spell_tier in (1, 2):
            table = 2
        elif spell_tier in (3, 4):
            table = 4
        else:
            table = 5
        if r == 1:
            return "<br/>".join(sample(wizard_mishaps.get(table), 2))
        return choice(wizard_mishaps.get(table))
    if class_ == "witch":
        if spell_tier <= 3:
            table = 1
        else:
            table = 2
        if r == 1:
            return "Diablerie!<br/>".join(sample(witch_mishaps[table], 2))
        return choice(witch_mishaps.get(table))


def cast_a_spell(bonus, spell_tier, class_, advantage=False, disadvantage=False):
    """Take bonus to cast and spell tier and return crit, mishap, natural roll, total value, success, outcome"""
    rolls = [roll("1d20") for _ in range(2)]
    if advantage and not disadvantage:
        r = max(rolls)
    elif disadvantage and not advantage:
        r = min(rolls)
    else:
        _ = rolls.pop()
        r = rolls[0]
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
    elif mishap and class_ in ("wizard", "witch"):
        outcome = "<b>Mishap!</b>" + "<br/>" + roll_mishap(spell_tier, class_)
    elif mishap and class_ == "priest":
        outcome = """<b>Mishap!</b> Your deity is greatly displeased and revokes its power.
        You can’t cast that spell again until you complete ritualistic
        penance to your deity and successfully complete a rest."""
    elif success:
        outcome = "You cast the spell, good job!"
    else:
        outcome = "You failed to cast the spell! You can't cast it again until you complete a rest."
    return crit, mishap, r, total, success, outcome, rolls
