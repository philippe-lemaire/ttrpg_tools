from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from random import choice
from .npc_names import gen_npc_name, gen_npc_name_by_syllables
from .chargen import roll_stats
from .forms import (
    ClassChoiceForm,
    SpellCastingForm,
    CharismaModForm,
    CarousingBonusForm,
    RandomTableSelection,
    AncestryChoiceForm,
)
from .chargen import PC_Character
from .game_facts import talents_dict
from .magic import cast_a_spell
from .encounters import gen_encounter
from .random_tables import TABLES
from .carousing import carousing_outcomes
from .dice_tools import get_closest_key, roll

# Create your views here.


class IndexView(TemplateView):
    template_name = "shadowdark/index.html"


class HexCrawlingView(TemplateView):
    template_name = "shadowdark/hexcrawling.html"


def npc_name(request):
    form = AncestryChoiceForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            ancestry = form.cleaned_data["ancestry"]
            print(ancestry)
            context["name"] = gen_npc_name(ancestry)

    return render(
        request,
        template_name="shadowdark/npc_names.html",
        context=context,
    )


def cast_wizard_spell_view(request):
    form = SpellCastingForm(request.POST or None)
    template_name = "shadowdark/cast_a_spell.html"
    context = {"form": form}
    if form.is_valid():
        bonus = form.cleaned_data["bonus"]
        spell_tier = form.cleaned_data["spell_tier"]
        class_ = form.cleaned_data["class_"]
        advantage = form.cleaned_data["advantage"]
        disadvantage = form.cleaned_data["disadvantage"]
        crit, mishap, r, total, success, outcome, rolls = cast_a_spell(
            bonus, spell_tier, class_, advantage, disadvantage
        )
        context.update(
            {
                "roll_done": True,
                "crit": crit,
                "mishap": mishap,
                "r": r,
                "rolls": rolls,
                "total": total,
                "success": success,
                "outcome": outcome,
                "bonus": bonus,
                "advantage": advantage,
                "disadvantage": disadvantage,
            }
        )
    return render(request, template_name, context)


def encounter_view(request):
    form = CharismaModForm(request.POST or None)
    context = {
        "form": form,
    }
    template_name = "shadowdark/encounters.html"

    if request.method == "POST":
        if form.is_valid():
            charisma_mod = int(form.cleaned_data["bonus"])
            context["encounter"] = gen_encounter(charisma_mod)
    return render(request, template_name, context)


def carousing_view(request):
    form = CarousingBonusForm(request.POST or None)
    context = {
        "form": form,
    }
    template_name = "shadowdark/carousing.html"

    if request.method == "POST":
        if form.is_valid():
            bonus = int(form.cleaned_data["bonus"])
            r = roll("1d8") + bonus
            if r > 14:
                r = 14
            context["roll"] = r
            context["carousing_table"] = carousing_outcomes
    return render(request, template_name, context)


def roll_random_table_view(request):
    form = RandomTableSelection(request.POST or None)
    template_name = "shadowdark/random_tables.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            table_name = form.cleaned_data["table"]
            table = TABLES.get(table_name)
            result = choice(table)
            context["result"] = result
    return render(request, template_name, context)


from .forms import get_zone_form
from .encounters import encounters_per_zone, zones_per_region


def select_zone_type_view(request, region):

    form = get_zone_form(region)(request.POST or None)

    template_name = "shadowdark/select_zone.html"
    context = {
        "form": form,
        "region": region,
    }
    if request.method == "POST":
        if form.is_valid():
            zone = form.cleaned_data["zone"]
            encounter_types = zones_per_region.get(region).get(zone)
            r = roll("1d8")
            encounter_type = get_closest_key(r, encounter_types)
            encounter = choice(encounters_per_zone.get(region)[encounter_type])
            context["encounter_type"] = encounter_type
            context["encounter"] = encounter
    return render(request, template_name, context)


from .forms import AreaChoiceForm
from .encounters import core_encounter_tables


def core_book_encounters(request):
    form = AreaChoiceForm(request.POST or None)
    template_name = "shadowdark/core_book_encounters.html"
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            area = form.cleaned_data["area"]
            charisma_mod = int(form.cleaned_data["bonus"])
            context["encounter"] = gen_encounter(charisma_mod)
            r = roll("1d100")
            context["encounter_detail"] = get_closest_key(
                r, core_encounter_tables.get(area)
            )
    return render(request, template_name, context)


from .forms import TreasureLevelChoiceForm
from .treasure import treasure_tables


def roll_treasure_view(request):
    template_name = "shadowdark/roll_treasure.html"
    form = TreasureLevelChoiceForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            level = form.cleaned_data["level"]
            r = roll("1d100")
            treasure = get_closest_key(r, treasure_tables.get(level))
            context["treasure"] = treasure
    return render(request, template_name, context)
