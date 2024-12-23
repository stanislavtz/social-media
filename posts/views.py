from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create_post(request):
    form = CreatePostForm()

    if request.method == "POST":
        form = CreatePostForm(request.POST, files=request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

            return redirect("index")
        
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def users_post(request):
    posts = request.user.posts.all()

    context = {
        "owner": request.user.username,
        "posts": posts
    }
    
    return render(request, "posts/user_posts.html", context)


@login_required
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    user = request.user

    if post.user == user:
        return render(request, "posts/post_details.html", {"post": post})
    
    return redirect("user_post")
