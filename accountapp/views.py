from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todo.models import Todo

# View for user registration
def register(request):
    if request.method == 'POST':
        # Create a UserCreationForm instance with the submitted POST data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new user
            user = form.save()
            # Log in the user
            login(request, user)
            # Redirect to the home page
            return redirect('todo:home')
    else:
        # Display an empty UserCreationForm for GET requests
        form = UserCreationForm()
    # Render the registration form template with the form data
    return render(request, 'accountapp/register.html', {'form': form})


# View for user login
def user_login(request):
    if request.method == 'POST':
        # Create an AuthenticationForm instance with the submitted POST data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Retrieve the authenticated user
            user = form.get_user()
            # Log in the user
            login(request, user)
            # Redirect to the home page
            return redirect('todo:home')
    else:
        # Display an empty AuthenticationForm for GET requests
        form = AuthenticationForm()
    # Render the login form template with the form data
    return render(request, 'accountapp/login.html', {'form': form})


# View for user logout
def user_logout(request):
    # Log out the user
    logout(request)
    # Redirect to the home page
    return redirect('todo:home')