from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .npc_names import gen_npc_name, gen_npc_name_by_syllables
from .chargen import roll_stats
from .forms import ClassChoiceForm, SpellCastingForm
from .chargen import PC_Character
from .game_facts import talents_dict
from .magic import cast_a_spell

# Create your views here.


class IndexView(TemplateView):
    template_name = "shadowdark/index.html"


def npc_name(request):
    gen_name = gen_npc_name_by_syllables()

    ancestries = ["Dwarf", "Elf", "Goblin", "Halfling", "Half-Orc", "Human"]
    name_per_ancestry = {anc: gen_npc_name(anc) for anc in ancestries}

    return render(
        request,
        template_name="shadowdark/npc_names.html",
        context={"gen_name": gen_name, "names_dict": name_per_ancestry},
    )


def get_stats(request):
    stats, best = roll_stats()
    context = {"stats": stats, "best": best, "form": ClassChoiceForm()}
    request.session["stats_d"] = stats
    request.session["character"] = {}
    return render(request, template_name="shadowdark/get_stats.html", context=context)


def create_PC(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClassChoiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ancestry = int(form.cleaned_data.get("ancestry"))
            background = int(form.cleaned_data.get("background"))
            class_ = int(form.cleaned_data.get("class_"))
            stats_d = request.session.get("stats_d")
            character = PC_Character(
                stats_d,
                ancestry,
                background,
                class_,
                known_talents=[],
                first_creation=True,
            )
            stats_zip = character.get_stats()
            talents = talents_dict.get(character.class_)
            request.session["character"] = character.save()

            return render(
                request,
                template_name="shadowdark/display_character.html",
                context={
                    "character": character,
                    "stats_zip": stats_zip,
                    "talents": talents,
                },
            )
    else:
        return redirect(get_stats)


def level_up_PC(request):
    char_values = request.session.get("character")

    if not char_values:
        return redirect(get_stats)
    character = PC_Character(**char_values, first_creation=False)
    character.level_up()
    request.session["character"] = character.save()
    stats_zip = character.get_stats()
    talents = talents_dict.get(character.class_)

    return render(
        request,
        template_name="shadowdark/display_character.html",
        context={
            "character": character,
            "stats_zip": stats_zip,
            "talents": talents,
        },
    )


def cast_wizard_spell_view(request):
    form = SpellCastingForm(request.POST or None)
    template_name = "shadowdark/cast_a_spell.html"
    context = {"form": form}
    if form.is_valid():
        bonus = form.cleaned_data["bonus"]
        spell_tier = form.cleaned_data["spell_tier"]
        class_ = form.cleaned_data["class_"]
        crit, mishap, r, total, success, outcome = cast_a_spell(
            bonus, spell_tier, class_
        )
        context.update(
            {
                "roll_done": True,
                "crit": crit,
                "mishap": mishap,
                "r": r,
                "total": total,
                "success": success,
                "outcome": outcome,
                "bonus": bonus,
            }
        )
    return render(request, template_name, context)
