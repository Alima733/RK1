from django.shortcuts import render
from django.contrib.auth.models import User

def users_list(request):
    users = User.objects.all()
    return render(request, "users_list.html", {"users": users})
