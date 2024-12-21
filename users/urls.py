from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.user_profile, name="profile"),
    path("edit/", views.edit_user, name="edit_user"),
    path("password_change/", login_required(PasswordChangeView.as_view(template_name="users/password_change.html")), name="password_change"),
    path("password_change/done", login_required(PasswordChangeDoneView.as_view(template_name="users/password_change_done.html")), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path("password_reset/done", PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password_reset/confirm/<uidb64>/<token>", PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset/complete", PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
]
