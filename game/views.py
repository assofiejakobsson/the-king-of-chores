from django.shortcuts import render
from django.shortcuts import redirect
from todo.models import Todo
from .models import Game
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.


@login_required
def game_view(request):
    user = request.user
    game_tasks = user.game_set.all()
    #game_tasks = Game.objects.filter(user=user)
    todos = [task.todo for task in game_tasks]
    context = {
        'todos': todos
    }
    '''context = {
        'tasks': game_tasks
    }'''
    return render(request, 'game.html', context)


@login_required
def complete_task(request, task_id):
    game_task = get_object_or_404(Game, id=task_id)
    game_task.completed = True
    game_task.save()
    return redirect('game:game')
