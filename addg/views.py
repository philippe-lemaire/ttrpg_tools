from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CharacterCreationForm
from .characters import Character

# Create your views here.


class AddgIndexView(TemplateView):
    template_name = "addg/index.html"


def addg_character_generation_view(request):
    template_name = "addg/character_generator.html"
    form = CharacterCreationForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            stat_array_nb = form.cleaned_data["stat_array_nb"]
            ability_to_raise = form.cleaned_data["ability_to_raise"]
            gender = form.cleaned_data["gender"]
            character = Character(stat_array_nb, ability_to_raise, gender)
            context["character"] = character
    return render(request, template_name, context)
