from django.urls import path

from . import views

app_name = "torchbearer"

urlpatterns = [
    path("", views.TorchbearerIndexView.as_view(), name="index"),
]
