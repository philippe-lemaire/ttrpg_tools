from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character
from .forms import BackgroundForm
from .game_logic import dungeon_events, wilderness_events
from .roll import roll


# Create your views here.
class CairnIndexView(TemplateView):
    template_name = "cairn/index.html"


def generate_character(request, background=None):
    return render(
        request,
        template_name="cairn/generate_character.html",
        context={"char": Character(background)},
    )


def generate_with_background(request):
    form = BackgroundForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            background = form.cleaned_data["background"]
            return generate_character(request, background)
    return render(
        request,
        template_name="cairn/generate_with_background.html",
        context={"form": form},
    )


def dungeon_events_view(request):
    context = {"dungeon_events": dungeon_events, "roll": roll("1d6")}
    template_name = "cairn/dungeon_events.html"
    return render(request, template_name, context)


def wilderness_events_view(request):
    context = {"wilderness_events": wilderness_events, "roll": roll("1d6")}
    template_name = "cairn/wilderness_events.html"
    return render(request, template_name, context)


def reaction_roll_view(request):
    # spread a 2d6 roll onto the 5 results 0 to 4
    context = {"r": roll("2d6") // 3}
    template_name = "cairn/reaction_roll.html"
    return render(request, template_name, context)
