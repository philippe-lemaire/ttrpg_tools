from django.shortcuts import render, redirect
from django.views import generic
from .models import Monster
from .hoard_treasure import roll_hoard, types, expand_result
from .adventuring_parties import roll_adventuring_party
from .forms import AdventuringPartyForm, DeckofManyThingsForm, HereticGnomesForm
from django.views.generic import TemplateView
from .magic_items import *
from .figurines import Figurine
from .heretic_gnomes import get_gnomes

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "ose/index.html"


class MonsterListView(generic.ListView):
    model = Monster
    ordering = ["name"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the hit_dice values for the filter
        context["hit_dice_values"] = list(range(1, 21))
        return context


def filtered_monster_list(request, hit_dice):
    queryset = Monster.objects.filter(hit_dice__regex=f"^{hit_dice}\D")
    return render(
        request,
        "ose/monster_list.html",
        {"monster_list": queryset, "hit_dice_values": list(range(1, 21))},
    )


class MonsterDetailView(generic.DetailView):
    model = Monster


class Hoard_index(TemplateView):
    template_name = "ose/hoards.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the hit_dice values for the filter
        context["types"] = types
        return context


def hoard_result(
    request,
    type_,
):

    if " " in type_:
        type_ = type_.split()[0]

    context = {"rolled_hoard": expand_result(roll_hoard(type_), level=1)}
    context["types"] = types
    context["type_called"] = type_

    return render(request, "ose/hoards.html", context)


def adventuring_party_view(request):

    if request.method == "POST":
        form = AdventuringPartyForm(request.POST)
        # check if it's valid
        if form.is_valid():

            level = form.cleaned_data["level"]
            party = roll_adventuring_party(level)

            treasure = expand_result(roll_hoard("type_u"), level=1)

            treasure = treasure + expand_result(roll_hoard("type_v"), level=1)

            treasure = treasure.replace("</ul><ul>", "")

            context = {
                "form": form,
                "party": party,
                "treasure": treasure,
                "level": level,
            }

    else:
        context = {"form": AdventuringPartyForm()}

    return render(request, "ose/adventuring_party.html", context)


def deck_of_many_things(request):
    if request.method == "POST":
        form = DeckofManyThingsForm(request.POST)
        if form.is_valid():
            ncards = form.cleaned_data["ncards"]
            deck = DeckofManyThings()
            cards = deck.draw(ncards)
            context = {"deck": deck, "cards": cards, "form": form}
    else:
        form = DeckofManyThingsForm()
        context = {"form": form}
    return render(request, "ose/deck_of_many_things.html", context)


def alchemist_beaker(request):
    context = {"item": AlchemistBeaker()}
    return render(request, "ose/alchemist_beaker.html", context)


def figurine_view(request):
    context = {"figurine": Figurine()}
    return render(request, "ose/figurine.html", context)


def heretic_gnomes_view(request):
    if request.method == "POST":
        form = HereticGnomesForm(request.POST)
        gnomes = get_gnomes()
        if form.is_valid():
            ngnomes = form.cleaned_data["ngnomes"]
            rolled_gnomes = random.sample(gnomes, ngnomes)
            context = {"gnomes": rolled_gnomes, "form": form}
    else:
        form = HereticGnomesForm()
        context = {"form": form}
    return render(request, "ose/heretic_gnomes.html", context)
