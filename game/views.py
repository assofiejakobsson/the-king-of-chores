from django.shortcuts import render
from django.shortcuts import redirect
from todo.models import Todo, Game
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def game_view(request):
    user = request.user
    game_tasks = Game.objects.filter(user=user)
    context = {
        'tasks': game_tasks
    }
    return render(request, 'game.html', context)


@login_required
def complete_task(request, task_id):
    game_task = Game.objects.get(id=task_id)
    game_task.completed = True
    game_task.save()
    return redirect('game')
