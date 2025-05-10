from django.shortcuts import render
from .spark_tables import spark_tables_by_theme, Spark
from .forms import SparkThemeForm
from django.views import generic
from random import choice


class MythicBastionlandIndexView(generic.TemplateView):
    template_name = "mythic_bastionland/index.html"


def spark_tables_view(request):
    form = SparkThemeForm(request.POST or None)
    template_name = "mythic_bastionland/spark_tables.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            theme = form.cleaned_data["theme"]
            tables = spark_tables_by_theme[theme]
            sparks = [Spark(table) for table in tables]
            context["sparks"] = sparks
    return render(request, template_name, context)
