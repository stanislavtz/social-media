from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        list_display_links = ("id", "title", "slug", "created")
        list_filter = ("created",)


admin.site.register(Post, PostAdmin)
