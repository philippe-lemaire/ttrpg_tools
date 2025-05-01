from django.urls import path

from . import views

app_name = "liminal_horror"

urlpatterns = [
    path("", views.LiminalHorrorIndexView.as_view(), name="index"),
    path("generate-character", views.generate_character, name="generate_character"),
    path("fallouts", views.fallout_view, name="fallout"),
]
