from django.urls import path
from . import views


app_name = 'accountapp'


urlpatterns = [
    # User registration
    path('register/', views.register, name='register'),

    # User login
    path('login/', views.user_login, name='login'),

    # User logout
    path('logout/', views.user_logout, name='logout'),
]
