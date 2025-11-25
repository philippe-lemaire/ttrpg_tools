from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .game_logic.character_generator import Character
from .game_logic.hypergeometry import gen_hypergeometry_mishap, gen_codex
from .game_logic.mutations import get_mutations
from .forms import AncestryForm
from .game_logic.character_generator import Character
from .game_logic.wounds import biological_wounds, synthetic_wounds

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


def vaarn_get_mutation_view(request):
    context = {"mutation": get_mutations(1).pop()}
    template_name = "vaarn/mutations.html"
    return render(request, template_name, context)


def vaarn_biological_wounds_view(request):
    context = {"wounds": biological_wounds, "wound_table": "Biological"}
    template_name = "vaarn/wounds.html"
    return render(request, template_name, context)


def vaarn_synthetic_wounds_view(request):
    context = {"wounds": synthetic_wounds, "wound_table": "Synthetic"}
    template_name = "vaarn/wounds.html"
    return render(request, template_name, context)
