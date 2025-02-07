from django.urls import path
from . import views

app_name = "grimwild"

urlpatterns = [
    path("", views.GrimwildIndexView.as_view(), name="index"),
    path("roll/", views.grimwild_roll_view, name="grimwild_roll"),
    path("roll_pool/", views.grimwild_pool_roll_view, name="grimwild_pool"),
]
