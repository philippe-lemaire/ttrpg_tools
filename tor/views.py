from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ActionResolutionForm
from .tor_dice_roller import roller


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
            favored = form.cleaned_data["favored"]
            ill_favored = form.cleaned_data["ill_favored"]
            weary = form.cleaned_data["weary"]
            miserable = form.cleaned_data["miserable"]
            tn_met, successes, total, feat_dice, success_dice = roller(
                rating=rating,
                target_number=target_number,
                favored=favored,
                ill_favored=ill_favored,
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
                }
            )
    return render(request, template_name, context)
