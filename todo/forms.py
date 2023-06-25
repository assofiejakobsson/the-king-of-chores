from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    # Additional field for completed_by (optional)
    completed_by = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Todo
        # Fields to include in the form
        fields = ['title', 'completed', 'completed_by', 'description']


