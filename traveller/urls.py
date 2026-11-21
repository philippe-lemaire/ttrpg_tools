from django.urls import path

from . import views

app_name = "traveller"

urlpatterns = [
    path("", views.TravellerIndexView.as_view(), name="index"),
    path("roll", views.traveller_skill_check_view, name="roll"),
]
