from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"), 
    path("home/", views.home, name="Home Page"), 
    path("tdl/", views.todolist, name="tdl_main"),
    path("tdl/<int:id>/", views.todolist, name="tdl_list"), 
    path("<int:id>/", views.v1, name="view1"), 

]