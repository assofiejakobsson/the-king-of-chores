from django import forms
from .models import Todo
#from .models import Todo, Guest


class TodoForm(forms.ModelForm):
    completed_by = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Todo
        fields = ['title', 'completed', 'completed_by', 'description']


