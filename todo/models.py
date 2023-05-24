from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    user = models.ManyToManyField(User)
    todo = models.ForeignKey('Todo', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)     

    objects = models.Manager()

    def __str__(self):
        return f"Game: {self.pk}"
   

