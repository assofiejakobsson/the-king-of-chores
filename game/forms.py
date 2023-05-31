""" from django import forms
from .models import Todo, Game


class GuestForm(forms.ModelForm):
   class Meta:
       model = Guest
       fields = ['name', 'email']


class GameForm(forms.ModelForm):
    todo = forms.ModelChoiceField(queryset=Todo.objects.all())

    class Meta:
        model = Game
        fields = ['todo']
  """