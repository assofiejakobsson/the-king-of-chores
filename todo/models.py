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
    points = models.IntegerField(default=0)

    objects = TodoManager()

    def __str__(self):
        return self.title
