from django.urls import path
from .views import game_view, complete_task

app_name = 'game'

urlpatterns = [
    path('game/', game_view, name='game'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
]

    