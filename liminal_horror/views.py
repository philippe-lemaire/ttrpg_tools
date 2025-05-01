from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from .character import Character
from .fallout import Fallout, FALLOUT_PARAGRAPH_DATA
from .forms import ModuleForm

# Create your views here.


class LiminalHorrorIndexView(TemplateView):
    template_name = "liminal_horror/index.html"


def generate_character(request):
    form = ModuleForm(request.POST or None)
    context = {"form": form}
    template_name = "liminal_horror/generate_character.html"
    if request.method == "POST":
        if form.is_valid():
            module = form.cleaned_data["module"]
            context.update({"char": Character(module=module), "module": module})
    return render(request, template_name, context)


def fallout_view(request):
    form = ModuleForm(request.POST or None)
    # add the correct url to post to for the form
    form.helper.form_action = reverse("liminal_horror:fallout")

    context = {"form": form}
    template_name = "liminal_horror/fallout.html"

    if request.method == "POST":
        if form.is_valid():
            module = form.cleaned_data["module"]
            fo = Fallout(module)
            context["explaination"] = FALLOUT_PARAGRAPH_DATA.get(module)
            context["fallout"] = fo
            context["module"] = module

    return render(request, template_name, context)
