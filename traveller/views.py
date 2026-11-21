from django.shortcuts import render
from django.views.generic import TemplateView
from random import randint
from .forms import TravellerRollForm
from .roll import traveller_roll

# Create your views here.


class TravellerIndexView(TemplateView):
    template_name = "traveller/index.html"


def traveller_skill_check_view(request):
    template_name = "traveller/traveller_roll.html"
    form = TravellerRollForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            char_dm = form.cleaned_data["characteristic_dm"]
            skill_dm = form.cleaned_data["skill_dm"]
            dm = char_dm + skill_dm
            difficulty = int(form.cleaned_data["difficulty"])
            boon_bane = form.cleaned_data["boon_bane"]
            boon = boon_bane == "boon"
            bane = boon_bane == "bane"
            dice = traveller_roll(boon=boon, bane=bane)
            total = dice + dm
            effect = total - difficulty
            result = "✅" if effect >= 0 else "❌"
            context["dice"] = dice
            context["dm"] = dm
            context["total"] = total
            context["difficulty"] = difficulty
            context["result"] = result
            context["effect"] = effect
    return render(request, template_name, context)
