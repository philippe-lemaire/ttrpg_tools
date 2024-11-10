from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character
from .fallout import Fallout

# Create your views here.


class LiminalHorrorIndexView(TemplateView):
    template_name = "liminal_horror/index.html"


def bloom_character_creation_view(request):
    context = {"char": Character()}
    template_name = "liminal_horror/generate_character.html"
    return render(request, template_name, context)


def bloom_fallout_view(request):
    context = {"fallout": Fallout()}
    template_name = "liminal_horror/fallout.html"
    return render(request, template_name, context)
