from django.shortcuts import render
from .models import Reservation

def reservations_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations_list.html", {"reservations": reservations})
