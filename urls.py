from django.urls import path
from app3 import views
from django.contrib import admin

from mhz import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('index/', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
    path('create/', views.create, name="create"),
    path('login/', views.login, name="login"),
    ]
