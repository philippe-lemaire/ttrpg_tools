from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character
from .forms import BackgroundForm
from .astromancies import astromancies
from .artifacts import artifacts
from .psionics import psionics

# Create your views here.
# Create your views here.


class MonolithIndex(TemplateView):
    template_name = "monolith/index.html"


def generate_character(request, background=None):
    return render(
        request,
        template_name="monolith/generate_character.html",
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
        template_name="monolith/generate_with_background.html",
        context={"form": form},
    )


def astromancies_view(request):
    template_name = "monolith/d66_tables.html"
    context = {"table": astromancies, "h1": "Astromancies"}
    return render(request, template_name, context)


def artifacts_view(request):
    template_name = "monolith/d66_tables.html"
    context = {"table": artifacts, "h1": "Artifacts"}
    return render(request, template_name, context)


def psionics_view(request):
    template_name = "monolith/d66_tables.html"
    context = {"table": psionics, "h1": "Psionics"}
    return render(request, template_name, context)
