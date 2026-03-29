from django.shortcuts import render
from django.views.generic import TemplateView
from .loot_tables import loot_tables_list
from .loot_subtables import loot_subtables
from .forms import CampEventForm
from .camp_events import camp_events_table
from .dice_tools import roll, get_closest_key

# Create your views here.


class TorchbearerIndexView(TemplateView):
    template_name = "torchbearer/index.html"


def loot_tables_view(request):
    template_name = "torchbearer/loot_tables.html"
    context = {"tables": loot_tables_list}
    return render(request, template_name, context)


def loot_subtables_view(request):
    template_name = "torchbearer/loot_subtables.html"
    context = {"tables": loot_subtables}
    return render(request, template_name, context)


class TorchbearerLootRules(TemplateView):
    template_name = "torchbearer/loot_rules.html"


class TorchbearerCampEventRules(TemplateView):
    template_name = "torchbearer/camp_event_rules.html"


def camp_events_view(request):
    form = CampEventForm(request.POST or None)
    template_name = "torchbearer/camp_events.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            table_name = form.cleaned_data["table"]
            table = camp_events_table[table_name]
            # compute the bonuses and penalties to the roll
            survivalist_outdoor = form.cleaned_data["survivalist_used_for_outdoor"]
            survivalist_used_for_concealment = form.cleaned_data[
                "survivalist_used_for_concealment"
            ]
            ranger_present = form.cleaned_data["ranger_present_outdoor_camp"]
            outcast_present = form.cleaned_data["outcast_present"]
            set_watch = form.cleaned_data["set_watch"]
            bonus = int(form.cleaned_data["bonus_from_past_event"])
            danger_level = int(form.cleaned_data["danger_level"])
            modifiers = sum(
                (
                    survivalist_outdoor,
                    survivalist_used_for_concealment,
                    ranger_present,
                    outcast_present,
                    set_watch,
                    bonus,
                    danger_level,
                )
            )
            roll_result = roll("3d6") + modifiers
            print(roll_result)
            context["event"] = table[get_closest_key(roll_result, table)]

    return render(request, template_name, context)
