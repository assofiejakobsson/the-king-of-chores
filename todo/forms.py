from django import forms
from .models import Todo, Guest


""" class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed'] """


class TodoForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Todo
        fields = ['title', 'completed', 'email']





""" from django import forms
from game.models import Todo, Game
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed')


class TodoCollaboratorForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Game
        fields = ['collaborators'] """
