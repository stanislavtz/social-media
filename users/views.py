from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "users/index.html")


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