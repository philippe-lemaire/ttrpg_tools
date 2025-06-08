from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TorIndexView(TemplateView):
    template_name = "tor/index.html"
