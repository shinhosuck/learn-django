from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{request.user.username} has successfully registered.")
            return redirect("users:login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
