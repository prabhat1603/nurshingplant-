from django.urls import path
from . import views

app_name = "nursery"

urlpatterns = [
   path('', views.Home, name = 'home'),
   path('myshop/', views.MyShop, name = 'myshop'),
   path('allnursery/', views.AllNursery, name = 'allnursery'),
   path('deleteshop/', views.DeleteShop, name = 'deleteshop'),
   path('createnursery/', views.CreateNursery, name = 'createnursery'),
   path('addplanttomyshop/', views.AddPlantToMyShop, name = 'addplanttomyshop'),
   path('updatenursery/<int:pk>/', views.UpdateNursery, name = 'updatenursery'),
   path('myshopcollection/', views.MyNurseryCollection, name = 'myshopcollection'),

]
