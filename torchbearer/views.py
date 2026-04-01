from random import choice
import markdown
from django.shortcuts import render
from django.views.generic import TemplateView
from .loot_tables import loot_tables_list
from .loot_subtables import loot_subtables
from .forms import CampEventForm, TwistForm, TownEventForm
from .camp_events import camp_events_table
from .dice_tools import roll, get_closest_key
from .twists import twists_data
from .town_events import town_events_table
from .town_laws import town_law_generalities, town_law_dict

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
            bonus = (
                int(form.cleaned_data["bonus_from_past_event"])
                if form.cleaned_data["bonus_from_past_event"]
                else 0
            )
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


def town_events_view(request):
    form = TownEventForm(request.POST or None)
    template_name = "torchbearer/town_events.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            town_type = form.cleaned_data["town_type"]
            town_events = town_events_table[town_type]
            # compute the bonuses and penalties to the roll
            # bonuses
            hearthmistress_favor = form.cleaned_data["hearthmistress_favor"]
            steward_skill_test_done = form.cleaned_data["steward_skill_test_done"]
            skald_established_a_court_of_the_wise = form.cleaned_data[
                "skald_established_a_court_of_the_wise"
            ]
            increate_theurge_allied = form.cleaned_data["increate_theurge_allied"]
            bonus = sum(
                (
                    hearthmistress_favor,
                    steward_skill_test_done,
                    skald_established_a_court_of_the_wise,
                    increate_theurge_allied,
                )
            )
            # penalties
            disaster_past_event = int(
                form.cleaned_data["disaster_past_event"]
                if form.cleaned_data["disaster_past_event"]
                else 0
            )
            increate_theurge_opposed = form.cleaned_data["increate_theurge_opposed"]
            penalties = disaster_past_event + increate_theurge_opposed
            modifiers = bonus - penalties

            roll_result = roll("3d6") + modifiers
            print(roll_result)
            context["event"] = town_events[get_closest_key(roll_result, town_events)]

    return render(request, template_name, context)


def twists_view(request):
    form = TwistForm(request.POST or None)
    template_name = "torchbearer/twists.html"
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            twist_type = form.cleaned_data["twist_type"]
            context["twist"] = choice(twists_data.get(twist_type))
    return render(request, template_name, context)


def law_list_view(request):
    template_name = "torchbearer/town_laws.html"
    md = markdown.Markdown(extensions=["fenced_code"])
    context = {
        "generalities": md.convert(town_law_generalities),
        "town_law_dict": town_law_dict,
    }
    return render(request, template_name, context)
