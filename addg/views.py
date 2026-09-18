from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CharacterCreationForm
from .characters import Character
from .location_names import gen_address, get_bar_name

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


def addg_gen_address_view(request):
    template_name = "addg/random_address.html"
    context = {"address": gen_address()}
    return render(request, template_name, context)


def addg_get_bar_name_view(request):
    template_name = "addg/random_bar.html"
    context = {"bar": get_bar_name()}
    return render(request, template_name, context)
