from django.urls import path
from . import views

app_name = "tor"

urlpatterns = [
    path("", views.TorIndexView.as_view(), name="index"),
]
