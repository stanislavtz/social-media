from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
def index(request):
    return render(request, "users/index.html")


def register_user(request):
    form = RegisterForm()
    message = ""

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            repeat_password = form.cleaned_data.get("repeat_password")

            if password != repeat_password:
                message = "Password don't match"
            else:  
                print(username, first_name, last_name)
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                return redirect("login")
    
    context = {
        "form": form,
        "message": message
    }

    return render(request, "users/register.html", context)


def login_user(request):
    form = LoginForm()
    message = ""

    if request.user.is_authenticated:
        return render(request, "users/login.html")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.user.is_authenticated)
                return render(request, "users/login.html")
            else:
                message = "** Invalid username or password!"
        else:
            message = "** Invalid form. Please populate all input fields!"

    context = { 
        "form": form,
        "message": message
    }

    return render(request, "users/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    return render(request, "users/logout.html")


@login_required
def user_profile(request):
    return render(request, "users/profile.html")