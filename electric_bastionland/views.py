from django.shortcuts import render
from django.views import generic
from .character import Character
from .forms import SparkForm
from random import choice
from .spark_tables import spark_tables

# Create your views here.


class ElectricBastionlandIndexView(generic.TemplateView):
    template_name = "electric_bastionland/index.html"


def create_character(request):
    template_name = "electric_bastionland/create_character.html"
    context = {"character": Character()}
    return render(request, template_name, context)


def spark_tables_view(request):
    form = SparkForm(request.POST or None)
    template_name = "electric_bastionland/spark_tables.html"
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            table_name = form.cleaned_data["table"]
            print(f"{table_name=}")
            table = spark_tables[table_name]

            left = choice(table.get("spark_1"))
            right = choice(table.get("spark_2"))
            spark = f"{left} & {right}"
            context["spark"] = spark
            context["table_name"] = table_name
            context["spark_1_name"] = table.get("spark_1_name")
            context["spark_2_name"] = table.get("spark_2_name")
            context["right"] = right
            context["left"] = left
    return render(request, template_name, context)
