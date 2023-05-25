from django import forms
from .models import Game, Todo


class GameForm(forms.ModelForm):
    todo = forms.ModelChoiceField(queryset=Todo.objects.all())

    class Meta:
        model = Game
        fields = ['todo']
