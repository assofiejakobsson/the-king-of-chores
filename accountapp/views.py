from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo:home')

    else:
        form = UserCreationForm()
    return render(request, 'accountapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accountapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('todo:home')
