from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms

class UserRegisterForm(UserCreationForm ):
    email = forms.EmailField()

    model = User 
    fields = ["username", "email", "passdword1", "password2"]
