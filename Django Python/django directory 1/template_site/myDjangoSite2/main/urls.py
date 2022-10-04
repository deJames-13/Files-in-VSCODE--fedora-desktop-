
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="indexpage"),  
    path('base/', views.base, name="basepage"),
    path('home/', views.home, name="homepage"),
            
    path('<str:label>/', views.base, name="labelpage"),  
    
]