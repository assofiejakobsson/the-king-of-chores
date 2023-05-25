from django.shortcuts import render
from django.shortcuts import redirect
from todo.models import Todo
from .models import Game
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import GameForm


# Create your views here.


@login_required
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.todo_id = form.cleaned_data['todo'].id 
            game.save()
            return redirect('game:game')
    else:
        form = GameForm()
    return render(request, 'game/game_create.html', {'form': form})


@login_required
def complete_task(request, task_id):
    todo = get_object_or_404(Todo, id=task_id)
    todo.completed = True
    todo.save()
    return redirect('game:game')


@login_required
def game_view(request):
    user = request.user
    family_games = Game.objects.filter(users=user)
    context = {
        'family_games': family_games
    }
    return render(request, 'game/game.html', context)


'''@login_required
def game_view(request):
    user = request.user
    game_tasks = user.game_set.all()
    #game_tasks = Game.objects.filter(user=user)
    todos = [task.todo for task in game_tasks]
    context = {
        'todos': todos
    }
    return render(request, 'game.html', context)'''
