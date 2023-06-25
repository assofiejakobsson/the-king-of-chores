from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    # User who owns the Todo
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # Title of the Todo
    title = models.CharField(max_length=200)

    # Description of the Todo (optional)
    description = models.TextField(blank=True, null=True)

    # Indicates whether the Todo is completed or not
    completed = models.BooleanField(default=False)

    # Name of the person who completed the Todo (optional)
    completed_by = models.CharField(max_length=100, blank=True, null=True)

    # Timestamps for creation and last update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # String representation of the Todo object (returns the title)
        return self.title
        

