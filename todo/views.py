from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import TodoForm
from .models import Todo, Guest


def todo_list(request):
    user_todos = Todo.objects.filter(user=request.user)
    guest_todos = Guest.objects.filter(email=request.user.email, completed=False)
    return render(request, 'todo/todo_list.html', {'user_todos': user_todos, 'guest_todos': guest_todos})
""" 

@login_required
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
    return render(request, 'todo/todo_create.html', {'form': form})


@login_required
def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form}) """


@login_required
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    #return redirect('todo:todo_list')
    

def todo_guest_complete(request, guest_id):
    guest_todo = Guest.objects.get(id=todo_id)
    guest_todo.completed = True
    guest_todo.save()
    return redirect('todo:todo_list')   


def create_todo(request):
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
