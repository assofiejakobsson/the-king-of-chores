from django.shortcuts import render
from todo.models import Game

# Create your views here.


def game(request):
    user = request.user
    game_todo = Game.objects.filter(user=user)
    context = {
        'todos': game_todo
    }
    return render(request, 'game.html', context)