from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RollForm, PoolForm
from .game_logic import grimwild_roll, grimwild_pool

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


def grimwild_pool_roll_view(request):
    form = PoolForm(request.POST or None)
    template_name = "grimwild/roll_pool.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            dice = form.cleaned_data["dice"]
            # gamelogic
            dice_result, outcome = grimwild_pool(dice)
            context.update(
                {
                    "dice_result": dice_result,
                    "outcome": outcome,
                }
            )
    return render(
        request,
        template_name=template_name,
        context=context,
    )
