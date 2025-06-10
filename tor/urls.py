from django.urls import path
from . import views

app_name = "tor"

urlpatterns = [
    path("", views.TorIndexView.as_view(), name="index"),
    path("action-resolution", views.action_resolution_view, name="action_resolution"),
    path("treasure", views.treasure_hoard_view, name="treasure"),
]
