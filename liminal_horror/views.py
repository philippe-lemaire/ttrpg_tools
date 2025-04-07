from django.shortcuts import render
from django.views.generic import TemplateView
from .character import Character
from .fallout import Fallout
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
    return render(request, template_name, context=context)


def bloom_fallout_view(request):
    context = {"fallout": Fallout()}
    template_name = "liminal_horror/fallout.html"
    return render(request, template_name, context)
