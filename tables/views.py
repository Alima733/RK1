from django.shortcuts import render
from .models import Table

def tables_list(request):
    tables = Table.objects.all()
    return render(request, "tables_list.html", {"tables": tables})
