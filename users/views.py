from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def users_list(request):
    users = User.objects.all().values("id", "username", "email")
    return render(request, "users_list.html", {"users": users})

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], email=data["email"], password=data["password"])
        return JsonResponse({"id": user.id, "username": user.username})

def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, "user_detail.html", {"user": user})
