from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
#from django.core.mail import send_mail
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import Todo
from django.db.models import F
#from .models import Todo, Guest


@csrf_exempt
@login_required
def update_completed_by(request, todo_id):
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
    completed_todos = Todo.objects.filter(user=request.user, completed=True).order_by('completed_by', 'title')
    completed_by_list = completed_todos.values_list('completed_by', flat=True).distinct()

    uncompleted_todos = Todo.objects.filter(user=request.user, completed=False)

    completed_todos_grouped = {}
    for completed_by in completed_by_list:
        todos = completed_todos.filter(completed_by=completed_by)
        completed_todos_grouped[completed_by] = todos

    return render(request, 'todo/todo_list.html', {
        'completed_todos': completed_todos_grouped,
        'uncompleted_todos': uncompleted_todos
    })


@csrf_protect
@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        todo = Todo.objects.create(title=title, user=request.user)
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_create.html')


@login_required
def todo_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        completed_by = request.POST.get('completed_by', '')
        todo.completed_by = completed_by
        todo.completed = True
        todo.save()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_complete.html', {'todo': todo})



@csrf_protect
@login_required
def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        completed_by = request.POST.get('completed_by', '')
        todo.completed_by = completed_by
        todo.completed = True
        todo.save()
        return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form})


@login_required
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo:todo_list')


@login_required
def todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_view.html', {'todo': todo})


def todo_guest_complete(request, guest_id):
    guest_todo = Guest.objects.get(id=todo_id)
    guest_todo.completed = True
    guest_todo.save()
    return redirect('todo:todo_list')   



#Crud funktion for the complted task


@login_required
def todo_completed_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_completed_update.html', {'form': form, 'completed_todo': todo})



@login_required
def todo_completed_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_completed_delete.html', {'todo': todo})


""" def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos}) """



""" def todo_list(request):
    user_todos = Todo.objects.filter(user=request.user)
    guest_todos = Guest.objects.filter(email=request.user.email, completed=False)
    return render(request, 'todo/todo_list.html', {'user_todos': user_todos, 'guest_todos': guest_todos}) """




""" @login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            # Invite the guest
            email = form.cleaned_data['email']
            guest = Guest.objects.create(todo=todo, email=email)
            
            # Send an invitation email to the guest
            send_mail(
                'Invitation to Todo List',
                f'You have been invited to collaborate on a todo list. Check it out at: {request.build_absolute_uri("/")}',
                'sender@example.com',
                [email],
                fail_silently=False,
            )

            return redirect('todo:todo_list')


    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form}) """



""" def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            # Invite the guest
            email = form.cleaned_data['email']
            guest = Guest.objects.create(todo=todo, email=email)
            
            # Send an invitation email to the guest
            send_mail(
                'Invitation to Todo List',
                f'You have been invited to collaborate on a todo list. Check it out at: {request.build_absolute_uri("/")}',
                'sender@example.com',
                [email],
                fail_silently=False,
            )

            return redirect('todo:todo_list')

    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})


 """
    








""" from django.shortcuts import render, redirect, get_object_or_404
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
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            game = Game.objects.create()
            game.users.add(request.user)
            game.todo = todo
            game.save()
            return redirect('game:game')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form' : form}) 


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
    return render(request, 'todo/todo_delete.html', {'todo': todo}) """