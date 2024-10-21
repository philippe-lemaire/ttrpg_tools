from django.urls import path
from . import views

app_name = "monolith"

urlpatterns = [
    path("", views.MonolithIndex.as_view(), name="index"),
    path("random", views.generate_character, name="generate_character"),
    path("choice", views.generate_with_background, name="generate_with_background"),
    path("astromancies", views.astromancies_view, name="astromancies"),
    path("artifacts", views.artifacts_view, name="artifacts"),
    path("psionics", views.psionics_view, name="psionics"),
]
