from django.urls import path
from . import views
urlpatterns = [
    path("create", views.create_post, name="create_post"),
    path("user_posts/", views.users_post, name="user_posts"),
    path("<slug:slug>", views.post_details, name="post_details")
]
