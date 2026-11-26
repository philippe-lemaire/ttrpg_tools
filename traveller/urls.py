from django.urls import path

from . import views

app_name = "traveller"

urlpatterns = [
    path("", views.TravellerIndexView.as_view(), name="index"),
    path("roll", views.traveller_skill_check_view, name="roll"),
    path("generate-world", views.generate_world_view, name="generate_world"),
    path("describe-world", views.describe_world_view, name="describe_world"),
    path("random-content", views.generate_random_content_view, name="random_content"),
    path("roll-encounter", views.encounter_view, name="roll_encounter"),
]
