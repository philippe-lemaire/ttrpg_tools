from django.urls import path
from . import views

app_name = "mythic_bastionland"

urlpatterns = [
    path("", views.MythicBastionlandIndexView.as_view(), name="index"),
    path("spark_tables", views.spark_tables_view, name="spark_tables"),
]
