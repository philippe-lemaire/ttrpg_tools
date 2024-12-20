from random import choice

from django.shortcuts import render
from django.views.generic import TemplateView
from mothership.character import Character, classes_descriptions_d
from .roll import roll, roll_pc_stats_and_saves, roll_d100, get_key
from mothership.forms import ClassesForm
from .forms import LevelForm, RegionSelectForm, RegionSelectFormHuntAndGather
from .land_of_cicada_encounters import cloud_empress_encounters, moods
from .land_of_cicadas_hunt_and_gather import Hunt_and_gather_result
from .game_logic import (
    roll_byway,
    Settlement,
    Guild,
    Mystling,
    Cavern,
    roll_mine,
    roll_exit,
    Encounter,
)

from .unseen_city_tables import spell_dict

# TODO : create this modules own character and forms
# Create your views here.


class CloudEmpressIndexView(TemplateView):
    template_name = "cloudempress/index.html"


def create_character(request):
    context = roll_pc_stats_and_saves()
    request.session.update(context)
    context["form"] = ClassesForm
    context["classes_descriptions"] = classes_descriptions_d

    return render(
        request,
        template_name="cloudempress/create_character.html",
        context=context,
    )


def create_character_step_2(request):
    form = ClassesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            class_ = form.cleaned_data["class_choice"]
            # create character with stats in session
            strength = request.session.get("strength", 0)
            speed = request.session.get("speed", 0)
            intellect = request.session.get("intellect", 0)
            combat = request.session.get("combat", 0)
            sanity = request.session.get("sanity", 0)
            fear = request.session.get("fear", 0)
            body = request.session.get("body", 0)
            health = roll("1d10") + 10
            wounds = 2

            character = Character(
                strength=strength,
                speed=speed,
                intellect=intellect,
                combat=combat,
                sanity=sanity,
                fear=fear,
                body=body,
                class_=class_,
                max_wounds=wounds,
                wounds=0,
                health=health,
                max_health=health,
                stress=2,
                minimum_stress=2,
                trauma_response=classes_descriptions_d.get(class_)[1],
                skills=[],
                trinket=[],
                patch=[],
                equipment=[],
                credits=roll("2d10") * 10,
                portrait="",
                name="",
                pronouns="",
            )

            # TODO update character stats depending on class
            character.update_stats()

            context = {"character": character}

            context["classes_descriptions"] = classes_descriptions_d
            return render(
                request,
                template_name="cloudempress/create_character.html",
                context=context,
            )

    return render(
        request,
        template_name="cloudempress/create_character.html",
        context={"form": form},
    )


def create_byway(request):
    context = {"byway": roll_byway()}
    return render(request, template_name="cloudempress/byway.html", context=context)


def roll_settlement(request):
    context = {"settlement": Settlement()}
    return render(request, "cloudempress/settlement.html", context)


def roll_guild(request):
    context = {"guild": Guild()}
    return render(request, "cloudempress/guild.html", context)


def roll_forgotten_mine(request):
    context = {"forgotten_mine": roll_mine()}
    return render(request, "cloudempress/forgotten_mine.html", context)


def roll_mystling(request):
    context = {"mystling": Mystling()}
    return render(request, "cloudempress/mystling.html", context)


def get_exit(request):
    context = {"exit": roll_exit()}
    return render(request, "cloudempress/exit.html", context)


def roll_cavern(request):
    form = LevelForm(request.POST or None)
    template_name = "cloudempress/cavern.html"
    if request.method == "POST":
        # catch level in the form
        if form.is_valid():
            level = form.cleaned_data["level"]
            level = int(level)
            context = {"cavern": Cavern(level=level), "form": form, "level": level}

            return render(request, template_name, context)
    return render(request, template_name, {"form": form})


def roll_encounter_unseen_city(request):
    return render(request, "cloudempress/encounter.html", {"encounter": Encounter()})


def spells_view(request):
    context = {"roll": roll("2d5"), "spells": spell_dict}
    return render(request, "cloudempress/unseen-city-spells.html", context)


def roll_encounter_land_of_cicadas(request):
    template_name = "cloudempress/roll_encounters_land_of_cicadas.html"
    form = RegionSelectForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            region = form.cleaned_data["region"]
            n = roll_d100()
            encounter_table = cloud_empress_encounters.get(region)
            k = get_key(n, encounter_table)
            encounter = encounter_table[k]
            context["encounter"] = encounter
            context["mood"] = choice(moods)
            context["encounter_rolled"] = True
    else:
        context["encounter_rolled"] = False
    return render(request, template_name, context)


def roll_hunt_and_gather_land_of_cicadas(request):
    template_name = "cloudempress/roll_hunt_and_gather_land_of_cicadas.html"
    form = RegionSelectFormHuntAndGather(request.POST or None)
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            region = form.cleaned_data["region"]
            context["result"] = Hunt_and_gather_result(region)
    else:
        context["result"] = None
    return render(request, template_name, context)
