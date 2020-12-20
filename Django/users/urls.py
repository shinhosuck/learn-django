from django.urls import path 
from users.views import user_register

app_name = "users"

urlpatterns = [
    path("", user_register, name="register")
]