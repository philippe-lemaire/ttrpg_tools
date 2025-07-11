from django.shortcuts import render
from django.views import generic

from .forms import CallingForm
from .character import Character

# Create your views here.


class BreakIndexView(generic.TemplateView):
    template_name = "break/index.html"


def break_create_character(request):
    form = CallingForm(request.POST or None)
    template_name = "break/character_creation.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            calling = form.cleaned_data.get("calling")
            context["character"] = Character(calling)

    return render(request, template_name, context)
