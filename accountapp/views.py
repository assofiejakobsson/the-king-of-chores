from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages
from todo.models import Todo


# View for user registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo:home')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accountapp/register.html', context)


# View for user login
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo:todo_list')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')  # Add error message
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'accountapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('todo:home')
