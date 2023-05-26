from django import forms
from .models import Game, Todo
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.forms import TodoForm
from .forms import GameForm


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.points = form.cleaned_data['points']
            todo.save()
            game = Game.objects.create()
            game.users.add(request.user)
            game.tasks.add(todo)
            return redirect('game:game')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})


@login_required
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            todo = Todo.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            game.todo = todo
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
