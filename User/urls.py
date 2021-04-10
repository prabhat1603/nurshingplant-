from Plant import views as plant_view
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
   path('plantdetail/<int:pk>/', plant_view.PlantDetail, name = 'plantinfo'),
   path('mycart/placedOrder/', views.PlacedOrder, name = 'placedOrder'),
   path('plantlist/', plant_view.AllPlants, name = 'allplants'),
   path('addTocart/', views.AddToCart, name = 'addTocart' ),
   path('myorders/', views.MyOrders, name = 'myorders'),
   path('mycart/', views.MyCart, name = 'mycart'),
   path('', views.Home, name = 'home')
]
