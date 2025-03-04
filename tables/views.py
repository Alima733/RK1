from django.shortcuts import render
from .models import Table

def tables_list(request):
    tables = Table.objects.all().values("id", "number", "seats", "is_available")
    return render(request, "tables_list.html", {"tables": tables})

def available_tables(request):
    tables = Table.objects.filter(is_available=True).values("id", "number", "seats")
    return render(request, "available_tables.html", {"tables": tables})
