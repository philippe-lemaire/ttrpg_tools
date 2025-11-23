from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .game_logic.character_generator import Character
from .game_logic.hypergeometry import gen_hypergeometry_mishap, gen_codex

# Create your views here.


class IndexView(TemplateView):
    template_name = "vaarn/index.html"


def vaarn_character_creation_view(request):
    context = {"character": Character()}
    template_name = "vaarn/character_creation.html"
    return render(request, template_name, context)


def vaarn_gen_codex_view(request):
    context = {"codex": gen_codex()}
    template_name = "vaarn/codex.html"
    return render(request, template_name, context)


def vaarn_hypergeometry_mishap_view(request):
    context = {"mishap": gen_hypergeometry_mishap()}
    template_name = "vaarn/mishap.html"
    return render(request, template_name, context)
