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
    path("random-address", views.addg_gen_address_view, name="random_address"),
    path("random-bar", views.addg_get_bar_name_view, name="random_bar"),
]
