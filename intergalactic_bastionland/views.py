from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from into_the_odd.game_logic import roll
from .heads_and_hands import heads_and_hands
from .character_creation import Character
from .sparks_tables import SPARK_TABLES

app_name = "intergalactic_bastionland"


class Intergalactic_Bastionland_IndexView(TemplateView):
    template_name = f"{app_name}/index.html"


def roll_d12_d6_view(request):
    d6 = roll("d6")
    d12 = roll("d12")
    template_name = f"{app_name}/d6_d12.html"
    context = {"d6": d6, "d12": d12, "total": d6 + d12}
    return render(request, template_name, context)


def heads_and_hands_view(request):
    context = {"heads_and_hands": heads_and_hands}
    template_name = f"{app_name}/heads_and_hands.html"
    return render(request, template_name, context)


def character_creation_view(request):
    template_name = f"{app_name}/character_creation.html"
    context = {"character": Character()}
    return render(request, template_name, context)


def sparks_tables_view(request, table_name):
    template_name = f"{app_name}/sparks_tables.html"
    tables = [
        (
            table.name,
            table.table_1_name,
            table.table_2_name,
            table.get_spark(),
        )
        for table in SPARK_TABLES.get(table_name)
    ]
    context = {
        "name": table_name.title(),
        "tables_1": tables[:3],
        "tables_2": tables[3:6],
        "tables_3": tables[6:],
    }
    return render(request, template_name, context)
