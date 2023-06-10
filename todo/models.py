from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completed_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        

""" class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    

class Guest(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    email = models.EmailField()
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.email  """



# Create your models here.


""" class TodoManager(models.Manager):
    pass


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    objects = TodoManager()

    def __str__(self):
        return self.title """