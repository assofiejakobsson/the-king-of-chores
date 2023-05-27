from django import forms
from game.models import Todo, Game
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed', 'points')


class TodoCollaboratorForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        requierd=False
    )

    class Meta:
        model = Game
        fields = ['collaborators']
