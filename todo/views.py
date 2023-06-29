from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .forms import TodoForm
from django.http import JsonResponse
from .models import Todo
from django.db.models import F


def home(request):
    # Renders the home page.
    return render(request, 'todo/home.html')


@login_required
def update_completed_by(request, todo_id):
    # Updates the 'completed_by' field of a Todo object.
    if request.method == 'POST':
        completed_by = request.POST.get('completed_by', '')
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.completed_by = completed_by
            todo.save()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@login_required
def todo_list(request):
    # Renders the list of both completed an uncompleted tasks.
    completed_todos = Todo.objects.filter(
        user=request.user, completed=True).order_by('completed_by', 'title')
    completed_by_list = completed_todos.values_list(
        'completed_by', flat=True).distinct()

    uncompleted_todos = Todo.objects.filter(user=request.user, completed=False)

    completed_todos_grouped = {}
    for completed_by in completed_by_list:
        todos = completed_todos.filter(completed_by=completed_by)
        completed_todos_grouped[completed_by] = todos

    context = {
        'completed_todos': completed_todos_grouped,
        'uncompleted_todos': uncompleted_todos
    }
    return render(request, 'todo/todo_list.html', context)


@login_required
# Creates a new task.
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})


@login_required
def todo_complete(request, pk):
    # Marks a task as completed.
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        completed_by = request.POST.get('completed_by', '')
        todo.completed_by = completed_by
        todo.completed = True
        todo.save()
        return redirect('todo:todo_list')


@login_required
def todo_update(request, pk):
    # Update a task.
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_update', pk=pk)
    else:
        form = TodoForm(instance=todo)
    return render(
        request, 'todo/todo_update.html',
        {'form': form, 'completed_todo': todo})


@csrf_protect
@login_required
def todo_delete(request, pk):
    # Delete task.
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_delete.html', {'todo': todo})


@login_required
def todo_view(request, pk):
    # View task.
    todo = get_object_or_404(Todo, pk=pk)
    logged_in_user = request.user
    return render(
        request, 'todo/todo_view.html', {'todo': todo, 'user': logged_in_user})


# Crud funktion for the complted task


@login_required
def todo_completed_update(request, pk):
    # Update completed task.
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_completed_update', pk=pk)
    else:
        form = TodoForm(instance=todo)
    return render(
        request, 'todo/todo_completed_update.html',
        {'form': form, 'completed_todo': todo})


@login_required
def todo_completed_delete(request, pk):
    # Delete completed task.
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_completed_delete', pk=pk)
    return render(request, 'todo/todo_completed_delete.html', {'todo': todo})
