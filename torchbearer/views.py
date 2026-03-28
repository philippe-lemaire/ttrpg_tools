from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class TorchbearerIndexView(TemplateView):
    template_name = "torchbearer/index.html"
