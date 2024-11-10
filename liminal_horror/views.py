from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character

# Create your views here.


class LiminalHorrorIndexView(TemplateView):
    template_name = "liminal_horror/index.html"


def bloom_character_creation_view(request):
    context = {"char": Character()}
    template_name = "liminal_horror/generate_character.html"
    return render(request, template_name, context)
