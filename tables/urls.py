from django.urls import path
from .views import tables_list

urlpatterns = [
    path('', tables_list, name="tables_list"),
]
