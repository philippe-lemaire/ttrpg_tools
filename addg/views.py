from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AddgIndexView(TemplateView):
    template_name = "addg/index.html"
