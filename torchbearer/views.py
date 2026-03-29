from django.shortcuts import render
from django.views.generic import TemplateView
from .loot_tables import loot_tables_list
from .loot_subtables import loot_subtables

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
