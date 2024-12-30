from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, ProfileForm, EditUserForm
from .models import Profile
from posts.models import Post

# Create your views here.
def index(request):
    posts = None
    if request.user.is_authenticated:
        posts = Post.objects.all()
    return render(request, "users/index.html", {"posts": posts})


def register_user(request):
    user_form = RegisterForm()
    profile_form = ProfileForm()
    message = ""

    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data.get("username")
            first_name = user_form.cleaned_data.get("first_name")
            last_name = user_form.cleaned_data.get("last_name")
            email = user_form.cleaned_data.get("email")
            password = user_form.cleaned_data.get("password")
            repeat_password = user_form.cleaned_data.get("repeat_password")

            if password != repeat_password:
                message = "* Password don't match"
            else:  
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                
                if not request.FILES.get("image"):
                    request.FILES["image"] = "users/NoImage.png"
                
                Profile.objects.create(user=user, image=request.FILES.get("image"))

                return redirect("login")
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
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
                return redirect("index")
            else:
                message = "* Invalid username or password!"
        else:
            message = "* Invalid form. Please populate all input fields!"

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


@login_required
def edit_user(request):
    user_form = EditUserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect("profile")
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, "users/edit_user.html", context)
