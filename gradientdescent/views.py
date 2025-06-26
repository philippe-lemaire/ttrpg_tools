from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

from mothership.roll import (
    roll_d10,
    roll_d100,
    check_doubles,
    doubles_value,
    get_key,
    get_reaction,
    roll_encounter_numbers,
)
from .encounters_per_floor import encounters_per_floor
from .forms import FloorForm, MonarchForm
from .artifacts import artifacts
from .random_search import random_search
from .models import Monarch
from django.http import HttpResponseRedirect
from django.urls import reverse


TABLES = {"artifacts": artifacts, "random_search": random_search}


# Create your views here.
def roll_encounters_view(request):
    form = FloorForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            floor = form.cleaned_data["floor"]
            encounters_dict = encounters_per_floor.get(floor)
            encounter_roll = roll_d100()
            encounter_present = check_doubles(encounter_roll)
            context["encounter_present"] = encounter_present
            context["roll"] = encounter_roll
            if encounter_present:
                n = roll_d10()
                distance = doubles_value(encounter_roll)
                key = get_key(n, encounters_dict)
                encounter = encounters_dict[key]
                encounter = roll_encounter_numbers(encounter)
                context["encounter"] = encounter
                context["distance"] = distance
                reaction, status = get_reaction()
                context["reaction"] = reaction
                context["status"] = status

    return render(request, "gradientdescent/roll_encounters.html", context)


def d100_table_view(request, table_name):
    template_name = "gradientdescent/d100_table.html"
    roll = roll_d100()
    table = TABLES.get(table_name)
    key = get_key(roll, table)
    context = {
        "table": table,
        "key": key,
        "table_name": table_name,
    }
    return render(request, template_name, context)


class MonarchListView(LoginRequiredMixin, ListView):
    login_url = "/admin"
    model = Monarch
    template_name = "gradientdescent/monarch_list.html"
    context_object_name = "monarchs"


@staff_member_required
def checkout_monarch(request, campaign_name):
    monarch = Monarch.objects.get(campaign_name=campaign_name)
    form = MonarchForm(request.POST or None, instance=monarch)

    form.helper.form_action = reverse(
        "gradientdescent:checkout_monarch", args=[monarch.campaign_name]
    )
    template_name = "gradientdescent/monarch_detail.html"
    context = {"form": form, "monarch": monarch}

    if request.method == "POST":
        if form.is_valid():
            # todo update the monarch
            print("form is valid")
            form.save()
            return HttpResponseRedirect(
                reverse(
                    "gradientdescent:checkout_monarch", args=[monarch.campaign_name]
                )
            )
    return render(request, template_name, context)
