from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    title = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    