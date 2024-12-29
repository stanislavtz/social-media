from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "slug", "created")
    list_filter = ("created",)
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
