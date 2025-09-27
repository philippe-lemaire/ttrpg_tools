from django.shortcuts import render
from .gamelogic.character import Character
from django.views.generic import TemplateView
from .forms import EncounterForm
from .gamelogic.encounters import type_roller, Encounter


def create_character(request):
    template_name = "dolmenwood/create_character.html"
    context = {"char": Character}
    return render(request, template_name, context)


class DolmenwoodIndexview(TemplateView):
    template_name = "dolmenwood/index.html"


def roll_encounter(request):
    form = EncounterForm(request.POST or None)
    context = {"form": form}
    template_name = "dolmenwood/encounters.html"
    if request.method == "POST":
        if form.is_valid():
            situation = form.cleaned_data["situation"]
            type_ = type_roller(situation)
            region = form.cleaned_data.get("region")
            print(region)
            context["type"] = type_
            context["encounter"] = Encounter(type_, region)
    return render(request, template_name, context)
