from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from game.models import Game
from . import views
from .forms import TodoForm, TodoCollaboratorForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})


@login_required
def todo_create(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        collaborator_form = TodoCollaboratorForm(request.POST)
        if todo_form.is_valid() and collaborator_form.is_valid():
            todo = todo_form.save()
            game = Game.objects.create()
            game.todos.add(todo)
            collaborators = collaborator_form.cleaned_data['collaborators']
            game.collaborators.set(collaborators)
            return redirect('todo:todo_list')
    else:
        todo_form = TodoForm()
    return render(request, 'todo/todo_create.html', {'todo_form': todo_form})


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form})


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
