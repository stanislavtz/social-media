from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "users/index.html")


def login(request):
    form = LoginForm()
    return render(request, "users/login.html", { "form": form })
