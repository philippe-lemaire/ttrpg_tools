from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character
from .forms import BackgroundForm


# Create your views here.
class CairnIndexView(TemplateView):
    template_name = "cairn/index.html"


def generate_character(request, background=None):
    return render(
        request,
        template_name="cairn/generate_character.html",
        context={"char": Character(background)},
    )


def generate_with_background(request):
    form = BackgroundForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            background = form.cleaned_data["background"]
            return generate_character(request, background)
    return render(
        request,
        template_name="cairn/generate_with_background.html",
        context={"form": form},
    )
