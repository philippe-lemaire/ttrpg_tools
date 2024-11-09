from django.shortcuts import render
from . import game_logic
from django.views import generic

# Create your views here.


class IntoTheOddIndexView(generic.TemplateView):
    template_name = "into_the_odd/index.html"


def create_character(request):
    context = {
        "character": game_logic.Character(),
        "companions": [game_logic.Companion() for _ in range(2)],
        "type": "Adventurer",
    }
    return render(
        request, template_name="into_the_odd/create_character.html", context=context
    )


def create_lackeys(request):
    context = {"lackeys": [game_logic.Companion() for _ in range(3)], "type": "lackey"}
    return render(
        request, template_name="into_the_odd/create_lackeys.html", context=context
    )


def create_mutant_character(request):
    context = {"character": game_logic.MutantCharacter(), "type": "Mutant"}
    return render(
        request,
        template_name="into_the_odd/create_mutant_character.html",
        context=context,
    )


def create_unhuman_character(request):
    context = {
        "character": game_logic.UnhumanCharacter(),
        "type": "Unhuman",
    }

    return render(
        request,
        template_name="into_the_odd/create_unhuman_character.html",
        context=context,
    )


def create_simple_folk_character(request):
    context = {
        "character": game_logic.SimpleFolkCharacter(),
        "companion": game_logic.Companion(),
        "type": "Simple Folk",
    }
    return render(
        request, template_name="into_the_odd/create_character.html", context=context
    )


def create_npc(request):
    context = {"npc": game_logic.NPC()}
    return render(
        request, template_name="into_the_odd/create_npc.html", context=context
    )


def create_island(request):
    context = {"island": game_logic.Island()}
    return render(
        request, template_name="into_the_odd/create_island.html", context=context
    )


def council_decision(request):
    context = {"council": game_logic.Council()}
    return render(
        request, template_name="into_the_odd/council_action.html", context=context
    )


def create_street(request):
    context = {"street": game_logic.Street()}
    return render(
        request, template_name="into_the_odd/create_street.html", context=context
    )


def create_route(request):
    context = {"route": game_logic.Route()}
    return render(
        request, template_name="into_the_odd/create_route.html", context=context
    )


def create_business(request):
    context = {"business": game_logic.Business()}
    return render(
        request, template_name="into_the_odd/create_business.html", context=context
    )


def create_creature(request):
    context = {"creature": game_logic.WeirdCreature()}
    return render(
        request, template_name="into_the_odd/create_creature.html", context=context
    )


def create_astral_cult(request):
    context = {"cults": [game_logic.AstralCult() for _ in range(3)]}
    return render(
        request, template_name="into_the_odd/create_astral_cult.html", context=context
    )


def create_beyond(request):
    return render(
        request,
        template_name="into_the_odd/create_beyond.html",
        context={"beyond": game_logic.Beyond()},
    )


def i_eat_the_stuff(request):
    return render(
        request,
        "into_the_odd/i_eat_the_stuff.html",
        context={"effect": game_logic.eat_the_stuff()},
    )


def is_this_thing_an_arcanum(request):
    return render(
        request,
        "into_the_odd/is_this_thing_an_arcanum.html",
        context={"thing": game_logic.Thing()},
    )
