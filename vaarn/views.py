from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Creature
from .game_logic.character_generator import Character
from .game_logic.hypergeometry import gen_hypergeometry_mishap, gen_codex
from .game_logic.mutations import get_mutations_list
from .forms import AncestryForm, FollowerForm
from .game_logic.character_generator import Character
from .game_logic.wounds import biological_wounds, synthetic_wounds
from .game_logic.follower import gen_follower
from .game_logic.mercenary import gen_mercenary
from .game_logic.cybernetics import get_cybernetic_implants_list
from .game_logic.exotica import get_exotica_list
from .game_logic.neobloom import get_bloomboons_list
from .game_logic.settlements import gen_settlement
from .game_logic.npc import gen_npc
from .game_logic.region import gen_region
from random import randint

# Create your views here.


class IndexView(TemplateView):
    template_name = "vaarn/index.html"


def vaarn_character_creation_view(request, ancestry=None):
    context = {"character": Character(ancestry)}
    template_name = "vaarn/character_creation.html"
    return render(request, template_name, context)


def vaarn_character_creation_chosing_ancestry(request):
    form = AncestryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ancestry = form.cleaned_data["ancestry"]
            return vaarn_character_creation_view(request, ancestry)
    return render(
        request,
        template_name="vaarn/generate_with_ancestry.html",
        context={"form": form},
    )


def vaarn_gen_codex_view(request):
    context = {"codex": gen_codex()}
    template_name = "vaarn/codex.html"
    return render(request, template_name, context)


def vaarn_hypergeometry_mishap_view(request):
    context = {"mishap": gen_hypergeometry_mishap()}
    template_name = "vaarn/mishap.html"
    return render(request, template_name, context)


def vaarn_biological_wounds_view(request):
    context = {"wounds": biological_wounds, "wound_table": "Biological"}
    template_name = "vaarn/wounds.html"
    return render(request, template_name, context)


def vaarn_synthetic_wounds_view(request):
    context = {"wounds": synthetic_wounds, "wound_table": "Synthetic"}
    template_name = "vaarn/wounds.html"
    return render(request, template_name, context)


def vaarn_generate_follower_view(request):
    form = FollowerForm(request.POST or None)
    context = {"form": form, "retainer_type": "Follower"}
    template_name = "vaarn/generate_follower.html"
    if request.method == "POST":
        if form.is_valid():
            ego = form.cleaned_data["ego"]
            context.update({"follower": gen_follower(ego=ego)})
    return render(request, template_name, context)


def vaarn_generate_mercenary_view(request):
    form = FollowerForm(request.POST or None)  # reuse the same form?
    context = {"form": form, "retainer_type": "Mercenary"}
    template_name = "vaarn/generate_follower.html"  # reuse the same template?
    if request.method == "POST":
        if form.is_valid():
            ego = form.cleaned_data["ego"]
            context.update({"follower": gen_mercenary(ego=ego)})
    return render(request, template_name, context)


def vaarn_cybernetic_implants(request):
    context = {"implants": get_cybernetic_implants_list(), "r": randint(1, 20)}
    template_name = "vaarn/cybernetic_implants.html"
    return render(request, template_name, context)


def vaarn_exotica(request):
    context = {"exoticas": get_exotica_list(), "r": randint(1, 20)}
    template_name = "vaarn/exotica.html"
    return render(request, template_name, context)


def vaarn_bloomboons(request):
    context = {"bloomboons": get_bloomboons_list(), "r": randint(1, 20)}

    template_name = "vaarn/bloomboons.html"
    return render(request, template_name, context)


def vaarn_get_mutation_view(request):
    context = {"mutations": get_mutations_list(), "r": randint(1, 100)}
    template_name = "vaarn/mutations.html"
    return render(request, template_name, context)


def vaarn_roll_settlement_view(request):
    context = {"settlement": gen_settlement()}
    template_name = "vaarn/settlement.html"
    return render(request, template_name, context)


def vaarn_roll_npc_view(request):
    context = {"npc": gen_npc()}
    template_name = "vaarn/npc.html"
    return render(request, template_name, context)


def vaarn_roll_region_view(request):
    n = 6
    context = {"region": gen_region(n), "n": n}
    template_name = "vaarn/region.html"
    return render(request, template_name, context)


class VaarnBestiaryList(ListView):
    model = Creature


class VaarnBestiaryDetail(DetailView):
    model = Creature
