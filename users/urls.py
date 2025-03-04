from django.urls import path
from .views import users_list, create_user, user_detail

urlpatterns = [
    path('', users_list, name="users_list"),
    path('<int:id>/', user_detail, name="user_detail"),
    path('create/', create_user, name="create_user"),
]
