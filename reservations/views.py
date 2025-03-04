from django.shortcuts import render
from .models import Reservation
from django.contrib.auth.models import User
from tables.models import Table
from django.http import JsonResponse
import json

def reservations_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations_list.html", {"reservations": reservations})

def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(id=data["user_id"])
        table = Table.objects.get(id=data["table_id"])
        existing_reservation = Reservation.objects.filter(user=user, date=data["date"]).exists()

        if existing_reservation:
            return JsonResponse({"error": "User already has a reservation on this date"}, status=400)

        reservation = Reservation.objects.create(user=user, table=table, date=data["date"])
        return JsonResponse({"id": reservation.id, "status": reservation.status})
