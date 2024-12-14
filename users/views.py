from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "users/index.html")


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.user.is_authenticated)
                return redirect("index")
            else:
                print("invalid username or password!")
    return render(request, "users/login.html", { "form": form })


@login_required
def logout_user(request):
    logout(request)
    return redirect("index")
