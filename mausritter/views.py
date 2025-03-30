import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Creature

from .game_logic.colony import generate_colony_obj
from .game_logic.adventure_site import generate_adventure_site_obj
from .game_logic.npc import NPC_Mouse, hireling_stats, Hireling
from .game_logic.seeds import generate_seed_obj
from .game_logic.spells import generate_spell_obj, get_spell_list
from .game_logic.magic_sword import generate_magic_sword_obj
from .game_logic.pc import generate_mouse_pc_obj
from .game_logic.roll import roll_spell as rs

from .forms import TreasureForm, RollSpellForm
from .game_logic.treasure import generate_treasure_list


# Create your views here.
def index(request):
    return render(request, "mausritter/index.html")


def generate_colony(request):
    context = {"colony": generate_colony_obj()}
    return render(request, "mausritter/generate_colony.html", context)


def generate_adventure_site(request):
    context = {"site": generate_adventure_site_obj()}
    return render(request, "mausritter/generate_adventure_site.html", context)


def generate_npc_mouse(request):
    npc = NPC_Mouse()
    context = {"npc": npc}
    return render(request, "mausritter/generate_npc_mouse.html", context)


def generate_seed(request):
    straight_seed = generate_seed_obj(mix=False)
    mixed_seed = generate_seed_obj(mix=True)
    context = {
        "straight_seed": straight_seed,
        "mixed_seed": mixed_seed,
    }
    return render(request, "mausritter/generate_seed.html", context)


def generate_spell(request):
    context = {"spell": generate_spell_obj()}
    return render(request, "mausritter/generate_spell.html", context)


def generate_magic_sword(request):
    context = {"sword": generate_magic_sword_obj()}
    return render(request, "mausritter/generate_magic_sword.html", context)


def generate_mouse_pc(request):
    context = {"pc": generate_mouse_pc_obj()}
    return render(request, "mausritter/generate_mouse_pc.html", context)


def roll_treasure(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TreasureForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # retrieve the values from the form
            location = form.cleaned_data["location"]
            magical = form.cleaned_data.get("magical")
            beast = form.cleaned_data.get("beast")
            adversity = form.cleaned_data.get("adversity")
            # each question in the from that was True grants extra dice
            extra_dice = sum((location, magical, beast, adversity))
            treasure_list = generate_treasure_list(extra_dice=extra_dice)
            # build the context
            context = {
                "form": form,
                "treasure_list": treasure_list,
            }
            return render(request, "mausritter/roll_treasure.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {"form": TreasureForm()}
    return render(request, "mausritter/roll_treasure.html", context)


def roll_spell(request):
    if request.method == "POST":
        form = RollSpellForm(request.POST)

        if form.is_valid():
            n_dice = form.cleaned_data.get("n_dice")
            SUM, USES, MISCAST = rs(n_dice)
            context = {
                "form": form,
                "SUM": SUM,
                "USES": USES,
                "MISCAST": MISCAST,
            }
            return render(request, "mausritter/roll_spell.html", context)
        # if a GET (or any other method) we'll create a blank form
    else:
        context = {"form": RollSpellForm()}
    return render(request, "mausritter/roll_spell.html", context)


class CreatureListView(generic.ListView):
    model = Creature
    ordering = ["name"]


class CreatureDetailView(generic.DetailView):
    model = Creature

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["roll"] = random.randint(1, 6)
        return context


def spell_list_view(request):
    spells = get_spell_list()
    return render(
        request, template_name="mausritter/spell_list.html", context={"spells": spells}
    )


def hirelings_view(request):

    return render(
        request,
        template_name="mausritter/hirelings.html",
        context={"hireling_stats": hireling_stats, "hireling": Hireling()},
    )
