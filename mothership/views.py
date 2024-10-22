from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character, classes_descriptions_d
from .roll import roll, roll_pc_stats_and_saves
from .forms import ClassesForm


# Create your views here.


class MothershipIndexView(TemplateView):
    template_name = "mothership/index.html"


def create_character(request):
    context = roll_pc_stats_and_saves()
    request.session.update(context)
    context["form"] = ClassesForm
    context["classes_descriptions"] = classes_descriptions_d

    return render(
        request,
        template_name="mothership/create_character.html",
        context=context,
    )


def create_character_step_2(request):
    form = ClassesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            class_ = form.cleaned_data["class_choice"]
            # create character with stats in session
            strength = request.session.get("strength", 0)
            speed = request.session.get("speed", 0)
            intellect = request.session.get("intellect", 0)
            combat = request.session.get("combat", 0)
            sanity = request.session.get("sanity", 0)
            fear = request.session.get("fear", 0)
            body = request.session.get("body", 0)
            health = roll("1d10") + 10
            wounds = 2

            character = Character(
                strength=strength,
                speed=speed,
                intellect=intellect,
                combat=combat,
                sanity=sanity,
                fear=fear,
                body=body,
                class_=class_,
                max_wounds=wounds,
                wounds=0,
                health=health,
                max_health=health,
                stress=2,
                minimum_stress=2,
                trauma_response=classes_descriptions_d.get(class_)[1],
                skills=[],
                trinket=[],
                patch=[],
                equipment=[],
                credits=roll("2d10") * 10,
                portrait="",
                name="",
                pronouns="",
            )

            # TODO update character stats depending on class
            character.update_stats()

            context = {"character": character}

            context["classes_descriptions"] = classes_descriptions_d
            return render(
                request,
                template_name="mothership/create_character.html",
                context=context,
            )

    return render(
        request,
        template_name="mothership/create_character.html",
        context={"form": form},
    )
