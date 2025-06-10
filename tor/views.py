from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ActionResolutionForm, TreasureForm
from .tor_dice_roller import roller, eye, gandalf, SuccessDie, FeatDie
from .magical_treasure import MagicalTreasure


# Create your views here.
class TorIndexView(TemplateView):
    template_name = "tor/index.html"


def action_resolution_view(request):
    form = ActionResolutionForm(request.POST or None)
    template_name = "tor/action_resolution.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            rating = form.cleaned_data["rating"]
            target_number = form.cleaned_data["target_number"]
            favoured = form.cleaned_data["favoured"]
            ill_favoured = form.cleaned_data["ill_favoured"]
            weary = form.cleaned_data["weary"]
            miserable = form.cleaned_data["miserable"]
            tn_met, successes, total, feat_dice, success_dice = roller(
                rating=rating,
                target_number=target_number,
                favoured=favoured,
                ill_favoured=ill_favoured,
                weary=weary,
                miserable=miserable,
            )
            context.update(
                {
                    "tn_met": tn_met,
                    "successes": successes,
                    "total": total,
                    "feat_dice": feat_dice,
                    "success_dice": success_dice,
                    "roll_done": True,
                    "weary": weary,
                    "miserable": miserable,
                    "favoured": favoured,
                    "ill_favoured": ill_favoured,
                    "eye": feat_dice[0].value == eye,
                    "gandalf": feat_dice[0].value == gandalf,
                }
            )
    return render(request, template_name, context)


def treasure_hoard_view(request):
    form = TreasureForm(request.POST or None)
    template_name = "tor/treasure.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            rating = int(form.cleaned_data["rating"])
            treasure_value = sum(SuccessDie().value for _ in range(rating))
            magical_treasure = [
                MagicalTreasure(die=FeatDie()) for _ in range(rating * 2)
            ]
            context.update(
                {
                    "treasure_value": treasure_value,
                    "magical_treasure": magical_treasure,
                    "roll_done": True,
                }
            )
    return render(request, template_name, context)
