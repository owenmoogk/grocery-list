from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": UserCreationForm})

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            event = form.cleaned_data
            if event.get("password1") != event.get("password2"):
                errorMsg = "Passwords do not match"
            else:
                errorMsg = "Username already exists"
            context = {
                "form": UserCreationForm,
                "error": errorMsg
            }
            return render(request, "users/register.html", context)