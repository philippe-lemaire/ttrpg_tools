from django.shortcuts import render
from .spark_tables import spark_tables
from .forms import SparkForm
from django.views import generic
from random import choice


class MythicBastionlandIndexView(generic.TemplateView):
    template_name = "mythic_bastionland/index.html"


def spark_tables_view(request):
    form = SparkForm(request.POST or None)
    template_name = "mythic_bastionland/spark_tables.html"
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
