from django.urls import path
from . import views

app_name = "electric_bastionland"

urlpatterns = [
    path("", views.ElectricBastionlandIndexView.as_view(), name="index"),
    path("create-character", views.create_character, name="create_character"),
    path("spark_tables", views.spark_tables_view, name="spark_tables"),
]
