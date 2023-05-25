from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoManager(models.Manager):
    pass


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    objects = TodoManager()

    def __str__(self):
        return self.title


class GameManager(models.Manager):
    pass


class Game(models.Model):
    users = models.ManyToManyField(User)
    todo = models.ForeignKey('Todo', on_delete=models.CASCADE)
    objects = GameManager()

    def __str__(self):
        return f"Game: {self.pk}"
