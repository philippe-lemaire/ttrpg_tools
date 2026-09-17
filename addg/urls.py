from django.urls import path

from . import views

app_name = "addg"

urlpatterns = [
    path("", views.AddgIndexView.as_view(), name="index"),
    path(
        "character-generator",
        views.addg_character_generation_view,
        name="character_generator",
    ),
]
