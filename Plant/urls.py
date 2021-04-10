from django.urls import path
from . import views

app_name = "plant"

urlpatterns = [
   path('plantdetail/<int:pk>/', views.PlantDetail, name = 'plantdetail'),
   path('appendplant/', views.AppendPlant, name = 'appendplant'),
   path('allplants/', views.AllPlants, name = 'allplants'),
   path('', views.Home, name = 'home'),
]
