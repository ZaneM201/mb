from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model): # Classes in Python follow Camel Case notation: class ProductsToSave
    title = models.CharField(max_length=128) # Text
    subtitle = models.CharField(max_length=256) # Text
    body = models.TextField() # Text
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])