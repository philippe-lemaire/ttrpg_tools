from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = "dolmenwood"

urlpatterns = [
    path("random", views.create_character, name="create_character"),
    path("", views.DolmenwoodIndexview.as_view(), name="index"),
    path("encounters", views.roll_encounter, name="roll_encounters"),
]
