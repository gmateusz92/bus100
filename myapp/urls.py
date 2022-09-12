from django.urls import path
from . import views

urlpatterns = [
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('booklist', views.seebookings, name="booklist"),
    path('cancellings', views.cancellings, name="cancellings")
   # path('success', views.success, name="success"),
    ]