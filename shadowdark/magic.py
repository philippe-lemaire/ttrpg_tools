from .dice_tools import roll


def cast_wizard(bonus, spell_tier):
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
        outcome = "Critical Success! Double one numeric value of the Spell."
    elif mishap:
        outcome = "Mishap!"  # TODO + roll_mishap(spell_tier)
    elif success:
        outcome = "You cast the spell, good job!"
    else:
        outcome = "You failed to cast the spell! You can't cast it again until you complete a rest."
    return crit, mishap, r, total, success, outcome
