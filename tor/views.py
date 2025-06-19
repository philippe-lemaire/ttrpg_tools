from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import (
    ActionResolutionForm,
    TreasureForm,
    StriderTellingTableForm,
    FortuneTableForm,
    StriderJourneyEventsForm,
    RevelationEpisodeForm,
)
from .tor_dice_roller import roller, eye, gandalf, SuccessDie, FeatDie
from .magical_treasure import MagicalTreasure
from .fortune_tables import fortune_table, ill_fortune_table
from .nameless_things import NamelessThing
from .solo_journey import Event
from .revelation_episodes_data import episodes


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
            rating = int(form.cleaned_data["hoard_rating"])
            treasure_value = sum(SuccessDie().value for _ in range(rating))
            magical_treasure = [
                MagicalTreasure(die=FeatDie()) for _ in range(rating * 2)
            ]
            suggest_magical_treasure = form.cleaned_data["suggest_magical_treasure"]

            context.update(
                {
                    "treasure_value": treasure_value,
                    "magical_treasure": magical_treasure,
                    "roll_done": True,
                    "suggest_magical_treasure": suggest_magical_treasure,
                }
            )
    return render(request, template_name, context)


def strider_telling_table_view(request):
    form = StriderTellingTableForm(request.POST or None)
    template_name = "tor/strider-telling-table.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            chance = int(form.cleaned_data["chance"])
            die = FeatDie()
            if die.value == eye:
                yes = False
            elif die.value == gandalf:
                yes = True
            elif chance == 1:
                yes = True
            elif chance == 5:
                yes = die.value == gandalf or die.value >= 10
            else:
                yes = die.value >= 2 * chance or die.value == gandalf
            context.update({"yes": yes, "die": die, "roll_done": True})
    return render(request, template_name, context)


def fortune_tables_view(request):
    form = FortuneTableForm(request.POST or None)
    template_name = "tor/strider-fortune-table.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            die = FeatDie()
            table = form.cleaned_data["table"]
            if table == "1":
                result = fortune_table.get(die.value)
            else:
                result = ill_fortune_table.get(die.value)
            context.update({"roll_done": True, "result": result, "die": die})
    return render(request, template_name, context)


def nameless_thing_view(request):
    context = {"thing": NamelessThing()}
    template_name = "tor/nameless_thing.html"
    return render(request, template_name, context)


def strider_solo_journey_view(request):
    form = StriderJourneyEventsForm(request.POST or None)
    template_name = "tor/strider-journey.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            land = form.cleaned_data["land"]
            favoured = False
            ill_favoured = False
            if land == "1":
                favoured = True
            elif land == "3":
                ill_favoured = True
            _, _, _, dice, _ = roller(
                rating=0, target_number=15, favoured=favoured, ill_favoured=ill_favoured
            )
            die = dice[0]
            event = Event(die)
            context.update(
                {
                    "roll_done": True,
                    "event": event,
                    "dice": dice,
                }
            )
    return render(request, template_name, context)


def strider_revelation_episode_view(request):
    form = RevelationEpisodeForm(request.POST or None)
    template_name = "tor/strider_revelation_episode.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            die = FeatDie()
            # TODO: gamelogic
            result = None
            context.update(
                {"roll_done": True, "result": result, "episodes": episodes, "die": die}
            )
    return render(request, template_name, context)
