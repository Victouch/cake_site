from django.urls import path
from . import views

app_name = "master_chefs"

urlpatterns = [
    path("master/", views.master_chefs, name="master_chefs")
]