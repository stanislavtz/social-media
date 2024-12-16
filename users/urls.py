from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.user_profile, name="profile"),
    path("password_change/", PasswordChangeView.as_view(template_name="users/password_change.html"), name="password_change"),
    path("password_change/done", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
]
