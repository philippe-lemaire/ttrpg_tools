from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .game_logic.character_generator import Character

# Create your views here.


class IndexView(TemplateView):
    template_name = "vaarn/index.html"


def vaarn_character_creation_view(request):
    context = {"character": Character()}
    template_name = "vaarn/character_creation.html"
    return render(request, template_name, context)
