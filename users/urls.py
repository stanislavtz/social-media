from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.user_profile, name="profile"),
]
