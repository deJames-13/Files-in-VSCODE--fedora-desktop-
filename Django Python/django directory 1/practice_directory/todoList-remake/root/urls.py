from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="basePage"),
    path("home/", views.home, name="homePage"),
    path("view/", views.view, name="viewPage"),


    ]
