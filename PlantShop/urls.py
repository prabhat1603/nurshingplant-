"""PlantShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.urls import path
from .signup import SignUp
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('home/Nursery/', include('Nursery.urls', namespace = "nursery")),
    path('home/Plant/', include('Plant.urls', namespace = 'plant')),
    path('userstatus/', views.UserStatus, name = 'userstatus'),
    path('home/User/', include('User.urls', namespace = 'user')),
    path('thanks/', views.LogoutView, name = 'thanks'),
    path('', views.WelcomePage, name = 'welcomepage'),
    path('home/', views.Home, name = 'home'),
    path('signup/', SignUp, name = 'signup'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
