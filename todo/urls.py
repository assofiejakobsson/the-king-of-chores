from django.urls import path
from .views import todo_list
from . import views




urlpatterns = [
    path('', views.todo_list, name='todo_list')
]