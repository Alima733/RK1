
from django.urls import path
from .views import create_reservation, reservations_list

urlpatterns = [
    path('', reservations_list, name="reservations_list"),
    path('create/', create_reservation, name="create_reservation"),
]
