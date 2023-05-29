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


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Game(models.Model):
    users = models.ManyToManyField(User)
    guests = models.ManyToManyField(Guest)
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE
        )

    def __str__(self):
        return f"Game: {self.id}"

""" class GameManager(models.Manager):
    pass


class Game(models.Model):
    users = models.ManyToManyField(User)
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name='games'
        )

    objects = GameManager()

    def __str__(self):
        return f"Game: {self.pk}"
 """


