from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RollForm
from .game_logic import grimwild_roll

# Create your views here.


class GrimwildIndexView(TemplateView):
    template_name = "grimwild/index.html"


def grimwild_roll_view(request):
    form = RollForm(request.POST or None)
    template_name = "grimwild/roll.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            dice = form.cleaned_data["dice"]
            thorns = form.cleaned_data["thorns"]
            # gamelogic
            dice_result, thorns_result, outcome = grimwild_roll(dice, thorns)
            context.update(
                {
                    "dice_result": dice_result,
                    "thorns_result": thorns_result,
                    "outcome": outcome,
                }
            )
    return render(
        request,
        template_name=template_name,
        context=context,
    )
