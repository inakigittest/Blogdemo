from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title, self.content

# Create your models here.



