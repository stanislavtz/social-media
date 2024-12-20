from django.shortcuts import render, redirect
from .forms import CreatePostForm

# Create your views here.
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
