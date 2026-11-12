from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from into_the_odd.game_logic import roll


class Intergalactic_Bastionland_IndexView(TemplateView):
    template_name = "intergalactic_bastionland/index.html"


def roll_d12_d6_view(request):
    d6 = roll("d6")
    d12 = roll("d12")
    template_name = "intergalactic_bastionland/d6_d12.html"
    context = {"d6": d6, "d12": d12, "total": d6 + d12}
    return render(request, template_name, context)
