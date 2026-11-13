from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from into_the_odd.game_logic import roll
from .heads_and_hands import heads_and_hands

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
