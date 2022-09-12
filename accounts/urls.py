from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logoutUser, name='logout'),

]