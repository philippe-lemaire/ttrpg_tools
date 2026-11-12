from django.urls import path

from . import views

app_name = "intergalactic_bastionland"

urlpatterns = [
    path("", views.Intergalactic_Bastionland_IndexView.as_view(), name="index"),
    path("roll-d6-and-d12", views.roll_d12_d6_view, name="roll_d6_d12"),
]
